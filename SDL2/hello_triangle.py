# This example now works on the Raspberry Pi and the Mac!
# 
# A black triangle is displayed in a red background.
# this program is designed to duplicate the "Hello_Triangle.c" program in
# chapter 2 from OpenGL ES.  The code works but we have to perform serious
# work on the OpenGL to Ctypes bridge is functional but it is not clean and is
# difficult to use.
from ctypes import *
import time
import math
import argparse
import sys
import os
os.environ["PYSDL2_DLL_PATH"] = os.environ["HOME"] + "/prog/SDL2-2.0.4/build/.libs"
from sdl2 import *

GL_COLOR_BUFFER_BIT = 0x00004000
GL_COMPILE_STATUS   = 0x8B81
GL_VERTEX_SHADER    = 0x8B31
GL_FRAGMENT_SHADER  = 0x8B30
GL_INFO_LOG_LENGTH  = 0x8B84
GL_LINK_STATUS      = 0x8B82
GL_FLOAT            = 0x1406 # defined in gl.h line 240
GL_FALSE            = 0x0000 # defined in gl.h line 156
GL_TRIANGLES        = 0x0004

def check_sdl_error(SDL_function):
    error = SDL_GetError()
    if error:
        print("SDL Error: %s at SDL function: %s " % (error, SDL_function))
        SDL_ClearError()
        sys.exit(200)

def init_mac(data):
    SDL_Init(SDL_INIT_VIDEO)
    data['width'] = 800
    data['height'] = 480
    data['window'] = SDL_CreateWindow(b"Hello world", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, data['width'], data['height'], SDL_WINDOW_OPENGL)
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
    # the Raspberry Pi Display is 800 x 480
    SDL_Init(SDL_INIT_VIDEO)
    data['width'] = 800
    data['height'] = 480
    check_sdl_error("SDL_Init")
    SDL_GL_SetAttribute(SDL_GL_RED_SIZE, 8)
    SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 8)
    SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 8)
    SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 16)
    SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1)
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 2)
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 0)
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_ES)
    data['window'] = SDL_CreateWindow(b"Minimal SDL2 Example", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, data['width'], data['height'], SDL_WINDOW_OPENGL)
    check_sdl_error("SDL_CreateWindow")
    data['context'] = SDL_GL_CreateContext(data['window'])
    check_sdl_error("SDL_GL_CreateContext")    

def load_shader(data, shader_type, shaderSrc):
    ogl = data['opengl']
    shader = c_uint32(0)
    compiled = c_int(0)

    ogl.glCreateShader.restype = c_uint32
    #ogl.glCreateShader.args = [c_uint32,]
    shader = ogl.glCreateShader(shader_type)

    if shader == 0:
        print("error in load_shader")
        sys.exit(200)

    #ogl.glShaderSource.args = [c_uint32, c_int32, c_char_p, c_void_p]
    ogl.glShaderSource(shader, c_int32(1), byref(shaderSrc), None)

    #ogl.glCompileShader.args = [c_uint32, ]
    ogl.glCompileShader(shader)

    # GLAPI void APIENTRY glGetShaderiv (GLuint shader, GLenum pname, GLint *params);
    #ogl.glGetShaderiv.args = [c_uint32, c_uint32, c_void_p]
    ogl.glGetShaderiv(shader, GL_COMPILE_STATUS, byref(compiled))
    if compiled.value != 1:
        print("load_shader failed to compile code %d" % (compiled.value))
        info_length = c_int32(0)
        #ogl.glGetShaderiv.args = [c_uint32, c_uint32, c_int32]
        ogl.glGetShaderiv(shader, GL_INFO_LOG_LENGTH, byref(info_length))
        if info_length.value > 1:
            N = 1024
            info_log = (c_char * N)()
            log_length = c_int()
            # GLAPI void APIENTRY glGetShaderInfoLog (GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog);
            ogl.glGetShaderInfoLog(shader, N, byref(log_length), byref(info_log))
            print("Error from OpenGL compiler: %s" % info_log.value)
        return 0

    return shader

