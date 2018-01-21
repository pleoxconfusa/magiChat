# magiChat

## Inspiration
In the new world of CubeSat's and the growing market of satellite photography, 
data transmission of images continues to be lossy and two-way communication 
consumes hardware space.  Islamic geometric pattern magic squares can be 
reconstructed with large portions of data missing.  


## What it does 
       o          o
        \   /\   /
         \ /* \ /
          (__*_)
    _______(oo) - I am Alfonso.
   /|  ___  \/
  / | {M U}||
 *  ||{_M_}||
    ||-----||
    ^^     ^^
    
BEHOLD, ALFONSO: OUR MAGIC COW!


This program is a PoC for a future package class.  The MMU program implements
the use of Pan-Magic Squares as a coding mechanism for 8-bit data.  The traditional
single-error correcting coding schema for 8-bit data is 17-bits long and allows 
for 1 error at a maximum sustainable error rate of 1 in 17.  Using magic squares
with error-detecting coding schemas, an 80-bit translation can be made.  A 
pan-magic square can be seen below:

| 2  5 11 12|
|15  8  6  1|
| 4  3 13 10|
| 9 14  0  7|

Using rules for pan-magic square construction, this square could be reconstructed
with the following worst-case input:

| 2  *  * 12|
| *  8  *  *|
| *  * 13  *|
| *  *  *  7|

There are 192 pan-magic squares, which is 64 short of 256, but we attempt a best
match for our reconstruction method, with priority given to values 0-192.  Our
values 193-256 are not pan-magic squares, so they require at least 9 matches.

To attain a magic square with possible accept and deny values, we encode the
required 4-bit 0-16 value as a 5-bit error detecting even parity value.

The resulting coding schema translates 8-bits to 80-bits rather than 17-bits, but
allots for a floor of 11 bits lost of 80 for 3/4 of data, and a floor off 6
bits lost of 80 for 1/4 of data, or an average floor of 12.1% data loss.

As shown in the documentation for reconstruct, the floor for error loss if worst
case bits are lost is 7.5%, and if best case bits are lost, is 68.75%

In future iterations beyond PoC we plan to implement data validation, user
error detection, and an efficient coding mapping of non-pan-magic squares to
infrequent mapped data (in other words, applying the codes with a floor of 7.5%
data loss to the most infrequently occurring data, and a floor of 12.5% data
loss to the rest).  

## How we built it
We first generated and numbered 256 magic squares into a text document, then
built a program to load an encoding and decoding dictionary scheme.  The 
program MMU.py was written to apply these schemes to messages, which are strings
in this PoC.  


## Challenges we ran into
Proving that magic squares can tolerate losses and generating those squares.
Finding a way to transmit bits over bytes in python UDP.


## What's next for MNU
Establishing encoding of images rather than strings.
Data validation.
Exception handling.
Implementation beyond PoC (python library creation).