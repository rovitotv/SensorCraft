=============
00 Flat World
=============

In this exercise we will modify the original code to make nothing but a flat
world with a block "fence" around it.  To get started with this programming
exercise first copy the original game's python code to a new file
00_flat_world_TVR.py but replace TVR with your initials using the
following command::

	cp main.py 00_flat_world_TVR.py

The object called "Model" starting on line 128 contains all the information
about the world and the blocks that were used to create it.  A method named
"_initialize" is used to create the world which initially is flat with a stone
fence around it from line 157 to line 192.  Then starting on line 174 - line 192
random hills are generated. To keep the world flat simply comment out that block
of code from line 174 - line 192 by placing a '#' on the first character of each
line. Below is what the _initalize method will look like after the code is
"commented out".

.. literalinclude:: ../code/00_flat_world.py
	:lines: 157-192

Now run the program "python 00_flat_world_TVR.py".  Then walk in a straight line
and eventually you will run into a stone wall.  

One more thing lets change the name of our game to Sensor Craft.  Skip down to
line 891 and change the caption parameter from "Pyglet" to "SensorCraft". Test
your title change by running the program once again "python
00_flat_world_tvr.py",  then make sure the title has been changed.

.. literalinclude:: ../code/00_flat_world.py
	:lines: 890-895