def init_common(data):
    '''init code that is common to all Platforms'''
    program_object = data['opengl'].glCreateProgram()
    if program_object == 0:
        print("program object = 0 this is bad")
        sys.exit(200)
    data['opengl'].glAttachShader(program_object, data['vertex_shader'])
    data['opengl'].glAttachShader(program_object, data['fragment_shader'])
    data['opengl'].glBindAttribLocation(program_object, 0, "vPosition")
    data['opengl'].glLinkProgram(program_object)
    # GLAPI void APIENTRY glGetProgramiv (GLuint program, GLenum pname, GLint *params);
    linked = c_int(9)
    data['opengl'].glGetProgramiv(program_object, GL_LINK_STATUS, byref(linked))
    if not linked:
        info_length = c_int32(0)
        data['opengl'].glGetProgramiv(program_object, GL_INFO_LOG_LENGTH, byref(info_length))
        if info_length.value > 1:
            N = 1024
            info_log = (c_char * N)()
            log_length = c_int()
            data['opengl'].glGetShaderInfoLog(program_object, N, byref(log_length), byref(info_log))
            print("failed to link:\n%s\n" % (info_log.value))

        data['opengl'].glDeleteProgram()
        return False
    else:
        print('shaders have been linked %d' % linked.value)

    data['program_object'] = program_object
    data['opengl'].glClearColor(c_float(1.0), c_float(0.0), c_float(0.0), c_float(0.0))
    return True

def cleanup(data):
    SDL_GL_DeleteContext(data['context'])
    SDL_DestroyWindow(data['window'])
    SDL_Quit()

def draw(data):
    GL_Float_Array = c_float * 9
    vVertices = GL_Float_Array(0.0, 0.5, 0.0,
                        -0.5, -0.5, 0.0,
                        0.5, -0.5, 0.0)

    # GLint ( x ) , GLint ( y ) , GLsizei ( width ) , GLsizei ( height ) 
    data['opengl'].glViewport(c_int32(0), c_int32(0), c_uint32(data['width']), c_uint32(data['height']))
    data['opengl'].glClear(GL_COLOR_BUFFER_BIT)
    data['opengl'].glUseProgram(data['program_object'])
    # void glVertexAttribPointer(   GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, GLvoid * pointer);
    data['opengl'].glVertexAttribPointer(c_uint32(0), c_int32(3), c_uint32(GL_FLOAT), c_bool(GL_FALSE), c_uint32(0), byref(vVertices))
    data['opengl'].glEnableVertexAttribArray(c_uint32(0))
    data['opengl'].glDrawArrays(c_uint32(GL_TRIANGLES), c_int32(0), c_uint32(3))
    SDL_GL_SwapWindow(data['window'])

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

    try:
        if data['platform'] == 'RasPi':
            data['bcm'] = CDLL("/opt/vc/lib/libbcm_host.so")
            data['opengl'] = CDLL("/opt/vc/lib/libGLESv2.so")
            init_raspi(data)
            data['opengl'].glClearColor(c_float(1.0), c_float(0.0), c_float(0.0), c_float(1.0))
            data['opengl'].glClear(GL_COLOR_BUFFER_BIT)
            SDL_GL_SwapWindow(data['window'])
            vShaderStr = c_char_p("""
                                  attribute vec4 vPosition;
                                  void main()                 
                                  {                           
                                     gl_Position = vPosition;
                                  }""")
            # take note this shader below is different for OpenGL and OpenGL ES
            fShaderStr = c_char_p("""           
                                    precision mediump float;
                                    void main(void)                                  
                                    {                                            
                                      gl_FragColor = vec4 ( 0.0, 0.0, 0.0, 1.0 );
                                    }""")
            data['vertex_shader'] = load_shader(data, GL_VERTEX_SHADER, vShaderStr)
            data['fragment_shader'] = load_shader(data, GL_FRAGMENT_SHADER, fShaderStr)        
        elif data['platform'] == 'Mac':
            # headers are here:
            #  /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/System/Library/Frameworks/OpenGL.framework/Headers
            data['opengl'] = CDLL("/System/Library/Frameworks/OpenGL.framework/Libraries/libGL.dylib")
            init_mac(data)
            data['opengl'].glClearColor(c_float(1.0), c_float(0.0), c_float(0.0), c_float(1.0))
            data['opengl'].glClear(GL_COLOR_BUFFER_BIT)
            SDL_GL_SwapWindow(data['window'])
            vShaderStr = c_char_p("""
                                  attribute vec4 vPosition;
                                  void main()                 
                                  {                           
                                     gl_Position = vPosition;
                                  }""")
            # take note this shader below is different for OpenGL and OpenGL ES
            fShaderStr = c_char_p("""           
                                    uniform vec4 vColor;
                                    void main(void)                                  
                                    {                                            
                                      gl_FragColor = vColor;
                                    }""")
            data['vertex_shader'] = load_shader(data, GL_VERTEX_SHADER, vShaderStr)
            data['fragment_shader'] = load_shader(data, GL_FRAGMENT_SHADER, fShaderStr)

        init_common(data)
        draw(data)
        time.sleep(10)
        cleanup(data)
    except:
        print "Unexpected error!!!! Trying to cleanup SDL."
        cleanup(data)