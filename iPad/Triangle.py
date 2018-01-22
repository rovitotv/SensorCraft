'''
This program started with a thread on the pythonista message boards here:
	https://forum.omz-software.com/topic/2066/python-opengles
	
but then I found the code here:
	https://github.com/Cethric/OpenGLES-Pythonista/blob/3c2332dcc31a091c0388f258e6ae4f7bbce89445/Util/Shader.py

this forum post on pythonista helped with glCreateShader:
	https://forum.omz-software.com/topic/4650/trouble-with-opengl-ctypes-and-pythonista
	
Draw a simple triangle
'''
#!python2
from ctypes import *
from objc_util import *
import time
import colorsys
import sys
from GLConstants import *

GLKView = ObjCClass('GLKView')
GLKViewController = ObjCClass('GLKViewController')
UINavigationController = ObjCClass('UINavigationController')
UIBarButtonItem = ObjCClass('UIBarButtonItem')
EAGLContext = ObjCClass('EAGLContext')

#functions defined here we should put this in a different file

#glClearColor
glClearColor = c.glClearColor
glClearColor.restype = None
glClearColor.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]

#glClear
glClear = c.glClear
glClear.restype = None
glClear.argtypes = [GLbitfield]

#glCreateShader
glCreateShader = c.glCreateShader
glCreateShader.restype = GLuint
glCreateShader.argtypes = [GLenum]

#glShaderSource
glShaderSource = c.glShaderSource
glShaderSource.restype = None
glShaderSource.argtypes = [GLuint, GLsizei, POINTER(c_char_p), POINTER(GLint)]

#glCompileShader
glCompileShader = c.glCompileShader
glCompileShader.restype = None
glCompileShader.argtypes = [GLuint]

#glGetShaderiv
glGetShaderiv = c.glGetShaderiv
glGetShaderiv.restype = None
glGetShaderiv.argtypes = [GLuint, GLenum, POINTER(GLint)]

#glGetSahderInfoLog(shader, N, byref(log_length), byref(info_log))
glGetShaderInfoLog = c.glGetShaderInfoLog
glGetShaderInfoLog.restype = None
glGetShaderInfoLog.argtypes = [GLuint, GLsizei, POINTER(GLsizei), POINTER(GLchar)]

#constants are defined here
GL_COLOR_BUFFER_BIT = 0x00004000
GL_COMPILE_STATUS = 0x8B81
GL_VERTEX_SHADER = 0x8B31
GL_FRAGMENT_SHADER = 0x8B30
GL_INFO_LOG_LENGTH = 0x8B84
GL_LINK_STATUS = 0x8B82
GL_FLOAT = 0x1406
GL_FALSE = 0x0000
GL_TRIANGLES = 0x0004

def load_shader(shader_type, shader_source):
	shader = c_uint32(0)
	compiled = c_int(0)
	
	shader = glCreateShader(shader_type)
	if shader == 0:
		print("error in load_shader")
		sys.exit(200)
	
	# load the shader source
	glShaderSource(shader, 1, byref(cast(shader_source, c_char_p)), None)

	# compile the shader
	glCompileShader(shader)
	# check the compile status
	glGetShaderiv(shader, GL_COMPILE_STATUS, byref(compiled))
	if compiled.value != 1:
		print("load shader failed to compile code %d" % (compiled.value))
		info_length = c_int32(0)
		glGetShaderiv(shader, GL_INFO_LOG_LENGTH, byref(info_length))
		if info_length.value > 1:
			N = 1024
			info_log = (GLchar * N)()
			log_length = c_int()
			glGetShaderInfoLog(shader, N, byref(log_length), cast(info_log, c_char_p))
			print("error from OpenGL compiler: %s" % info_log.value)
		return 0
	return shader
	
def glkView_drawInRect_(_self, _cmd, view, rect):
    glClearColor(1.0, 0.0, 0.0, 1.0) # red
    #glClearColor(0.0, 1.0, 0.0, 1.0) # green
    #glClearColor(0.0, 0.0, 1.0, 1.0) # blue
    glClear(GL_COLOR_BUFFER_BIT)
MyGLViewDelegate = create_objc_class('MyGLViewDelegate', methods=[glkView_drawInRect_], protocols=['GLKViewDelegate'])

def dismiss(_self, _cmd):
    print("dismiss closing down")
    self = ObjCInstance(_self)
    self.view().delegate().release()
    self.view().setDelegate_(None)
    self.dismissViewControllerAnimated_completion_(True, None)

def viewDidLoad(_self, _cmd):
    print("viewDidLoad loading up MyGLViewController")
    self = ObjCInstance(_self)
MyGLViewController = create_objc_class('MyGLViewController', GLKViewController, methods=[dismiss, viewDidLoad])

@on_main_thread
def main():
    context = EAGLContext.alloc().initWithAPI_(2).autorelease()
    glview = GLKView.alloc().initWithFrame_(((0, 0), (320, 320))).autorelease()
    delegate = MyGLViewDelegate.alloc().init()
    glview.setDelegate_(delegate)
    glview.setContext_(context)
    glview.setEnableSetNeedsDisplay_(False)
    glvc = MyGLViewController.alloc().initWithNibName_bundle_(None, None).autorelease()
    glvc.setTitle_('GLKit Demo Hello Triangle.py')
    glvc.setView_(glview)
    done_b = UIBarButtonItem.alloc().initWithTitle_style_target_action_('Done', 2, glvc, 'dismiss').autorelease()
    glvc.navigationItem().setRightBarButtonItem_(done_b)
    nav = UINavigationController.alloc().initWithRootViewController_(glvc)
    rootvc = UIApplication.sharedApplication().keyWindow().rootViewController()
    rootvc.presentModalViewController_animated_(nav, True)
    nav.release()
    vShaderStr = (b"attribute vec4 vPosition;void main(){gl_Position = vPosition;}")
    vertex_shader = load_shader(GL_VERTEX_SHADER, vShaderStr)
    fShaderStr = (b"precision mediump float; void main(void){ gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);}")
    fragment_shader = load_shader(GL_FRAGMENT_SHADER, fShaderStr)

main()