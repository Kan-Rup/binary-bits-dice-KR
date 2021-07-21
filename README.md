
Binary Dice (two methods for getting the function of a six sided cube dice, from binary bits)
==============================================================================================

Table of contents
==============================================================================================

    #0 -- Licence

    #1 -- Binary-Dice Project
    
    #2 -- Program description
    
    #3 -- Notable Features

    #4 -- How to install the program / How to use the program
    
    #5 -- Reason why this program was made
    
    END -- List of authors / modifications




0# -- LICENCE
------------------------------------------------------------------------------------------------------

This code is provided to you under the licence :  GNU GENERAL PUBLIC LICENSE | Version 3 or later

                            https://www.gnu.org/licenses/gpl-3.0.html

                            
Date of first Publishing : 15/07/2021 , Author ('binary_dice_07_21.py') : Kanishka Rupasinghe
© Copyright (2021) Kanishka Rupasinghe (program : binary bits dice / 2 methods).


If the code of the program or files of the project are modified (and if you adapt this code from 
open source and under licence), you must mark that code as having been altered, and you must mark 
youself who made the alterations in some identifiable way, as the author of code or file changes, 
in this README file (END section authors/modifications list) and in the code file itself. 
So there will be a history of who made what changes.
 

personal statement:
------------------------------------------------------------------------------------------------------
 
There is no warranty whatsoever for this software. KR states that there most probably is room for
parts of the first code to be implemented in better ways. Some parts of the first code are 
most probably flawed.

Please be aware that the open source code can be accessed by other developers, and any such developer
may change the code according to their own intents. 

------------------------------------------------------------------------------------------------------



#1 -- Binary-Dice Project::
------------------------------------------------------------------------------------------------------

The physical cube dice can be rolled to get a random number in the range 1 - 6. This program
tests two methods which use binary bits to get that same function. The end results of the program
indicate that one of these methods may be suitable for this requirement.

You can consider this program to be a part of a proof that binary bits (digital or physical) can
be used for getting the same function as a physical cube dice. i.e. there are ways to implement
this binary dice physically and I can confirm that (method-2) dice is very usable. 
(KR) neither encourages nor recommends gambling. This program was inspired by a want for 
a make-it-yourself dice for board games and gamebooks, where a cube dice was not at hand.



First version of this program was made by KR during the time of [May 2021 to mid July 2021].
It is very possible that this idea has been done before by other people or at least has been 
thought of before, and such product may exist from before this was made. 
If not, this will be a first version of implementing of the idea, product published first on 
15/07/21 by KR.

The first-program concept was not caused or inspired by any other existing code project or product,
KR had not personally seen any other similar project, so no such attribution can be made.



This is a console program, and it is run in a terminal window. After launching the program, You 
can interact with it by reading its output text, and then selecting and entering the option letters
from the menus. So, there is no GUI or GUI windows for this program.

Python is the programming language used in this program. I made use of Python as it may be suitable
for beginners who are learning programming. That is, it is easier for me to program in, in these 
early stages of personal coding, and it may also be easy to read for an early student of coding.



I note that this program has many lines of code (also comment lines and whitespace). In the end the 
whole file grew into a larger size than I expected, because I went after a more complete program. 
In future I will try to make smaller program files.




#2 -- Program description::
-----------------------------------------------------------------------------------------------------
The program gives the option to roll the binary-bits-dice once, or to roll the dice multiple
times. In both cases the program then asks whether to use method 1 or method 2. 

When rolling the dice multiple times, the program further prompts user to give the number of rolls
to be done in each set, and also how many sets of rolls to be done. 
The number of sets that were input are then rolled, and a file is made on program's directory, 
where all values rolled can be read by the user. 

In addition to displaying the averages of the dice-values that were rolled, the program displays
a bar chart of dice-value occurence proportions. If these bars have similar lengths (after a large 
number of rolls are done), the user could assume that, with that specific method used, the dice-values
have equal chance of occuring (so it is similar to the cube dice).

You can read the information on the two methods used, by selecting option #3 from main menu.
-----------------------------------------------------------------------------------------------------




#3 -- Notable Features::
-----------------------------------------------------------------------------------------------------

+++ this is an interactive console program.

+++ two separate core methods (one method has dice-value probabilities same as the cube-dice.)

+++ Single roll of the binary dice is possible.

+++ Multiple rolls of the binary dice is possible (specify number of rolls in a 'set', and number of sets).

+++ Multiple dice roll, in the end creates a data file for user, and displays a bar chart (dice-value averages).

+++ There is a menu option which provides information to the user on the two methods used.

+++ User's input values are validated by the program.

+++ The functions are grouped as : 
        interface functions / control functions / variable-data-storage functions / file input output functions.
        
        
        
        
#4 -- How to install the program / How to use the program::
-----------------------------------------------------------------------------------------------------

A simple way to get the code to your computer is to download the code as a zip file.
The option to download the project files as zip file is presented by the repository page,
(check green download button with text 'code').

To get the code on this repository, you can also use 'Git clone' operation (the url used for this is 
provided by the repository page (check green download button with text 'code').



Once you have the project directory in a place of your choosing on computer, you can run the program
by opening a terminal window at the project directory,

    'binary_dice_07_21.py' is the file that will be run.

    and at the terminal, type in : python3 binary_dice_07_21.py

(at the point of first uploading this project, Python 3.9.2 was used.)

(you might have to modify execute clearance for the file, so choose on that.)

The program should then run, and it should then present you with the main menu of the program.



To see which method of calculation is similar to the cube-dice function, use the multiple roll.
You could first enter a small number of rolls and a small number of sets. Then you would see
the averages of dice-values, and the bar chart. 

Progress toward the maximum number of rolls per set and maximum number of sets. You should
see a pattern (in the bar chart) of the bars taking a regular shape. (In addition to the
cube-dice point, this would show that over a large number of rolls, there is a pattern of occurence).

Where all bars of dice-values take the same length, that binary dice has similarity to the cube-dice.




#5 -- Reason why this program was made::
-----------------------------------------------------------------------------------------------------

The first program was written for educational purposes, for students of coding - to inspect the code 
and to try understand what's been done.

The important parts of the whole program have been commented to help the reader understand what has been coded.

The practical project instruction was meant for coding beginners, but this specific program grew in size,
that a complete beginner might not deal with it well. So, I may have to write a smaller core program also.

I will still keep this program in my collection as an example complete program.

I went into coding the dice-roll methods not knowing if right cube-dice probabilities would be possible.
And yes, the first method I coded has a different specific probability pattern. So I tried coding
a second (less complicated) method, and I'm happy to say that this one seems to have probability closer to the
cube dice. Both methods can be used, but in one of them, the mid values are more common than the end values.

note:: this program depends on the random number generating mechanism used by the python function for
generating random numbers in a given range, and to what extent the resulting numbers are really random.



END -- List of authors / modifications
-----------------------------------------------------------------------------------------------------


    DATE            ID                              CONTACT DETAIL                          MODIFICATION
        
    -------------------------------------------------------------------------------------------------
    
    15/07/2021      Kanishka K Rupasinghe           kanrup@gmail.com                        The first version of the program was published.
                                                    techieartisans.com (2021)
    
    -------------------------------------------------------------------------------------------------


