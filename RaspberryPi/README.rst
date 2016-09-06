This directory is for the port of SensorCraft to the Raspberry Pi.  It
is not complete yet so use this code at your own risk.  The idea is to
get some simple C programs working and learn how to call the low level
Raspberry Pi API's from within Python.  The code will support two platforms
one for Raspberry Pi and the other based on Google's libangle (which is Mac
based for development and testing).

Raspberry Pi VideoCore notes
-The Raspberry Pi uses a GPU called a VideoCore IV GPU
-The API is documented here:
http://elinux.org/Raspberry_Pi_VideoCore_APIs

On the RasPi the headers and library files are in 
/opt/vc

This book is pretty good on Raspberry Pi Open GL ES and how to
get it started:
https://jan.newmarch.name/RPi/index.html

dispmanx: This shows how to access the lower level API to speak with the
video core GPU.  It is the lowest level first access to get to the GPU. This
example program gets the width and height of the display.

EGL: From the RPi viewpoint, EGL forms the link between native Dispmanx windows
and the OpenGL ES API. 
