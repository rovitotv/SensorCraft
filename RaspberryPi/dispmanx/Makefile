DMX_INC =  -I/opt/vc/include -I/opt/vc/include/interface/vmcs_host/ -I/opt/vc/include/interface/vcos/pthreads -I/opt/vc/include/interface/vmcs_host/linux

INCLUDES = $(DMX_INC)

CFLAGS = $(INCLUDES)
CPPFLAGS = -march=armv7-a -mtune=cortex-a7

DMX_LIBS =  -L/opt/vc/lib/ -lbcm_host -lvcos -lvchiq_arm -lpthread
LDFLAGS =  $(DMX_LIBS)

all: info