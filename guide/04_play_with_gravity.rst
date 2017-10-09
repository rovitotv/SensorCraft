04 Play with Gravity
--------------------

As the main programmer of SensorCraft we are in control, nothing is off limits.
Our only limitation is our imagination and programming skill.  Imagination is
not in short supply but programming skill is something that needs to be
developed.  Simulations, aka video games, have some challenging aspects some of
which we have already covered.   Performance is a must with any video game
because if a high frame rate is not maintained then the user will be 
disappointed.  Since we are in control why not have a little fun and experiment
with some of the game's constants such as gravity.

To get started with this programming exercise first copy the original game's
python code to a new file 04_play_with_gravity_TVR.py but replace TVR with your
initials using the following command::

	cp main.py 04_play_with_gravity_TVR.py

This command will start a new file with the original game's traits so the world
will be random with multiple hills and valleys.  At the very top of the new
Python program you will see many variables that are being set, it is a
programming practice to name all constants with capital letters.  First cut the
gravity in half by changing line 21 to "GRAVITY = 10.0", don't use the quotes.
After you make the change run the program and jump to see how that effects
things.  Next set the MAX_JUMP_HEIGHT to 5, which is specified in number of
blocks, by changing line 22 to "MAX_JUMP_HEIGHT=5.0".  Experiment with GRAVITY
and MAX_JUMP_HEIGHT trying to create an environment similar to what you think it
would be like on the moon. With the right settings you can actually jump between
each hill top easily. For fun lets say your character just consumed a box of
candy and drank 12 cans of soda, then you should set the WALKING_SPEED on line
18 to 10.  My changes from the start of the program to line 33 look like the
following:

.. literalinclude:: ../code/04_play_with_gravity.py
	:lines: 1 - 33

