This directory is for experimental ideas.  The code in this directory most
likely will not work, use at your own risk.

OpenGL ES and EGL experiment
****************************

To get SensorCraft working on Raspberry Pi we need to look at using OpenGL ES
that might also open up Android and iOS.  By using Google's ANGLE we can in
theory write SensorCraft in OpenGL ES and still run on Windows, Macs, and
Linux.  This first experiment is an attempt to use ctypes to call OpenGL ES
and EGL.  Making this a fun project is the fact the ANGLE has a cool EGLWindow
class and Sample Application class that we might want to reuse.  This first
example will attempt to "port" the HelloTriangle example to Python.
