=======================
02 3D Coordinate System
=======================

Math is everywhere in Computer Science, but not the kind of math most young
kids learn in school.  When you first start learning mathematics you start
with arithmetic which can be tedious but is necessary to build a strong
foundation for which to do more complex mathematical operations.  The good
thing about programming computers is the computer can do almost all the 
calculations for you so no need to do arithmetic.  But you still need to
have a good understanding of higher level mathematics depending on the
types of applications you are programming.  Some of the math in video games
can get complex so we will take it slow over the next few chapters.  Since
this tutorial is a block based game some of the math is simplified because
everything is a cube.  

Take note of the text in the upper left of the game window of SensorCraft, 
what are all those numbers?  

.. figure::  images/fps_and_coords_text.png
   :align:   center

The first number starting from the left is frames per second, which is a good
indicator of how well the game is  performing. Most humans need to see 20 - 25
frames per second to consider a video "smooth".  Frame rates can slow down if
the code is too complex or too many blocks have to be rendered simultaneously.
The next three numbers in parenthesis "()" are the X, Y, Z coordinates of your
character within the game space. Take note that if you start the game then
walk in a straight line the X or Z will increase.  Y increases when you jump
(push the space bar).  Any of these axis by itself is just like a number
line, the only difference is here you have 3 number lines.  

To get started with this programming exercise first copy
01_building_automatically_TVR.py code to a new file
02_3D_coordinate_system_TVR.py but replace TVR with your initials using the
following command::

	cp 01_building_automatically_TVR.py 02_3D_coordinate_system_TVR.py

This command will start a new file with all the traits of the last exercise
being the world is flat and if you press the B key a wall will be constructed.
SensorCraft and other games use a system called OpenGL, which stands for
Open Graphics Language, this system draws geometric primitives in 3D very 
fast.  Obviously a game such as SensorCraft uses many cubes, but how does 
each block type get created?  First OpenGL renders (aka displays) a cube then
it will wrap "textures" around the cube.  This is similar to wrapping a present
in real life, OpenGL will take a 2 dimensional image and wrap it around the
cube.  Textures are generally stored in a simple image file, so if you open
up texture.png you will see this:

.. figure::  code/texture.png
   :align:   center

The "texture.png" file originated from github when we cloned the repository and
designed SensorCraft.  It has the basic textures that we need. The "grass" 
texture for the side is in the lower left corner at coordinates 0, 0.  Then
the "grass" texture top is over to the right by one column at coordinates 0, 1.
Finally the bottom of the "grass" texture is in position 1, 0. Take note that 
for the sand block no matter if it is top, side, or bottom will always look the
same and be represented by the texture at coordinates 1, 1.  For this 
programming exercise we want to use numbered blocks so we generated a new
texture file called "numbered_textures.png" that looks like the following:

.. figure::  code/numbered_textures.png
   :align:   center

In order to use the new "numbered_textures.png" file you want to change the
line 71 to::

	TEXTURE_PATH = 'numbered_textures.png'

After changing the TEXTURE_PATH variable we want to add new block types for
each of the numbered stone blocks starting at line 73 append the following
codes:

.. literalinclude:: code/02_3D_coordinate_system.py
	:lines: 77-87

To make sure you don't create a typo simply copy and paste the code from the
web browser to your editor. Next we are going to adjust the initialize function
like we did in the previous programming exercise to create a number line on
the x axis and z axis.  Here is what the initialize function should look like
when you are done:

.. literalinclude:: code/02_3D_coordinate_system.py
	:lines: 164-185

We are cleverly using a for loop and placing four blocks at a time, by using a
simple negative sign we can go in both positive and negative directions 
simultaneously.  Now run the new game with the command::

	python 02_3D_coordinate_system.py

Make your character look down and take note you are standing on a 0 block, now
move forward and watch the upper left corner and pay attention to what the
display says while comparing it to the number line. Make sure you move across
both number lines while looking down.  This is fun but it is only a two 
dimensional system and obviously we are playing in a 3D world.  Think about
how you would modify the initialize method again to place number blocks on the
y axis so we have three number lines that will represent our 3D world.  The 
solution is below.

.. literalinclude:: code/02_3D_coordinate_system_part2.py
	:lines: 164-192

