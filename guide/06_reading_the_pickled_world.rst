06 Reading the Pickled World
----------------------------

This exercise builds on the previous exercise named 05_pickling_the_world, be
sure to complete the previous exercise before you attempt this exercise.  The
main idea of this exercise is be able to read in a file of a world you saved
from the previous exercise.  This is helpful in the event that you create a
super cool model and want to save it for future use.  The code presented in this
exercise will assume the file to read is called "composite_world.pkl" and that
the file exists or the load_pickle method will fail.  To get started with this
programming exercise first copy the file 05_pickling_the_world.py python code to
a new file  06_reading_the_pickled_world_TVR.py but replace TVR with your
initials using the following command::

    cp 05_pickling_the_world.py 06_reading_the_pickled_world_TVR.py

Next jump down to line 432 and create a new method called "load_pickle" which
will read a pickle file and call the add_block method for each new block. The
new "load_pickle" method is shown below:

.. literalinclude:: ../code/06_reading_the_pickled_world.py
    :lines: 431-437

The last thing we need to do is modify the method "on_key_press" so when the
"O" key is pressed the "load_pickle" method is called.  The new "on_key_press"
method is listed below:

.. literalinclude:: ../code/06_reading_the_pickled_world.py
    :lines: 716-751
