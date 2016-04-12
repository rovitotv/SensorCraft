============
Introduction
============

Most people are familiar with Minecraft (Minecraft is developed by Mojang and
not related to this programming tutorial nor do they endorse this tutorial) for
this project we are using a Minecraft type environment created in the Python
programming language. The Air Force Research Laboratory (AFRL) Sensors
Directorate  located in Dayton, Ohio created this guide to inspire kids of all
ages to learn to program and at the same time get an idea of what it is like to
be a Scientist or Engineer for the Air Force.

Python is an amazing programming language that is a widely used high-level
programming language.  Python's design philosophy emphasizes code readability
with a code syntax that allows programmers to express concepts in fewer lines of
code than would be possible in other programming languages such as C++ or Java.
See the excellent `wikipedia page on Python
<https://en.wikipedia.org/wiki/Python_(programming_language)>`_  for more
information. To demonstrate the expressive power of Python consider that we can
create a Minecraft game in Python under 900 lines of code.  The game in this
tutorial is not a complete Minecraft clone but it is functional and offers us
the opportunity to explore adding more functions to it.

Python is used everyday at AFRL in all of our technical directorates.  Over the
last 10 years the language has excelled for science and engineering projects
with a emphasis on high performance computing. The Air Force Research Laboratory
is home to some of the `world's  fastest super computers
<http://www.top500.org/site/49284>`_,  with the most recent super computer named
Thunder which has over 125,000 CPU cores capable of computing 5.62 Petaflops and
it runs Python!

This project started with open source code from GitHub here:
https://github.com/fogleman/Minecraft

This code is open source with the original license in the file named LICENSE
take note we are permitted to use it and or modify it.  The original code is in
main.py and the original texture is called "texture.png".  Thank you fogleman
for your effort your project is an amazing foundation to build a STEM project
on. In science it is not unusual to start with somebody else's work. Sir Isaac
Newton is quoted as saying "if I have seen further, it is by standing on the
shoulders of giants". Newton was talking about how science builds upon the base
that has been built  before.  We would argue nowhere in the history of man kind
has the shoulders of giants concept been used like it has in software. Software
is easy to  replicate and share.  In Sir Isaac Newton's spirit this guide will
be on github for all to modify, edit, and add to as people see fit. I am not
perfect and I am sure this guide will have typos and mistakes please submit a
pull request.  If you make a cool programming exercise please feel free to
submit that modification via github here:

https://github.com/rovitotv/SensorCraft


Install
-------

We are using Enthought Canopy for development.  Not sure why but Enthought's web
site says pyglet comes with Canopy but it does not want to import.  So I used
the following commands::

	enpkg setuptools 
	enpkg pip 
	pip install pyglet

Now I can import pyglet which is required for this game!!!! Enthought has a
free version of Canopy called `Canopy Express 
<https://www.enthought.com/canopy-express>`_ which should work with this
code on the following operating system platforms Linux, Mac OS X, and
Windows.  

Getting Started
---------------

Each separate tutorial builds on the previous tutorial but they are designed
to stand on there own so feel free to skip around.  The tutorials start with
simple objectives and builds to more difficult objectives. To get started first
copy main.py into a new file name with the copy command like so::

	cp main.py 00_flat_world_TVR.txt

On Microsoft Windows platforms the copy command is spelled out "copy" and for
Linux and OS X the command is "cp".  The example above uses the programmer's
initials on the end of the file. 


Programming Exercises
---------------------

In this chapter we dive in with several different fun examples of extending
the SensorCraft game.  Review the examples and try the code, all of the
exercises have complete answers in the code directory in case you get stuck. 