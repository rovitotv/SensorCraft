# Here is where TVR makes his money!
# convert info.c to info.py and get the exact same results
# we are going to use ctypes.
#
# this program should make the display all red then output:
# Got a Dispmanx window
# Surface destroyed ok
# Main context destroyed ok
# Display terminated ok
# EGL thread resources released ok
# Dispmanx display rleased ok
from ctypes import *
import pdb

def init_egl(data):
    '''
        inits egl
    '''
    num_configs = c_int32(0)
    result = c_uint(0)
    data['bcm_host_lib'].bcm_host_init(None)
    attribute_list_type = c_int32 * 11
    attribute_list = attribute_list_type(0x3024, 8,
                                         0x3023, 8,
                                         0x3022, 8,
                                         0x3021, 8,
                                         0x3033,
                                         0x0004,
                                         0x3038)
    context_attributes_type = c_int32 * 3
    context_attributes = context_attributes_type(0x3098, 2, 0x3038)
    # typedef struct
    # {
    #     EGLDisplay display;
    #     EGLSurface surface;
    #     EGLContext context;
    #     EGLConfig config;

    #     EGL_DISPMANX_WINDOW_T nativewindow;
    #     DISPMANX_DISPLAY_HANDLE_T dispman_display;
    # } EGL_STATE_T;

    # EGL_STATE_T state = {
    #     .display = EGL_NO_DISPLAY,
    #     .surface = EGL_NO_SURFACE,
    #     .context = EGL_NO_CONTEXT
    # };
    # EGL_STATE_T *p_state = &state;

    #typedef void *EGLDisplay;
    #EGLAPI EGLDisplay EGLAPIENTRY eglGetDisplay(EGLNativeDisplayType display_id);
    #define EGL_DEFAULT_DISPLAY             ((EGLNativeDisplayType)0)
    #typedef void *EGLNativeDisplayType;
    # // get an EGL display connection
    # state->display = eglGetDisplay(EGL_DEFAULT_DISPLAY);
    pdb.set_trace()
    EGL_DEFAULT_DISPLAY = c_void_p(0)
    data['state_display'] = c_void_p()
    eglGetDisplay = data['egl_lib'].eglGetDisplay
    eglGetDisplay.argtype = [c_void_p]
    eglGetDisplay.restype = c_void_p
    data['state_display'] = eglGetDisplay(EGL_DEFAULT_DISPLAY)
    return
    # // initialize the EGL display connection
    # result = eglInitialize(state->display, NULL, NULL);
    result = data['egl_lib'].eglInitialize(data['state_display'], None, None)
    # typedef void *EGLConfig;
    data['state_config'] = c_void_p()
    result = data['egl_lib'].eglChooseConfig(data['state_display'], attribute_list, data['state_config'], 1, byref(num_configs))
    #print(result.value)
    result = data['egl_lib'].eglBindAPI(c_int(0x30A0))
    # typedef void *EGLContext;
    data['state_context'] = c_void_p()
    EGL_NO_CONTEXT = c_void_p(0)
    data['state_context'] = data['egl_lib'].eglCreateContext(data['state_display'],
        data['state_config'], EGL_NO_CONTEXT, context_attributes)


if __name__ == '__main__':
    data = {}
    data['bcm_host_lib'] = cdll.LoadLibrary("/opt/vc/lib/libbcm_host.so")
    data['GLES2_lib'] = CDLL("/opt/vc/lib/libGLESv2.so")
    data['egl_lib'] = CDLL("/opt/vc/lib/libEGL.so", mode=RTLD_GLOBAL)
    init_egl(data)
    print(data)
    print(type(data['state_display']))
