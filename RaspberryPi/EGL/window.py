# Here is where TVR makes his money!
# convert window.c to window.py and get the exact same results
# we are going to use ctypes.
#
# on Raspberry Pi
# this program should make the display all red then output:
# Got a Dispmanx window
# Surface destroyed ok
# Main context destroyed ok
# Display terminated ok
# EGL thread resources released ok
# Dispmanx display rleased ok
from ctypes import *
import argparse
import sys

# error_codes = {0x3000: None, # Success code.
#                0x3001: NotInitializedError, 0x3002: BadAccessError,
#                0x3003: BadAllocError, 0x3004: BadAttributeError,
#                0x3005: BadConfigError, 0x3006: BadContextError,
#                0x3007: BadCurrentSurfaceError, 0x3008: BadDisplayError,
#                0x3009: BadMatchError, 0x300A: BadNativePixmapError,
#                0x300B: BadNativeWindowError, 0x300C: BadParameterError,
#                0x300D: BadSurfaceError, 0x300E: ContextLostError}

# define types
# Null handles for the major EGL objects.
NO_DISPLAY, NO_CONTEXT, NO_SURFACE = c_void_p(0), c_void_p(0), c_void_p(0)

c_int_p = POINTER(c_int)
c_ibool = c_enum = c_uint
c_config = c_context = c_surface = c_display = c_void_p
c_native_display = c_native_pixmap = c_native_window = c_void_p
c_client_buffer = c_void_p
c_attr_list = c_int_p
c_configs = POINTER(c_config)
c_void_fn = c_void_p # The function ext.load_ext() will cast this to a function
                     # pointer with the correct argument and return types.

EGL_DEFAULT_DISPLAY = c_void_p(0)

def make_int_p(ival=0):
    '''Create and initialise a pointer to an integer.

    Keyword arguments:
        ival -- The initial value of the referenced integer. The default
            is 0.

    '''
    p = c_int_p()
    p.contents = c_int(ival)
    return p

def init_egl(data):
    '''
        inits egl
    '''
    num_configs = c_int32(0)
    result = c_uint(0)
    if data['platform'] == 'RasPi':
        # only call this function for the RasPi
        data['bcm_host_lib'].bcm_host_init(None)

    if data['platform'] == 'RasPi':
        attribute_list_type = c_int32 * 11
        attribute_list = attribute_list_type(0x3024, 8,
                                             0x3023, 8,
                                             0x3022, 8,
                                             0x3021, 8,
                                             0x3033,
                                             0x0004,
                                             0x3038)
    else:
        attribute_list_type = c_int32 * 13
        attribute_list = attribute_list_type(0x3024, 8,
                                             0x3023, 8,
                                             0x3022, 8,
                                             0x3021, 8,
                                             0x3025, 32,
                                             0x3026, 8,
                                             0x3038)
      
    context_attributes_type = c_int32 * 3
    context_attributes = context_attributes_type(0x3098, 2, 0x3038)

    
    egl = data['egl_lib']
    # Trap EGL errors. We set the argument type for "EGLint eglGetError(void)"
    # here, since we use it for error_check. We don't set a return type, because
    # it's just an int, which is the default.
    egl.eglGetError.argtypes = ()

    # EGLDisplay eglGetDisplay(EGLNativeDisplayType display_id); ***************
    egl.eglGetDisplay.argtypes = (c_native_display,)
    egl.eglGetDisplay.restype = c_display
    data['state_display'] = egl.eglGetDisplay(EGL_DEFAULT_DISPLAY)

    # EGLBoolean eglInitialize(EGLDisplay dpy, EGLint *major, EGLint *minor); **
    egl.eglInitialize.argtypes = (c_display, c_int_p, c_int_p)
    egl.eglInitialize.restype = c_ibool
    data['major'], data['minor'] = make_int_p(), make_int_p()

    result = egl.eglInitialize(data['state_display'], data['major'], data['minor'])
    if result != 1:
        print("error eglInitialize should return a 1")
        sys.exit(200)
    print("eglInitialize Result: %d Major: %d Minor: %d" % (result, data['major'].contents.value, data['minor'].contents.value))
    
    # EGLBoolean eglChooseConfig(EGLDisplay dpy, const EGLint *attrib_list, ****
    #                            EGLConfig *configs, EGLint config_size,
    #                            EGLint *num_config);
    egl.eglChooseConfig.argtypes = (c_display, c_attr_list, c_configs, c_int, c_int_p)
    egl.eglChooseConfig.restype = c_ibool
    # Errors: BadAttributeError, BadDisplayError?, BadParameterError?
    # eglChooseConfig = error_check(egl.eglChooseConfig, fail_on=False)
    data['state_config'] = c_configs()
    result = egl.eglChooseConfig(data['state_display'], attribute_list, data['state_config'], c_int(1), byref(num_configs))
    if result != 1:
        print("error eglChooseConfig should return a 1")
        sys.exit(200)
    print("eglChooseConfig Result: %d" % (result))

    # # EGLBoolean eglBindAPI(EGLenum api); ************************************
    # # Errors: BadParameterError
    # eglBindAPI = error_check(egl.eglBindAPI, fail_on=False)
    egl.eglBindAPI.argtypes = (c_enum,)
    egl.eglBindAPI.restype = c_ibool    
    # # Errors: BadParameterError
    result = egl.eglBindAPI(c_enum(0x30A0))
    if result != 1:
        print("error eglBindAPI should return a 1")
        sys.exit(200)
    print("eglBindAPI Result: %d" % (result))


    # EGLContext eglCreateContext(EGLDisplay dpy, EGLConfig config, ************
    #                             EGLContext share_context,
    #                             const EGLint *attrib_list);
    # Errors: BadAllocError, BadConfigError, BadContextError, BadDisplayError?,
    #         BadMatchError
    #eglCreateContext = error_check(egl.eglCreateContext, fail_on=NO_CONTEXT)
    egl.eglCreateContext.argtypes = (c_display, c_config, c_context, c_attr_list)
    egl.eglCreateContext.restype = c_context
    data['state_context'] = egl.eglCreateContext(data['state_display'],
        data['state_config'],
        NO_CONTEXT,
        context_attributes)
    if data['state_context'] == None:
        error_code = egl.eglGetError()
        error_code_str = "0x%0.4X" % error_code
        print("error %s eglCreateContext should return a state_context that is not null" % error_code_str)
        sys.exit(200)
    
    # # typedef void *EGLContext;
    # data['state_context'] = c_void_p()
    # EGL_NO_CONTEXT = c_void_p(0)
    # data['state_context'] = data['egl_lib'].eglCreateContext(data['state_display'],
    #     data['state_config'], EGL_NO_CONTEXT, context_attributes)


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
        data['bcm_host_lib'] = cdll.LoadLibrary("/opt/vc/lib/libbcm_host.so")
        data['GLES2_lib'] = CDLL("/opt/vc/lib/libGLESv2.so")
        #data['egl_lib'] = CDLL("/opt/vc/lib/libEGL.so", mode=RTLD_GLOBAL)
        # do we need the mode=RTLD_GLOBAL parameter?
        data['egl_lib'] = CDLL("/opt/vc/lib/libEGL.so" )
    else:
        data['GLES2_lib'] = CDLL("/Users/rovitotv/prog/angle/out/Release/libGLESv2.dylib")
        data['egl_lib'] = CDLL("/Users/rovitotv/prog/angle/out/Release/libEGL.dylib")
    init_egl(data)
    print(data)
