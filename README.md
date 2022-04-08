# mie237-reactiongame
Below you will find how to run the reaction game which was created to conduct experiments for the MIE237 (Statistics) term project. 

# 1. Setup
Make sure you have the most recent version of Python installed on your computer (although older versions may work as well).

After downloading Python to your computer, you can run the .py file through the Command Line or using an IDE of your choice. 
Either way, there is not much difference between the two.

Make sure you have all the necessary libraries also downloaded (namely pygame, time, ranodm, etc.).

# 2. Running It
There are 3 different game modes: standard, binary and integer.

The standard mode only shows red squares in a pattern which need to be replicated.
The binary mode also shows these same red squares, but additionally the numbers 0 or 1 may also be printed on the squares. At the end, the user must enter the sum of the numbers that were shown on the squares.
The integer mode is the same as binary except that now all numbers from 1 to 9 can be shown on the highlighted squares.

To change the game mode, please see the binary and integer boolean variables. To play a specific game mode, make only one of these variables True and the other False.
For the standard version, keep both False.

During the game, the last square you click in the pattern will not be highlighted and this is your indication that you have clicked the same amount of squares as what was shown in the pattern (and so the round is over).
When this occurs when playing the binary or integer version, the system will await a response from the user. Make sure to type a numerical value (representing the sum of numbers shown) on your keyboard and click enter for the next round to start.

# 3. Reading Data
Whether you ran it in command line or in an IDE, all the data will be printed in the console and seperated by trial #. When playing the standard mode, the data will be incomplete for anything related to the summation of numbers.

# 4. Improvements to be made
Better GUI for more intuitive user feedback.
