import ctypes
import time
import math
import argparse
import sys
import os
os.environ["PYSDL2_DLL_PATH"] = "/Users/rovitotv/prog/SDL2-2.0.4/build/.libs"
from sdl2 import *


def init_mac(data):
	SDL_Init(SDL_INIT_VIDEO)
	window = SDL_CreateWindow(b"Hello world", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
		512, 512, SDL_WINDOW_OPENGL)
	if not window:
		print("could not create window")
		sys.exit(200)
	context = SDL_GL_CreateContext(window)


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
       # init_raspi(data)
    elif data['platform'] == 'Mac':
        data['opengles'] = ctypes.CDLL("/Users/rovitotv/prog/angle/out/Release/libGLESv2.dylib")
        data['openegl'] = ctypes.CDLL("/Users/rovitotv/prog/angle/out/Release/libEGL.dylib")
        init_mac(data)
    print(data)
    # Normal OpenGLES commands
    # data['opengles'].glClearColor ( eglfloat(1.0), eglfloat(0.0), eglfloat(0.0), eglfloat(1.0) )
    # data['opengles'].glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # # Send this to make the graphics drawn visible
    # data['openegl'].eglSwapBuffers(data['display'], data['surface'])
    # wait for 10 seconds
    #time.sleep(10)
