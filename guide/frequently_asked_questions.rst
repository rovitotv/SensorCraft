==========================
Frequently Asked Questions
==========================

What version of Python is required?
-----------------------------------

SensorCraft currently supports Python 2.7 and Python 3.X.  We have tested 
the software with Enthought Canopy version 1.7.x and Enthought Canopy 
version 2.1.3 which supports both Python 2.7 and Python 3.5.  Please make sure
you download and install the correct version of Python on your computer so
SensorCraft will run.  The `install section of the guide 
<http://sensorcraft.readthedocs.io/en/latest/intro.html#install>`_ has all 
the details and steps you through installing a Enthought Canopy with 
Python 2.7 or Python 3.X.

Error "AttributeError: 'Window' object has no attribute 'label'"
----------------------------------------------------------------

This is an error that is created with undefined interactions between Enthought
Canopy and Pyglet.  A workaround is to restart your kernel between running
the SensorCraft exercises `which is explained in the SensorCraft guide
<http://sensorcraft.readthedocs.io/en/latest/intro.html#restart-of-the-python-kernel>`_.

Error "IOError: [Errno 2] No such file or directory: 'texture.png'"
-------------------------------------------------------------------

This usually happens because you are trying to run a SensorCraft program with
out being in the code directory.  The `changing directory section of the guide
<http://sensorcraft.readthedocs.io/en/latest/intro.html#changing-directory>`_
should be able to help you solve this problem.

Error "NameError: name 'xrange' is not defined"
-----------------------------------------------

This error should no longer appear it was fixed when we ported the code
to support Python 3.X.  If you see this error please make sure you
get the latest version and run the code again. The `install section of 
the guide <http://sensorcraft.readthedocs.io/en/latest/intro.html#install>`_ 
steps you through installing a Enthought Canopy with Python 2.7 and/or
Python 3.5 support..


Error "ImportError: cannot import name gl_info"
-----------------------------------------------

This error is caused because you are not running the correct version of pyglet.
The error is easily rectified by carefully reading the `install section of the 
guide <http://sensorcraft.readthedocs.io/en/latest/intro.html#install>`_.


Can I play SensorCraft on my tablet?
------------------------------------

Unfortunately not yet hopefully in the near future SensorCraft will work on
tablets.  

Can I play SensorCraft on a Raspberry Pi?
-----------------------------------------

Unfortunately not yet hopefully in the near future SensorCraft will work on
the Raspberry Pi platform.