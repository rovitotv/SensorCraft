05 Pickling The World
---------------------

SensorCraft makes it fun to build objects in your world but we have no way to
save them for use in other worlds.  For this exercise we are going to  add some
new textures and create a new method that will save out the world so we can
reload it in the future.  The blocks we are going to add will be state of the
art USAF created blocks that are made out of composite material.  Composites are
now used in aircraft like the F22 Stealth Fighter and commercial aircraft. To
get started with this programming exercise first copy the file
03_show_current_block_TVR.py python code to a new file
05_pickling_the_world_TVR.py but replace TVR with your initials using the
following command::

    cp 03_show_current_block_TVR.py 05_pickling_the_world_TVR.py

First delete lines 77 - 87 as we no longer need the numbered stone blocks. 
Next we need to change the file name used for textures on line 71 change the
line to "TEXTURE_PATH = 'composite_textures.png'" without the double quotes.  
At line 77 you want to add the new composite blocks so after all the changes
above line 71 - 83 should look like the following chunk of code:

.. literalinclude:: code/05_pickling_the_world.py
    :lines: 72-83


Next we need to remove the code that placed the numbered stone blocks to
form the number lines on the axis in exercise 3.  Your _initialize method
should look like the following after all the code has been deleted:

.. literalinclude:: code/05_pickling_the_world.py
    :lines: 159-174

We now have to add the new composite blocks to our character's inventory so
modify line 472 so it looks like the following:

.. literalinclude:: code/05_pickling_the_world.py
    :lines: 472-473

Recall back to the exercise 03_show_current_block and consider what 
modifications need to be made to the draw_label method.  Within the
if/else block you need to make adjustments for the new composite 
blocks that we added your new draw_label method should be something
like:

.. literalinclude:: code/05_pickling_the_world.py
    :lines: 837-865

How do we tell the game that it can save the world?  We could spend time and
write a complicated menu system that lets a user enter a file name, but since
we are just starting out lets deploy a simple solution.  Once such solution
is to simply press a key, in this case the "L" key and the method
pickle_world will be called from the model class.  Below is what the new
on_key_press method will look like, take note of the last elif:

.. literalinclude:: code/05_pickling_the_world.py
    :lines: 707-740

Finally we implement the method that will save our world, or parts of the world
we care about.  First a little background, Python has this incredibly powerful
data structure called a dictionary.  Dictionaries allow a programmer to
associate a key to any given value.  In our case the key is X, Y, Z position of
the block and the value is the type of block like COMPOSITE_RED, COMPOSITE_BLUE,
COMPOSITE_BLACK, SAND, GRASS, BRICK, etc. You can learn more about dictionaries
in Python by reading the `data structure dictionary documentation page
<https://docs.python.org/2/tutorial/datastructures.html#dictionaries>`_.  Pickle
is another powerful capability that the Python language brings to you the
programmer, it allows you to easily save  Python objects to disk. Python objects
include almost any variable, function, or data structure including dictionaries.
We encourage you to take a look at the Python documentation page on `pickle
<https://docs.python.org/2/library/pickle.html?highlight=pickle#module-
pickle>`_.  Now we can put a complete method together to pickle our world which
we have aptly called pickle_world which is shown below.  First we create a new
dictionary called composite_world with the line "composite_world = {}", then we
use a for loop to iterate over the entire world.  A large if statement with a
number of logical "or" are used to filter out only the blocks we want saved.  If
a block is found of the COMPOSITE_ type then we save it to the dictionary called
composite_world.  Finally outside of the for loop we open a new file called
composite_world.pkl and dump the dictionary composite_world to it.  We could of
used a call to the "open" function but we used the Python "with"  statement
which will make sure the file is first opened correctly and then the file is
automatically closed when the with statement completes. Append the function
below to the bottom of the world class around line 413:

.. literalinclude:: code/05_pickling_the_world.py
    :lines: 414-429

For the pickle module to work we have to import the cPickle module by adding
a line at the top of the program around line 4:

.. literalinclude:: code/05_pickling_the_world.py
    :lines: 1-5

