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
[This table](http://techwatch.keeward.com/geeks-and-nerds/arduino-vs-raspberry-pi-vs-cubieboard-vs-gooseberry-vs-apc-rock-vs-olinuxino-vs-hackberry-a10/) covers info on our options

The microntroller for Spheric Time Prism was the [Arduino Mega 2560](http://arduino.cc/en/Main/arduinoBoardMega2560) and that is a good choice here

The [Hackberry A10](https://www.miniand.com/products/Hackberry%20A10%20Developer%20Board) is $65, has a fast cpu, and composite video output.
Some hacking may be required to use the gpu acceleration available with the [open source driver](http://limadriver.org/Hardware/#Allwinner+A10)
We'll also need a [suitable output cable](http://www.ebay.com/sch/sis.html;jsessionid=91D76C1D761FCD7EF759132D64DEB17A?_nkw=Creative%20Zen%20Vision%20M%2030GB%2060GB%20Audio%20Video%20Composite%20AV%20TV%20RCA%20Cable%20Cord&_itemId=140873354903#vi-content)

Veejay only works with I-frames so hardware video decoding is useless for us

Files
--------------
enc.sh - encode videos for use with veejay
test-veejay-play.py - initial test of sending commands to veejay
