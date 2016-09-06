# Here is where TVR makes his money!
# convert info.c to info.py and get the exact same results
# we are going to use ctypes
#
# bcm_host.h contains the function bcm_host_init and graphics_get_display_size
# the lib is called /opt/vc/lib/libbcm_host.so

import ctypes as ctypes


if __name__ == '__main__':
	bcm_host_lib = ctypes.cdll.LoadLibrary("/opt/vc/lib/libbcm_host.so")
	bcm_host_lib.bcm_host_init(None)
	#int32_t graphics_get_display_size( const uint16_t display_number,
    #                                                uint32_t *width,
    #                                                uint32_t *height);
	return_value = ctypes.c_int32(0)
	display_number = ctypes.c_uint16(0)
	width = ctypes.c_uint32(10)
	height = ctypes.c_uint32(20)
	return_value = bcm_host_lib.graphics_get_display_size(display_number, 
		ctypes.byref(width),
		ctypes.byref(height))
	print("return value: %d" % (return_value))
	print("Screen height %d, width %d\n" % (height.value, width.value))
