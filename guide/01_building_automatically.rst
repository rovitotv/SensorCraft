=========================
01 Building Automatically
=========================

For a Computer Scientist code runs the world but this is true for the everyday
person on the planet earth even if they do not realize it.  Code is in your
refrigerator, microwave, car,  TV, you name it code runs the device.  We live in
the digital age.  One thing that is not apparent to most people is that when you
have the source code to your device or game you can do almost anything that you
can imagine.  When you don't have the source code then you are beholden to the
people that do have the code.  Think about your favorite game wouldn't it be
cool if you could make the rocket launch faster? Games is one thing but as a
government Computer Scientist having the source code makes it possible to verify
the system performance and understand the weakness or strength of the algorithm.
Fortunately open source software exists and is thriving today making computers
accessible to everyone. For this exercise we are going to use a simple for loop
to build a wall by pushing the 'b' key.  To get started with this programming
exercise first copy 00_flat_world_TVR.py code to a new file
01_building_automatically_TVR.py but replace TVR with your initials using the
following command::

	cp 00_flat_world_TVR.py 01_building_automatically_TVR.py

The first thing we have to do is tell the program that the 'b' key is worth
listening for so jump down to line 733 and make the adjustments as shown
below.

.. literalinclude:: ../code/01_building_automatically.py
	:lines: 703-734

Take note the method we are working on is called "on_key_press" which is a name
that makes a lot of sense because this code will be executed when a key is
pressed.  Lots of keys exist on the keyboard and for this game we only care
about the keys listed so we use a if-else if construct to execute lines of code
when that particular key is pressed.  The code is obvious when symbol is  equal
to the constant key B then execute the method build_wall().  So next would be a
good time to create the build_wall method.

.. literalinclude:: ../code/01_building_automatically.py
	:lines: 848-855

The build_wall method is created at the end of the Window class, be sure to tab
this method over two tabs or Python will be unhappy.  Python uses whitespace (in
our case the tab character) to delimit program blocks, which is a genius feature
of Python because you don't have to count braces like in many other languages. A
"for loop" is a critical structure in computer science and is often used by
programmers to repeat instructions over and over again and  increment (or
decrement) a variable.  In this case the variable is x and it will run over the
range starting at -10 and ending before 10.  Notice that for each iteration of
the for loop a block is added at a different elevation -1, 0, or 1.  We will
explain 3 dimensional coordinate systems in the next chapter.
