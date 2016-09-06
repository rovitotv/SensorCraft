DMX_INC =  -I/opt/vc/include/ -I /opt/vc/include/interface/vmcs_host/ -I/opt/vc/include/interface/vcos/pthreads -I/opt/vc/include/interface/vmcs_host/linux
EGL_INC = 
INCLUDES = $(DMX_INC) $(EGL_INC)

CFLAGS = $(INCLUDES)
CPPFLAGS = -march=armv7-a -mtune=cortex-a7

DMX_LIBS =  -L/opt/vc/lib/ -lbcm_host -lvcos -lvchiq_arm -lpthread
EGL_LIBS = -L/opt/vc/lib -lEGL -lGLESv2 

LDFLAGS = $(DMX_LIBS) $(EGL_LIBS)

all: window