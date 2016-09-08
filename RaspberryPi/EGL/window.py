# This project on github has the best example of getting the Raspberry Pi
# display initalized and making two simple openGL commands:
#       https://github.com/peterderivaz/pyopengles
#
# The prepare_constants.py program scans the headers and creates egl.py and
# gl2.py.  It seems to work well but no arguments or results are defined so
# it might not be that robust.  
#
# Not working on the Mac yet with libAngel
import ctypes
import time
import math
# Pick up our constants extracted from the header files with prepare_constants.py
from egl import *
from gl2 import *
import argparse
import sys

# Define verbose=True to get debug messages
verbose = True

# Define some extra constants that the automatic extraction misses
EGL_DEFAULT_DISPLAY = 0
EGL_NO_CONTEXT = 0
EGL_NO_DISPLAY = 0
EGL_NO_SURFACE = 0
DISPMANX_PROTECTION_NONE = 0
eglint = ctypes.c_int
eglshort = ctypes.c_short
eglfloat = ctypes.c_float

def eglints(L):
    """Converts a tuple to an array of eglints (would a pointer return be better?)"""
    return (eglint*len(L))(*L)

def eglfloats(L):
    return (eglfloat*len(L))(*L)
                
def check(e):
    """Checks that error is zero"""
    if e==0: return
    if verbose:
        print 'Error code',hex(e&0xffffffff)
    raise ValueError

def init_raspi(data, depthbuffer=False):
    """Opens up the OpenGL library and prepares a window for display"""
    if data['platform'] != "RasPi":
        print("Wrong platform for called init_raspi")
        sys.exit(200)
    b = data['bcm'].bcm_host_init()
    assert b==0
    data['display'] = data['openegl'].eglGetDisplay(EGL_DEFAULT_DISPLAY)
    assert data['display']
    r = data['openegl'].eglInitialize(data['display'], 0, 0)
    assert r
    if depthbuffer:
        attribute_list = eglints(     (EGL_RED_SIZE, 8,
                                  EGL_GREEN_SIZE, 8,
                                  EGL_BLUE_SIZE, 8,
                                  EGL_ALPHA_SIZE, 8,
                                  EGL_SURFACE_TYPE, EGL_WINDOW_BIT,
                                  EGL_DEPTH_SIZE, 16,
                                  EGL_NONE) )
    else:
        attribute_list = eglints(     (EGL_RED_SIZE, 8,
                                  EGL_GREEN_SIZE, 8,
                                  EGL_BLUE_SIZE, 8,
                                  EGL_ALPHA_SIZE, 8,
                                  EGL_SURFACE_TYPE, EGL_WINDOW_BIT,
                                  EGL_NONE) )
    # EGL_SAMPLE_BUFFERS,  1,
    # EGL_RENDERABLE_TYPE, EGL_OPENGL_ES2_BIT,
                                                                
    numconfig = eglint()
    config = ctypes.c_void_p()
    r = data['openegl'].eglChooseConfig(data['display'],
                                 ctypes.byref(attribute_list),
                                 ctypes.byref(config), 1,
                                 ctypes.byref(numconfig));
    assert r
    r = data['openegl'].eglBindAPI(EGL_OPENGL_ES_API)
    assert r
    if verbose:
        print('numconfig=%d' % numconfig.value)
    context_attribs = eglints( (EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE) )
    data['context'] = data['openegl'].eglCreateContext(data['display'], config,
                                    EGL_NO_CONTEXT,
                                    ctypes.byref(context_attribs))
    assert data['context'] != EGL_NO_CONTEXT
    width = eglint()
    height = eglint()
    s = data['bcm'].graphics_get_display_size(0,ctypes.byref(width),ctypes.byref(height))
    data['width'] = width
    data['height'] = height
    assert s>=0
    dispman_display = data['bcm'].vc_dispmanx_display_open(0)
    dispman_update = data['bcm'].vc_dispmanx_update_start( 0 )
    dst_rect = eglints( (0, 0, width.value, height.value) )
    src_rect = eglints( (0, 0, width.value<<16, height.value<<16) )
    assert dispman_update
    assert dispman_display
    dispman_element = data['bcm'].vc_dispmanx_element_add ( dispman_update, dispman_display,
                              0, ctypes.byref(dst_rect), 0,
                              ctypes.byref(src_rect),
                              DISPMANX_PROTECTION_NONE,
                              0 , 0, 0)
    data['bcm'].vc_dispmanx_update_submit_sync( dispman_update )
    nativewindow = eglints((dispman_element,width,height));
    nw_p = ctypes.pointer(nativewindow)
    data['nw_p'] = nw_p
    data['surface'] = data['openegl'].eglCreateWindowSurface( data['display'], config, data['nw_p'], 0)
    assert data['surface'] != EGL_NO_SURFACE
    r = data['openegl'].eglMakeCurrent(data['display'], data['surface'], data['surface'], data['context'])
    assert r

def init_mac(data):
    if data['platform'] != "Mac":
        print("Wrong platform for called init_raspi")
        sys.exit(200)
    # glesMajorVersion = 2
    # glesMinorVersion = 0
    # requestedRender = EGL_PLATFORM_ANGLE_TYPE_DEFAULT_ANGLE
    # width = 1280
    # height = 720
    # nm libangle_util.a | grep 'CreateOSWindow'
    # 0000000000002e70 T __Z14CreateOSWindowv
    # header files are /util/osx/

if __name__ == '__main__':
    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--platform', required=False,
        help = ('Platform RasPi or Mac default is RasPi'))

    args = parser.parse_args()
    data = {}
    data['args'] = args
    if args.platform:
        if args.platform == 'Mac':
            data['platform'] = 'Mac'
        else:
            data['platform'] = 'RasPi'
    else:
        # default to RasPi
        data['platform'] = 'RasPi'

    if data['platform'] == 'RasPi':
        data['bcm'] = ctypes.CDLL("/opt/vc/lib/libbcm_host.so")
        data['opengles'] = ctypes.CDLL("/opt/vc/lib/libGLESv2.so")
        data['openegl'] = ctypes.CDLL("/opt/vc/lib/libEGL.so" )
        init_raspi(data)
    elif data['platform'] == 'Mac':
        data['opengles'] = ctypes.CDLL("/Users/rovitotv/prog/angle/out/Release/libGLESv2.dylib")
        data['openegl'] = ctypes.CDLL("/Users/rovitotv/prog/angle/out/Release/libEGL.dylib")
        init_mac(data)
    print(data)
    # Normal OpenGLES commands
    data['opengles'].glClearColor ( eglfloat(1.0), eglfloat(0.0), eglfloat(0.0), eglfloat(1.0) )
    data['opengles'].glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # Send this to make the graphics drawn visible
    data['openegl'].eglSwapBuffers(data['display'], data['surface'])
    # wait for 10 seconds
    time.sleep(10)

