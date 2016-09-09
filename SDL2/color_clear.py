# code works on Raspberry Pi and Mac
# on Raspberry Pi you can not have x-windows running
import ctypes
import time
import math
import argparse
import sys
import os
os.environ["PYSDL2_DLL_PATH"] = os.environ["HOME"] + "/prog/SDL2-2.0.4/build/.libs"
from sdl2 import *

GL_COLOR_BUFFER_BIT = 0x00004000


def check_sdl_error(SDL_function):
    error = SDL_GetError()
    if error:
        print("SDL Error: %s at SDL function: %s " % (error, SDL_function))
        SDL_ClearError()
        sys.exit(200)

def init_mac(data):
    SDL_Init(SDL_INIT_VIDEO)
    check_sdl_error("SDL_Init")
    data['window'] = SDL_CreateWindow(b"Hello world", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 512, 512, SDL_WINDOW_OPENGL)
    check_sdl_error("SDL_CreateWindow")
    data['context'] = SDL_GL_CreateContext(data['window'])
    check_sdl_error("SDL_GL_CreateContext")
    #Set our OpenGL version.
    # SDL_GL_CONTEXT_CORE gives us only the newer version, deprecated functions are disabled
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE)

    # 3.2 is part of the modern versions of OpenGL, but most video cards whould be able to run it
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 2);

    # Turn on double buffering with a 24bit Z buffer.
    # You may need to change this to 16 or 32 for your system
    SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);

    # this makes our buffer swap syncronized with the monitor's vertical refresh
    SDL_GL_SetSwapInterval(1)

def init_raspi(data):
    SDL_Init(SDL_INIT_VIDEO)
    check_sdl_error("SDL_Init")
    SDL_GL_SetAttribute(SDL_GL_RED_SIZE, 8)
    SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 8)
    SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 8)
    SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 16)
    SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1)
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 2)
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 0)
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_ES)
    data['window'] = SDL_CreateWindow(b"Minimal SDL2 Example", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 512, 512, SDL_WINDOW_OPENGL)
    check_sdl_error("SDL_CreateWindow")
    data['context'] = SDL_GL_CreateContext(data['window'])
    check_sdl_error("SDL_GL_CreateContext")

  # print_gl_string(GL_RENDERER);
  # print_gl_string(GL_SHADING_LANGUAGE_VERSION);
  # print_gl_string(GL_VERSION);
  # print_gl_string(GL_EXTENSIONS); 


def cleanup(data):
    SDL_GL_DeleteContext(data['context'])
    SDL_DestroyWindow(data['window'])
    SDL_Quit()


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
        # headers and lib are located in /opt/vc/include
        data['bcm'] = ctypes.CDLL("/opt/vc/lib/libbcm_host.so")
        data['opengl'] = ctypes.CDLL("/opt/vc/lib/libGLESv2.so")
        init_raspi(data)
    elif data['platform'] == 'Mac':
        # headers are here:
        #  /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/System/Library/Frameworks/OpenGL.framework/Headers
        data['opengl'] = ctypes.CDLL("/System/Library/Frameworks/OpenGL.framework/Libraries/libGL.dylib")
        init_mac(data)

    data['opengl'].glClearColor(c_float(1.0), c_float(0.0), c_float(0.0), c_float(1.0))
    data['opengl'].glClear(GL_COLOR_BUFFER_BIT)
    SDL_GL_SwapWindow(data['window'])
    time.sleep(5)
    
    cleanup(data)
    # Normal OpenGLES commands
    # data['opengles'].glClearColor ( eglfloat(1.0), eglfloat(0.0), eglfloat(0.0), eglfloat(1.0) )
    # data['opengles'].glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # # Send this to make the graphics drawn visible
    # data['openegl'].eglSwapBuffers(data['display'], data['surface'])
    # wait for 10 seconds
    #time.sleep(10)
