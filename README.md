thecargomother
==============

Code for the Houston CORE 2013 Burning Man Project: The Cargo Mother

.plan
--------------

On the arduino side the code from The Spheric Time Prism should work nearly unmodified

The PC side will be all written in python unless we write any custom video effects in C

For video playback and compositing we'll use [veejay](http://www.veejayhq.net/)

For DMX lighting control we'll use [OLA](http://code.google.com/p/open-lighting/)

Hardware
--------------
The [Hackberry A10](https://www.miniand.com/products/Hackberry%20A10%20Developer%20Board) is $65, has a fast cpu, and composite video output.

Some hacking may be required to use the gpu acceleration available with the [open source driver](http://limadriver.org/Hardware/#Allwinner+A10)

