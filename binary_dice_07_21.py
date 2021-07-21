
    #+++ binary bits dice / two methods - (use of 0/1 bits to get the same function as the 6 sided cube dice) +++
    #
    #Copyright (C) 2021 Kanishka Rupasinghe (KR)
    #
    #This program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.
    #
    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.
    #
    #You should have received a copy of the GNU General Public License
    #along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
    
    
    
    # PLEASE READ THE README FILE - details relevant to the project are written there.
    # PLEASE READ THE LICENCE DOCUMENT.
    #
    # (relevant to Section #5)  
    #
    # If you adapt or modify the code of this program, or files of the project
    # directory into a work of your own, 
    # THEN YOU MUST MARK THAT CODE AS HAVING BEEN CHANGED, AND MARK YOURSELF IN
    # in some identifable way as the author of those changes, and also mark the
    # relevant date. You can do this in this code file itself in comment form.
    #
    # There is a authors/modifications list in the README file.
    # You would update that with the relevant details and changes made also.
    # (so, there will be a history of who made what changes).
    #
    # 
    #
    #
    #++(INTRO)++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #
    #Hey there! This is the Binary-Bits-Dice program.
    #
    #Please note, the code below is not perfect. Most probably there are better ways to do parts of this program.
    #
    #About the code: It has one class, which contains all of its functions and variables.
    #
    #The most notable functions in the program are : def doSingleRoll / def doSetRoll / def multipleRollSetTest.
    #
    #The program itself makes use of two main methods (or algorithms to use a fancy word).
    #
    #It has some interface functions which takes user's input, and prints out text to the screen.
    #It has a set of functions which work with the data variables (such as setting values to the variables).
    #It has the set of functions which do the main work tasks and the processing of the program.
    #It has one main function to output the processed results to a computer file (a file Input/Output function).
    #There is one function which is used to display a simple chart of the processed results.
    #
    #It also imports and makes use of code if two language library modules : 'random' and 'decimal'
    #Such modules are code tools provided by the language developers for the coders to use in their own programs.
    #You can see those being added to this program right at the top of the file. ('import' statements).
    #
    #
    #the program code starts at the 'import' statements (below following comments)
    #
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #
    # 
    #
    #COMMENTS
    #----------
    #
    #These lines which start with a '#' are comments. They are ignored by the
    #program when its run. They are used for communication with human readers
    #like you who will be reading the program code.
    #
    #I've added extra comments throughout the program. I've added extra comments 
    #to the more noteworthy functions.I haven't explained everything though. 
    #
    #Have a look at the code and see if you can get an idea of what the code 
    #might be doing. If you're new to coding, don't worry if you can't read most 
    #of the code! Just have a look to see what it is like and have a go at trying 
    #to read it!
    #
    #It might get a bit tricky when a function uses another function within itself.
    #So you might have to refer to that other function to get an idea of what it
    #is doing.
    #
    #
    #
    #TERMS used in the program:
    #----------------------------
    #
    # bit : a 'bit' is a digit which is either 0, or 1. this bit could also be represented by something like a coin 
    #       (heads/tails).
    #
    # method 1 / 2 : you can get the info on both of these by running the program and selecting the info option.
    #
    # to read that info within this file:
    #
    # method 1 : see the function 'def displayHowMethod1Calculated'
    # method 2 : see the function 'def displayHowMethod2Calculated'
    # (you can use your text editor's search function to get to these quick).
    #
    # dice : the dice here has a set of bits, 4 bits or 3 bits depending on method.
    #        but in the end, the resulting value of rolling the dice is still supposed to be a random value from 1 - 6.
    #
    # roll : assigning random 1/0 values to the bits of the dice, then calculating the resulting dice value using these.
    # roll-set : when a certain number of multiple rolls are done, these rolls are stored in one list, a roll-set.
    #
    #
    # ===(program code starts below)==================================================================================


    


import random;          #a module used here for generating random numbers
from decimal import *;  #used in one place of the program for coverting one type of number to another type.



class BinaryDice:


    # class VARIABLES (Data is stored in these)
    #=============================================================================

      
    #4 BITs : 2 bin bits / 2 add bits (for method 1)
    firstPlace, secondPlace, addOne, addTwo = 0,0,0,0;
    
    #3 BITS : bin-1, bin-2, bin-3 (for method 2)
    binaryOne, binaryTwo, binaryThree = 0,0,0;



    #A variable to hold all roll values of a single roll-set
    #
    #this variable will be holding multiple number lists.
    #(so the variable is a list of lists.)
    #
    #e.g. [ [1,0,0,4] , [0,0,1,1] , [0,1,0,2] ]
    #
    resultList = [];


    #this variable is for storing a collection of roll-sets.
    #
    # ( a list that holds multiple list-of-lists! )
    #
    #e.g. [ [[0,0,1,1],[1,0,1,5],[1,1,0,6]] , [[1,0,0,4],[0,0,1,1],[0,1,0,2]] ]
    #
    rollsetValuesList = [];


    #(methodFlag)
    #A variable whose value is checked by other functions of the program.
    #
    #value 1 = method 1, value 2 = method 2
    #
    methodFlag = 1;


    #=============================================================================





    #(in some other languages, { } brackets are used to indicate scope of functions)
    #
    #IN PYTHON, FUNCTION/STRUCTURE SCOPE IS DEFINED BY USING INDENTATION / TABS.
    #So, pay attention to what extent the statements are indented.
    #
    #
    # varName = "some text";
    #
    # def functionA(self):
    #   
    #   varSpeed = 10;
    #
    #
    # def functionB(self):
    #
    #   varWeight = 50;
    #
    # 
    # in above, functionA has no way of knowing/accessing 'varWeight' variable
    # because varWeight is defined in the separate other scope of
    # functionB. 
    # 
    # both functionA and functionB can access the variable 'varName'
    #




    #=================================================================================================
    #
    #INTERFACE FUNCTIONS
    #
    #Functions that interact with the user. input from screen/keyboard and text output to screen.
    #
    #once the functions take the input from user, then they trigger the processing functions.
    #the user's given input are provided to these.
    #after the processing is done, the processing functions then send the results-data to
    #interface functions again (which output the data to screen).
    #
    #some of the below functions print text information to the screen for the user to see.
    #some of the functions ask user for an input (enter a number or a letter.)
    #   these input functions have to do some extra work to validate that the input the user gave
    #   was acceptable (user might enter values that are invalid.)



    #display main menu
    #
    def displayMainMenu(self):

        #this is one of the longer functions. I've divided it into smaller sections using the blank space
        #to make it more readable for you.



        #'print' function outputs the text thats been typed into the round-brackets.
        #i.e. text to output to screen has been passed into the 'parameter' of the function print.
       
        #' \n ' makes a new-line in the printing. the next text that comes starts at the start of next line.

        print("\n - - - Binary Dice : 2 methods - - -");

        menutext1 = "Please enter number (1) to roll dice once , (2) to do multiple rolls , ";
        menutext2 = "(3) to see how dice value is calculated, (4) for Help / About info,  (q) to exit program\n?-";




        #user's input number, letter (or invalid input value) is stored in 'selectedOption'. this data has a type of 'string' (text) 
        #'input' function takes text input from keyboard.
        
        selectedOption = input(menutext1 + menutext2);




        #first we check if the input is letter q or Q.
        #if so the function ends, and the program ends.
        #
        #the main menu function gets called (!!by the main menu function itself) 
        #each time the user's input task is completed.
        #
        #so at the point user enters 'q', user would already have completed
        #his/her tasks in previous occurences of the main menu function.

        if(selectedOption == 'q' or selectedOption == 'Q'):

            print("good-bye!");
            return;



        #try / except : this is similar to try / catch in some other languages
        #
        #'try' block tries to execute some code instructions, but by using try / except
        #the coder has indicated to expect poisslbe errors or exceptions to occur.
        #the errors to watch for are indicated at 'except'
        #
        #if the errors indicated occur, the except blocks trigger and their instructions are
        #carried out.
        #so the errors are 'caught' and handled.



        optionInteger = 0;

        try:
            
            #try to change selectedOption value to int (integer type data). store in optionInteger if successful.

            optionInteger = int(selectedOption); 
       

        except ValueError: 

            #if a 'ValueError' error gets thrown while trying above, it would mean a letter or symbol was present in the string of text.
            #We've already checked for the text letter q/Q. So this here input is invalid.

            #the main menu is displayed again. after indicating an error was caught.

            print("\nError! Sorry, please enter number 1 (1 roll), 2 (multiple rolls), 3 (method info), 4 (Help & About info), or q (exit program)");
          


            #note that displayMainMenu function is calling displayMainMenu function itself, again.
            
            self.displayMainMenu(); 


            #'return' instructs the function to stop at this point. 
            #(its possible to instruct for the to return a certain data value)
            #e.g: return 18
            
            return 



        #after we made sure its a number value, we check if it's in range (1 - 4)
        if(optionInteger < 1 or optionInteger > 4):

            str1 = "Error! Sorry, please enter 1 (roll once), 2 (roll multiple times)";
            str2 = "\n or 3 (display calculation method), or 4 (help and about info),\n"; 
            str3 = "or q (to exit program)";  

            print(str1+str2+str3);

            self.displayMainMenu();


        else: 

            #if the input is valid (a value of 1 , 2 , 3, 4)
            #
            #check which specific input it is (if / elif)
            #do different tasks for each different input


            if optionInteger == 1:

                #roll the dice just once, and get the result printed to screen.


                self.userChoosesRollDice();


            #'elif' is python for 'else-if'

            elif optionInteger == 2:

                #roll the dice multiple times (some number of sets, some number of rolls in each)
                #a text file record of all the rolls made is also created at the end. 


                self.userChoosesRollSetRoll(); 


            elif optionInteger == 3:

                #this option is used to display information on the method that is used to get the value of each dice-roll.
                #
                #with this option, a further input is asked for, to select which specific information the user wants (there are two methods).  



                print("\n");
                opt = input("there are two methods used here, which one to display info about? please enter ' 1 ' or ' 2 ' . enter ' c ' to cancel.\n?-");
                
                intopt = 10;



                #' != ' means 'is not equal to'
                #puting 'or' instead of 'and' here would make the code malfunction. can you see why this is? 
                
                if(opt != 'c' and opt != 'C'):

                    try:
                    

                        intopt = int(opt); 

                        #if int conversion succeeded, check if value is in range.

                        if(intopt < 1 or intopt > 2):                             

                            print("error! Sorry, please enter '1' or '2'");
                            print("returning to main menu...");

                        else:

                            if(intopt == 1):
                                self.displayHowMethod1Calculated(); #display method 1 info

                            elif(intopt == 2):
                                self.displayHowMethod2Calculated(); #display method 2 info




                    except ValueError:

                        #int conversion did not succeed.

                        print("Error! Sorry, please enter ' 1 ' or ' 2 '");
                        print("returning to main menu...");


                else: #input is c or C

                    print("info display cancelled!");



            elif optionInteger == 4:

                self.userChoosesAboutInfo();



            #once the input option's tasks are done, this same main menu is presented again.

            self.displayMainMenu();






    #prompt user for method
    #
    def promptUserForMethod(self):

        #because two methods are available for use, the program uses the below function to ask the user which one it should use,
        #and it takes the user's choice as input. 



        print("\n\nplease enter which method to use : method 1--[2 bit binary number and 2 adding bits] or method 2--[3 bit binary number, skip 0 and 7]");
       
        meth = "";
        methInt = None; #'none' in python has some similarity with 'null' in other languages. here it was just set as an initial value   

        cancelFlag = 0;



        while(True):

            #this is a 'while loop'
            #
            #because the condition check of the loop has been set directly to 'True',
            #the tasks in this block will be done continously for ever, until
            #the 'break' keyword is met. the 'break' keyword indicates:
            #come out of the loop and carry on down the function's next steps.


            meth = input("please enter 1 or 2. you can enter 'c' to cancel this prompt.\n?-");


            #if the value inputted is 'c' or 'C' (exit option), a value is set to the
            #cancelFlag variable to indicate user has chosen to cancel
            #and after this the prompting loop ends (keyword 'break').
            #
            #if the statement 'break' is reached, the loop exits, and
            #the rest of the loop instructions are not done.

            if(meth == 'c' or meth == 'C'):

                print("cancelling prompt...");

                cancelFlag = 1;
                
                break;

            else: 

                try:

                    #get user input
                    methInt = int(meth);

                    if(methInt < 1 or methInt > 2):

                        raise ValueError();
                    
                    else:

                        break;

                except ValueError:

                    print("Error! Sorry, input is out of range - please enter ' 1 ' for method 1 and ' 2 ' for method 2, to cancel this prompt enter 'c'");

                    continue;


        #returns user input option 1 or 2, 
        #if user has indicated to cancel the operation,
        #returns letter 'c' which indicates that choice.

        if(cancelFlag == 0):

            print("received, thanks");
            return methInt;

        elif(cancelFlag == 1):
            return 'c'



    #about information 
    #detailing the title, copyright, non-warranty info, licence info
    #
    def userChoosesAboutInfo(self):

        print("\n\n\nHELP INFORMATION");
        print("======================");
        print("");
        print("this program presents to you two ways of using binary bits to get the same (or similar) function as the cube-dice.");
        print("There are three main options you can select, from the main menu.");
        print(""); 
        print("------------------------------------------------------------------------------------------------------------------");
        print("option 3 : use this option to get INFORMATION on the 2 METHODS.");
        print("");
        print("after entering '3', enter '1' to get the information on method-1 , and '2' to get information on method-2.");
        print("");
        print("single-roll and multiple-roll asks to enter which method to use, before the rolling is done...so,");
        print("I recommend reading through these two first, to get an idea of what is being done in either of the methods.");
        print("------------------------------------------------------------------------------------------------------------------");
        print(""); 
        print("------------------------------------------------------------------------------------------------------------------");
        print("option 2 : use this option to roll the binary dice multiple times.");
        print("You will be asked which method to use ('1' or '2')");
        print("You will be asked to 'enter number of repeats in rollset' (this means, enter how many dice-rolls will be done in each set of rolls)");
        print("You will be asked to 'enter number of rollsets' (this means, enter how many sets-of-rolls will be done)");
        print("");
        print("so 10 repeats, 2 rollsets means : two sets of rolling will be done, and in each of these sets, 10 actual castings of the dice will be done.");
        print(""); 
        print("once these inputs are given, the processing of the task by the computer will start. In the end, you will be presented with:");
        print("1:number of occurences of each dice value, for each set of rolling, 2: dice-value-occurence average over all sets,");
        print("3:and also a bar chart, which displays the proportions of these average values graphically.");
        print("------------------------------------------------------------------------------------------------------------------");
        print(""); 
        print("------------------------------------------------------------------------------------------------------------------");
        print("option 1 : use this option to roll the binary dice just one time.");
        print("You will then be asked which method to use.");
        print("The result of the single-roll will then be displayed on screen.");
        print("------------------------------------------------------------------------------------------------------------------");
        print("");
        print("\n"); 

        print("ABOUT INFORMATION");
        print("=================");
        print("");
        print("\n\n+++ binary-bits-dice / two methods - (use of 0/1 bits to get the same function as the 6 sided cube dice) +++");
        print("[Version:1]--[Patch:1]--[Label:Binary digit order]--[dev:KR]--[Date:16/07/21]");
        print("");
        print("Copyright © (2021) Kanishka Rupasinghe");
        print("");
        print("This program comes with ABSOLUTELY NO WARRANTY");
        print("This software is licenced under GPLv3 or later version");
        print("Please read licence document for licencing details and rights relevant to you");
        print("Readme file also contains relevant information");

        print("\n(help and about information was printed above)");


    #user chooses roll dice
    #
    def userChoosesRollDice(self):

        #user has selected to roll the dice once, for a number from 1 - 6.
        
        #this function signals the control function single-roll to start,
        #with end result of displaying on screen the random numbers rolled, 
        #and calculated decimal value.

        meth = self.promptUserForMethod();

        if(meth == 'c'):
            return 'c';

        #sets the methods to be used for the rolling
        self.setMethod(meth);

        #do the dice roll according the that method
        self.doSingleRoll();




    #print single roll results
    #
    def printSingleRollResults(self,randBins,value):

        #prints the single roll values to screen.
        #do-single-roll control function makes use of this.

        print("\n\n===========================================");
        print("random roll results: "+str(randBins) );
        print("processed decimal value: "+str(value) );
        print("===========================================\n\n");




    #user chooses roll-set roll
    #
    def userChoosesRollSetRoll(self):

        #user has chosen to do one or many sets of dice-rolls.
        #user can choose to roll-dice once or multiple times per each set



        #get the method choice        
        meth = self.promptUserForMethod();
        
        if(meth == 'c'):
            return 'c';

        self.setMethod(meth);



        reps = 0;
        sets = 0;

        #use the functions 'get number of repeats' and
        #'get number of sets'. these let the user input
        #how many rolls to do in each set, and how many
        #sets to do.

        print("\n");

        try:

            reps = self.getNumberOfRepeats();

            if(reps == 'c' or reps == 'C'):

                print("Cancelling multiple roll...");
                return 'c';


            sets = self.getNumberOfSets();

            if(sets == 'c' or sets == 'C'):

                print("Cancelling multiple roll...");
                return 'c';


            print("\n");

            print("SETS NUMBER: "+str(sets), " , REPEATS-per-set NUMBER: "+str(reps) , );



        except ValueError:
        
            #(you can set further expections to be triggered: e.g. TypeError below) 
            #( these exceptions have to have handlers defined: i.e.:
            # 'except TypeError' )
            #
            #raise TypeError #(causes a TypeError exception to be triggered)

            print("= = = please enter a value in the correct range = = =\n");



        #trigger the control function ' multiple roll set test', which does the job.
        #the number of sets and repeats inputs are also passed on here.

        self.multipleRollSetTest(reps,sets);






    #get number of repeats
    #
    def getNumberOfRepeats(self):

        #this function gives the option for the user to choose and enter the number of dice-rolls in each set.
        #
        #a roll-number range of 1 to 1000 per each set has been coded into this function
        #(but this was upto the coder's liking. more or less is possible).
        #
        #input validating is done as necessary.

        
        while(True):

            inputString = input("Please enter number of repeats in rollset (number from 1 to 1000) , enter ' c ' to cancel this prompt:");

            number = -1;


            #'continue' instruction : this instructs to stop going down to the nextinstruction, 
            #and to go into the start of next repeat of the loop. 

            
            if(inputString == None or inputString == ""):
                print("Error! no value was given...\n");
                continue;

            if(inputString == 'c' or inputString == 'C'):
                return 'c';

            try:
                x = int(inputString);

            except ValueError:
                
                print("= = = please enter a value of integer number type = = =\n");
                continue;


            number = int(inputString);


            if(number < 1 or number > 1000):     
                
                print("Error! input number is out of range!");
                continue;

            else:
                return number;


            #this loop only repeats if input is out of range, or if non-integer/non-cancel-code value is inputted.
            break;





    #get number of sets
    #
    def getNumberOfSets(self): 

        #this function gives the option for the user to choose and enter the number of (dice-roll) sets.
        #
        #a set range of 1 to 250 been coded into this function
        #(but this was upto the coder's liking. more or less is possible).
        #
        #input validating is done as necessary.


        while(True):

            inputString = input("Please enter number of rollsets (number from 1 to 250), enter ' c ' to cancel this prompt:");
            number = -1;

            if(inputString == None or inputString == ""):
                print("Error! no value was given...\n");
                continue;

            if(inputString == 'c' or inputString == 'C'):

                return 'c';


            try:
                x = int(inputString);

            except ValueError:

                print("= = = please enter a value of integer number type = = =\n");
                continue;
 

            number = int(inputString);


            if(number < 1 or number > 250):
                
                print("Error! input number is out of range!");
                continue;

            else:
                return number;


            #this loop continues only if input number is out of range, or if non-integer/non-cancel-code input is given. 
            break;





    #display roll set collection stats
    #
    def displayRollSetCollectionStats(self, rollsets):

        #see also function 'multipleRollSetTest' which makes use of this function

        #the data 'rollsets' is inputted to this function when this function is called.
        #
        #'rollsets' is a list of lists, and this is made at the end of the function which carries out       
        # multiple-set dice-rolls.
        #
        # after all dice rolls sets have been rolled, a process  goes through all the roll-results,
        # and for each set of rolls, counts up the number of times value 1 has come up, 2 has come up, 3, 4, 5, 6.
        # these occurence countings are put in a list, and count-list corresponds to dice-roll set. 
        #
        # (rollsets)
        # --------------------------------------------------------------------------------------------------------------
        # set 1 [ set 1 value (1) count, 1 value (2) count, value (3) count, value (4), value (5), value (6) ] 
        # set 2 [ set 2 value (1) count, 2 value (2) count, value (3) count, value (4), value (5), value (6) ] 
        # set 3 [ set 3 value (1) count, 3 value (2) count, value (3) count, value (4), value (5), value (6) ]  
        # set 4 [ set 4 value (1) count, 4 value (2) count, value (3) count, value (4), value (5), value (6) ]
        # --------------------------------------------------------------------------------------------------------------




        #TOTALS local variables
        
        t1 = 0; t2 = 0; t3 = 0; t4 = 0; t5 = 0; t6 = 0;

        #AVERAGES local variables

        av1 = 0; av2 = 0; av3 = 0; av4 = 0; av5 = 0; av6 = 0;



        #get the number of (dice-roll) sets there are in the data collection
        rollsetNum = len(rollsets);



        print("\n");
        print(" SET #1 = the first set of dice rolls that were rolled");
        print(" val-3 = cube-dice value number 3");
        print(" (15) times = that cube dice value occured 15 times in that set of rolls");
        print("\n");


        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        #displaying the 'rollsets' data collection data on the screen.
        #also total up the counts of each dice-value over all sets.
        #
        #
        #below is the use of a 'for loop'
        # i in range(num)  code uses that python syntax for indexing, 
        #
        #detail : the number of sets in rollsets is found above, and
        #from this number, 'range' function is used to get the range : number 0 to number (rollsetNum - 1) 
        #the for-loop cycles from value 0 to value rollsetNum-1 , and that value is stored in the local variable ' i '
        #
        #
        #the variable i is accessed in the body of the loop cycle , 
        #e.g. if i = 1,  rollsets[i][4] means : 'access the number of occurences of dice-roll value-5, in the roll-set number 2' 
        #
        # ( note : the first loop starts at index 0 , and the second looping then has index of 1 , 3rd has index 2 etc )
        # ( note : in a list of [2,3,4,5] , the value at index #0 --> 2 , and the value at index #3 --> 5 )
        #
        for i in range(rollsetNum):

            print( "SET #"+str(i+1) );

            print("val-1 ("+str(rollsets[i][0])+") times, val-2 ("+str(rollsets[i][1])+") times, val-3 ("+str(rollsets[i][2])+") times, val-4 ("
                    +str(rollsets[i][3])+") times, val-5 ("+str(rollsets[i][4])+") times val-6 ("+str(rollsets[i][5])+") times");
            print("------------------------------------------------------------------------------------------------------");



            #the 'rollsets' dataset contains the 'counts' of occurences of value 1,2,3,4,5,6 (please refer to comments 
            #at start of this function).
            #
            #here the 1 counts of all sets are totaled together, the 2 counts of all sets are totaled together, etc.
            #for this,
            #since the for loop cycles through the indexes of each roll-set, at each set,
            #the count amount of dice-value(1) is added to Totals Local variable t1, count amount of value(2) is added to t2, etc 

            t1 += rollsets[i][0];
            t2 += rollsets[i][1];
            t3 += rollsets[i][2];
            t4 += rollsets[i][3];
            t5 += rollsets[i][4];
            t6 += rollsets[i][5];


        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



        #the average values of each dice-value can be found by dividing the total-variable-value, by the number of roll-sets.
        
        av1 = t1 / rollsetNum;
        av2 = t2 / rollsetNum;
        av3 = t3 / rollsetNum;
        av4 = t4 / rollsetNum;
        av5 = t5 / rollsetNum;
        av6 = t6 / rollsetNum;

        
        #the averages are displayed on the screen :

        print("\n");
        print("Below are the average occurences of each of the cube dice values, caulculated using all roll sets");
        print("==============================================================================================================================");
        print(" Average of 1: "+str(av1)+"\n Average of 2: "+str(av2)+"\n Average of 3: "+str(av3)+
                "\n Average of 4: "+str(av4)+"\n Average of 5: "+str(av5)+"\n Average of 6: "+str(av6));
        print("==============================================================================================================================");


        #the average values are collected onto a list,
        #and handed to 'display stats chart' function, which displays the average values in a bar chart on screen.  

        averages = [av1,av2,av3,av4,av5,av6];

        self.displayStatsChart(averages); 




    #display stats chart
    #
    def displayStatsChart(self,averages):

        #this function takes the average values of each dice value occurence in the roll-set collection,
        #
        #it divides each of the average values by the smallest average value
        #   this scales down all the numbers to smaller values, while keeping the same proportions between them
        #   this makes the each chart bar more likely to fit onto the computer screen.
        #but if the minimum average is 0, the averages are not divided.
        #
        #
        #then the strings of text that will be output to screen are prepared and displayed.
        #the 'averagesNext' values are used in setting the length of each bar
        #
        #
        #don't worry too much about this function. its an extra.
        #
        #I had to do some research and use some extra machinery to get the divided scaled-down values suitable for
        #display as chart bars. (because the divided values come in 'float' number type, while we need 'integer'
        #number type for the bars. so don't worry if those parts are confusing.



        #find the minimum of the averages
        minimumValue = min(averages);

        #this variable will hold the scaled-down averages
        averagesNext = []; 

        #this time I've used an 'iterable.' to cycle through the list
        #this can also be done by using a 'for' loop.
        #
        #below statement is used to get an iterable of the 'averages' list.
        averagesIterable = iter(averages);

        #another averages iterable also made for different procedure.
        averagesContrastCheckIterable = iter(averages);


        #-------------------------------------------------------------------------------------------------------------------
        #sometimes in an averages set, there can be a small lowest average and a very large maximum average value.
        #chart made out of this kind of set sometimes does not display well, the largest bars sometimes take too much space,
        #spilling to a line below.
        #
        #so here a check is being made for this kind of extreme contrast
        #with the aim of indicating, if there are very large averages, divide every bar length by 2, 
        #so the chart can be displayed on screen better

        divideBy2Flag = False;

        contrastCheckMin = min(averages);
        contrastCheckMax = max(averages);

        #if 0, changing checker variable to a non-zero small value
        if(contrastCheckMin == 0):
            contrastCheckMin = 0.01;

        contrastCheckDiv = contrastCheckMax / contrastCheckMin;

        if(contrastCheckDiv > 12):
            divideBy2Flag = True;
 
        #-------------------------------------------------------------------------------------------------------------------


        if(minimumValue == 0):

            #add all values in 'averages' list to 'averagesNext' 

            for averageVal in averagesIterable:

                averagesNext.append(averageVal);

        else:

            #take each value in averagesIterable (averages) and divide that each value using
            #the mimimum average value.
            #
            #collect these reduced-scale values to a list called argdiv.

            for averageVal in averagesIterable:

                avgdiv = averageVal / minimumValue;

                averagesNext.append(avgdiv);





        #here the 'decimal' package imported at the start of the file is used.

        #decimalContext is an object used in the process of rounding the float number (number with a decimal point)
        #into a integer number
        decimalContext = Context(prec=50, rounding=ROUND_HALF_EVEN); 


        print("\n\nOccurence of each dice value, 1 - 6 . (proportions are displayed below).\n");
        print("note: proportions are displayed, not actual average amount");
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n");

        for k in range( len(averagesNext) ):

            #note, nesting of functions used above -- range( len( )  )
            #meaning: cycle from number 0 to number 5


            #get a decimal type value from the divided floating-point number (use decimalContext to do it).
            decimalValue = decimalContext.create_decimal_from_float(averagesNext[k]); 
            #round the decimal value into a number without a decimal point.
            roundedDecimal = round(decimalValue,1);

            #increase the size of the value so that its suitable for display
            roundedDec10Times = roundedDecimal * 10;



            possiblyDividedValue = roundedDec10Times;

            #if max-min difference is too large, division by 2 is used to get in the end a shorter bar length.
            if(divideBy2Flag == True):
                possiblyDividedValue = possiblyDividedValue / 2;



            #turn the decimal value into an int / integer number.
            chartBarInteger = int(possiblyDividedValue);

            #set up the start of each bar string, which indicates the dice-roll number 
            strbar = "dice value ["+str(k+1) + "]\t:";
            #str( ) changes the int value into a string segment. \t tells to put a tab in the string.

            #draw each bar by using the int value relevant to each average. 
            for j in range(chartBarInteger):

                strbar = strbar + "=";

            strbar = strbar+"\n";

            #print the string line onto the screen.
            print(strbar);

        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n");



    #display roll set result
    #
    def displayRollSetResult(self):
        results = self.getResultList();

        print("---rolls result list---");

        for roll in results:
            print(str(roll)); 

        print("---end of list---");

        return;


    #display how method 1 calculated
    #
    def displayHowMethod1Calculated(self):

        print("\n");
        print("METHOD 1");
        print("");
        print("4 bits are used: 0/1 , 0/1 , 0/1 , 0/1");
        print("e.g. the bits can have values such as: 0 1 0 0, or 1 1 1 0, or 0 0 0 1, etc.");
        print("the value 1 or value 0, is randomly assigned by the computer program ( or can be decided by an action such as a coin toss)");
        print("");
        print("================================================================================");
        print("(see the value list given at the end)");
        print("");
        print("the first two bits are considered a binary-system number, & a decimal value is taken from that...");
        print("then add either 0, 1 or 2 depending on what values the last two addition bits get.");
        print("");
        print("lastly, add 1 to the value gotten from above (because otherwise you'd get;");
        print("values from 0 to 5)");
        print("");
        print("================================================================================");
        print("\n");
        print("the first two bits form a binary-number-system number");
        print("values can be : 0 0 , 0 1 , 1 0 , 1 1");
        print("");
        print("first bit : \t0 = decimal 0 ,   1 = decimal 1");
        print("second bit : \t0 = decimal 0 ,   1 = decimal 2");
        print("");
        print("so 0 0 = decimal 0 , 0 1 = decimal 1 , 1 0 = decimal 2, 1 1 = decimal 3 (add the decimal 1 and 2)");
        print("\n");
        print("the 3rd and 4th bits are decimal adding bits");
        print("if bit 3 = 0 then add nothing, if bit 3 = 1 then add decimal 1");
        print("if bit 4 = 0 then add nothing, if bit 4 = 1 then add decimal 1");
        print("\n");
        print("VALUE TABLE - this shows the way each dice value is arrived at");
        print("bin  add");
        print("--------------------------------------------");
        print("0 0  0 0 ---> (decimal-0) + 0 (additon bits) + 1 = decimal 1");
        print("0 1  0 0 ---> (decimal-1) + 0 (additon bits) + 1 = decimal 2");
        print("1 0  0 0 ---> (decimal-2) + 0 (additon bits) + 1 = decimal 3");
        print("1 1  0 0 ---> (decimal-3) + 0 (additon bits) + 1 = decimal 4");
        print("1 1  1 0 ---> (decimal-3) + 1 (additon bits) + 1 = decimal 5");
        print("1 1  1 1 ---> (decimal-3) + 2 (additon bits) + 1 = decimal 6"); 
        print("\n");




    #display how method 2 calculated
    #
    def displayHowMethod2Calculated(self):
        print("\n");
        print("METHOD 2");
        print("");
        print("three bits are used : 0/1 , 0/1 , 0/1"); 
        print("these three bits combine into a binary-number-system number :");
        print("for example , 001 or 101 or 110 or 100 etc");
        print("the value 1 or value 0, is randomly assigned by the computer program ( or can be decided by an action such as a coin toss)");
        print("");
        print("the 1st bit : \t0 = decimal 0 ,\t1 = decimal 1");
        print("the 2nd bit : \t0 = decimal 0 ,\t1 = decimal 2");
        print("the 3rd bit : \t0 = decimal 0 ,\t1 = decimal 4");
        print("\n");
        print("====================================================================");
        print("the program sets value 0 or value 1 to each of the 3  bits, randomly.");
        print("");
        print("So a random 3 bit binary number is generated, simply.");
        print("The three bits can represent decimal number values from 0 to 7.");
        print("");
        print("Since we want only values 1 - 6 , we have to discard any roll-");
        print("-where a  0 is generated, or where a 7 is generated.");
        print("");
        print("where 0 or 7 is met, the program rolls again (and again) until-");
        print("-a value in range 1 - 6 is generated.");
        print("====================================================================");
        print("\n");
        print("VALUE TABLE - this shows how each decimal number 1 - 6 is arrived at.\n");
        print("bit1    bit2    bit3        decimal value");
        print("--------------------------------------------------------------"); 
        print("0       0       0   ---->   0   -   -   -   (discard, roll again)");
        print("0       0       1   ---->   1   -   -   -   (accepted)");
        print("0       1       0   ---->   2   -   -   -   (accepted)");
        print("0       1       1   ---->   3   -   -   -   (accepted)");
        print("1       0       0   ---->   4   -   -   -   (accepted)");
        print("1       0       1   ---->   5   -   -   -   (accepted)");
        print("1       1       0   ---->   6   -   -   -   (accepted)");
        print("1       1       1   ---->   7   -   -   -   (discard, roll again)");
        print("\n");



    #get print roll
    #
    def getRollValuesStr(self):

        #returns a string of text that shows the random values that were assigned to the bit-variables
        #this line of text the function provides, is used elsewhere in the program.


        if(self.getMethod() == 1):

            #here a string of text is being made, making use of hard coded text and also values of variables

            return (" Binary-bit-1:["+str(self.getSP())+"] Binary-bit-2:["+
                    str(self.getFP())+"] Addition-bit-1:["+str(self.getA1())+"] Addition-bit-2:["+str(self.getA2())+"]");

        if(self.getMethod() == 2):

            return (" Binary-bit-1:["+ str(self.getBinaryThree()) +"] Binary-bit-2:["+ 
                    str(self.getBinaryTwo()) +"] Binary-bit-3:["+ str(self.getBinaryOne()) +"]");

    #=================================================================================================
        




    #CONTROL FUNCTIONS
    #===============================================

    #roll the dice
    #
    def rollTheDice(self):

        #get the randomly decided 0 or 1 values for each binary variable. 

        if(self.getMethod() == 1):

            #roll randomly the individual binaries
        
            # random.randint(0,1)  ---> this generates randomly a 0 or a 1.

            #setting to method 1 variables
            self.setFP(random.randint(0,1));
            self.setSP(random.randint(0,1));
            self.setA1(random.randint(0,1));
            self.setA2(random.randint(0,1));

            return;

        elif(self.getMethod() == 2):
            
            #setting to method 2 variables

            self.setBinaryOne(random.randint(0,1));
            self.setBinaryTwo(random.randint(0,1));
            self.setBinaryThree(random.randint(0,1));

            return;


    #CALCULATE DECIMAL VALUE
    #
    def calculateDecimalValue(self):

        #calcuate the dice-roll value from the binary variables,
        #the decimal value can be from number 1 - 6

        #method 1
        #
        if(self.getMethod() == 1):

            #first place 0 / 1 translates to decimal 0 / 1
            firstPlaceDecimal = self.getFP();

            #second place 1 ---> decimal 2
            secondPlaceDecimal = 0;
            if(self.getSP() == 1): 
                secondPlaceDecimal = 2;
           
            #adding digits combined
            addingDecimal = self.addOne + self.addTwo;

            #add the above values together, 
            #and add one to it( 1 - 6 , not 0 - 5 )
            return firstPlaceDecimal + secondPlaceDecimal + addingDecimal + 1;

        #method 2
        #
        elif(self.getMethod() == 2):

            #variable to hold the end value. 
            dec = 0;

            #bin1, bin2, bin3 can be 1 or 0

            #first place can be 0 or 1
            bin1 = self.getBinaryOne();
            if(bin1 == 1):
                dec = dec + 1;

            #second place can be 0 or 2
            bin2 = self.getBinaryTwo();
            if(bin2 == 1):
                dec = dec + 2;

            #third place can be 0 or 4
            bin3 = self.getBinaryThree();
            if(bin3 == 1):
                dec = dec + 4;

            return dec;

            

    #do single roll
    #
    def doSingleRoll(self):

        
        if(self.getMethod() == 1):

            #get the random values for the digits.
            self.rollTheDice();
            
            v1 = self.getRollValuesStr();       #string of text displaying the roll digit values 
            v2 = self.calculateDecimalValue();  #dice value that's calculated from random rolls

            self.printSingleRollResults(v1,v2); #print results to screen


        elif(self.getMethod() == 2):
 
            v1 = "";    #string of text displaying roll digit values
            v2 = 0;     #holds the dice value

            while(True):

                self.rollTheDice();
                
                v2 = self.calculateDecimalValue();


                #if a 0 or a 7 is calculated, roll again, for a value between 1 - 6

                if(v2 == 0 or v2 == 7):
                    continue;

                else:
                    break;


            v1 = self.getRollValuesStr();       
            self.printSingleRollResults(v1,v2); #print the values to screen

        return;



    #do roll set roll
    #
    def doSetRoll(self, amount):

        #set up an initial set variable
        self.initRollSetList(amount, self.getMethod());


        #check if method 1 chosen
        if(self.getMethod() == 1):

            for x in range(amount):
    
                #roll the dice
                self.rollTheDice();

                n1 = self.getSP(); 
                n2 = self.getFP();
                n3 = self.getA1();
                n4 = self.getA2();
                n5 = self.calculateDecimalValue();

                #get the dice values and store in rollResult
                rollResult = [n1,n2,n3,n4,n5];

                #set the 'rollResult' values at the 'x' index in 
                #the variable for holding set of rolls
                self.setListValue(x,rollResult);

            #displayRollSetResult : screen output of the list of rolls
            #I disabled this function, long sets and large number of sets-
            #large amount of terminal is used in long lists.
            #
            #self.displayRollSetResult();



        #check if method 2 chosen
        elif(self.getMethod() == 2):

            for x in range(amount):

                n1 = 2;
                n2 = 2;
                n3 = 2;
                n4 = 10;

                while(True):

                    self.rollTheDice();

                    n4 = self.calculateDecimalValue();
                   
                    #discard dice-roll value of 0 or 7
                    #repeat discarding until a non-0 non-7 value 
                    if(n4 == 0 or n4 == 7):
                        continue;
                    else:
                        break;


                #get the random roll values of the roll
                n1 = self.getBinaryThree();
                n2 = self.getBinaryTwo();
                n3 = self.getBinaryOne();


                rollResult = [n1,n2,n3,n4];

                #store the roll results at x index of the roll-set list
                self.setListValue(x,rollResult);


            #screen output of the dice rolls
            #I've disabled this function 
            #
            #self.displayRollSetResult();

        return;




    #multiple roll set test
    #
    def multipleRollSetTest(self,repeatsNumber,rollsetsNumber):

        #a further set of multiple roll-sets
        rollsetResultsCollection = [];

        #make the roll-sets according to given rollsetsNumber
        for x in range(rollsetsNumber):

            #do a new rollset...

            #occerence of each dice-value counted here.
            count1 = 0;
            count2 = 0;
            count3 = 0;
            count4 = 0;
            count5 = 0;
            count6 = 0;

            #do a set of dice rolls 
            self.doSetRoll(repeatsNumber);

            #get results of the roll
            rollResult = self.getResultList();

            #add the rolled dice-values to rollsetValuesList  
            self.rollsetValuesList.append(rollResult);


            valueIndex = 10;

            #the method 1 roll result and method 2 roll result lists are
            #different in length. the value is stored at the end index.
            if(self.getMethod() == 1):
                valueIndex = 4;
            elif(self.getMethod() == 2):
                valueIndex = 3;

            #counting checks are done on the dice-roll value of each roll result.
            #depending on the value, the relevant counter is incremented. 

            for s in range(len(rollResult)):

                if rollResult[s][valueIndex] == 1:
                    count1 += 1;
                elif rollResult[s][valueIndex] == 2:
                    count2 += 1;
                elif rollResult[s][valueIndex] == 3:
                    count3 += 1;
                elif rollResult[s][valueIndex] == 4:
                    count4 += 1;
                elif rollResult[s][valueIndex] == 5:
                    count5 += 1;
                elif rollResult[s][valueIndex] == 6:
                    count6 += 1;

            #the counters are collected into one list.
            #the count list is added to a further set of count lists. 
            rollStats = [count1,count2,count3,count4,count5,count6]
            
            rollsetResultsCollection.append(rollStats);

            
            self.clearResultList();



        #the data 'rollsets' is input into this function when its used.
        #
        #'rollsets' is a list of lists, and this is made at the end of the function which carries out       
        # multiple-set dice-rolls.
        #
        # after all dice rolls sets have been rolled, a process  goes through all the roll-results,
        # and for each set of rolls, counts up the number of times value 1 has come up, 2 has come up, 3, 4, 5, 6.
        # these occurence countings are put in a list, and count-list corresponds to dice-roll set. 
        #
        # (rollsets)
        # --------------------------------------------------------------------------------------------------------------
        # set 1 [ set 1 value (1) count, 1 value (2) count, value (3) count, value (4), value (5), value (6) ] 
        # set 2 [ set 2 value (1) count, 2 value (2) count, value (3) count, value (4), value (5), value (6) ] 
        # set 3 [ set 3 value (1) count, 3 value (2) count, value (3) count, value (4), value (5), value (6) ]  
        # set 4 [ set 4 value (1) count, 4 value (2) count, value (3) count, value (4), value (5), value (6) ]
        # --------------------------------------------------------------------------------------------------------------

        self.displayRollSetCollectionStats(rollsetResultsCollection);
        
        
        #File output
        #the roll results sets are recorded in table format, in a text file
        self.writeResultsToFile();


        self.clearRollSetValuesList();
        



    #file Input / Output functions
    #===============================================

    #if your text editor program has word-wrap enabled, the data will not be displayed in table format correctly.
    #in that case, you could disable word-wrap, which probably can be reached through the 'view' menu.
    #(should be able to re-enable wrapping again through that option too). 
    #note that this stops word-wrapping and gives you a horizontal scroll bar to view out-of-screen data

    #note, repeating use of multiple roll replaces data file with a new one.

    def writeResultsToFile(self):

        data = self.getValueLists();

        rollsNumber = len(data[0]);
        
        setsNumber = len(data);


        listCounter = 0;
        setCounter = 0;

        #this statement opens an object that can be used to create and write to a file
        #called 'program-DATA-FILE'. the 'w' option indicates the the file is opened for writing
        #and it is made blank at the point of opening

        #don't forget to call close() after the last string is written to the file!
        fileObject = open('program-DATA-FILE','w');


        #add a label at the top of the file indicating whether its method 1 or method 2
        methodString = "";
        if(self.getMethod() == 1):
            methodString = "-(Method 1 :- 2 bin bits, 2 add bits) - e.g. [1,1,0,0,4] : 4 is the resulting cube-dice value.\n";
        elif(self.getMethod() == 2):
            methodString = "-(Method 2 :- 3 bin bits, discard result 0 & 7) - e.g. [1,0,1,5] : 5 is the resulting cube-dice value.\n";

        printString = "";


        #the info detailing the stats of the data set. 
        headerString1 = " The Binary Dice - Random Roll Results\n\n" + methodString + "\n Number of roll-sets: ";
        headerString2 = str(setsNumber) + " , number of rolls in each set: " + str(rollsNumber)+"";
        headerString3 = "\n\n 1 Vertical Column = 1 complete roll-set.\n";
        headerString4 = "\nif the data is not in column format, you might have to configure 'word-wrap' in your notepad program.\n";
        headerString5 = "\n-----------------------------------------------------------------------------------------------------------------\n\n";

        #write the above strings to the top of the file.
        fileObject.write(headerString1 + headerString2 + headerString3 + headerString4 + headerString5); 

        
        for x in range(rollsNumber):

            #cycling through the number of rolls (same number of rolls in each set)

            for y in range(setsNumber):

                #cycling though the number of sets

                #each roll is added to the string that will be printed out.
                #escape character (\t) seperates the rolls from each other.

                #\n is a line break escape character

                printString = printString + "\t" + str(data[y][x]);

                #at the end of last set, the next roll-number.
                if (y == setsNumber-1):
                    printString = printString + "\n";
                    fileObject.write(printString);
                    printString = "";
        
        #indicate end of file
        fileObject.write("\n\n===(End)====================================================================================================\n");
        
        #!!! its important to call close() after open() was called previously.
        fileObject.close();

        print("DATA FILE REPLACED - check program directory\n\n");



    #=================================================================================================
    #
    #CONSTRUCTOR
    #
    #The constructor function is used when making a new instance/object from a 'class' template.
    # 
    #It sets the first values of the object's variables.
    #It can also do any other thing that needs to be done right at the point were the object is made.
    #
    #In this case, the constructor just sets some place-holder values to some of the variables
    #(these will be replaced soon as the dice is rolled).
    #
    #
    #SELF: 'self' is passed onto the function. it's a 'parameter' of this function(one of the variables within-
    #the function brackets)
    #
    #here 'self' refers to this very object that the function belongs to.
    #(in this instance the object is the 'diceObject' object that gets made at the end of the file.
    #
    #so self.firstPlace = 10 means: change the value of own (diceObject) 'firstPlace' variable's value to 10.
    #
    def __init__(self):


        #possibly it would have been better to use the syntax 'None' rather than putting actual number values
        #for placeholder.

        self.firstPlace = 10;
        self.secondPlace = 10;
        self.addOne = 10;
        self.addTwo = 10;

        self.binaryOne = 10;
        self.binaryTwo = 10;
        self.binaryThree = 10;


    #=================================================================================================



    #================================================================================================= 
    #
    #ENTITY : Functions for data storage and retrieval (to and from variables)
    #
    #Not much is done in these functions...they are used to store data in the variables, and
    #also to retrieve data from them.
    #Some setter functions check the value given to them with an if statement, before storing it in the variable.
    #Some functions clear the value of the variable and set it to blank.



    def getMethod(self):

        #get and provide the value stored in methodFlag variable 
        return self.methodFlag;


    def setMethod(self,num):

        #take the value (num) given, and store that value in methodFlag variable

        #but first check that the value given is in the correct set of values to be stored here.
        #if statement (used in making decisions in the program).
        if(num == 1 or num == 2):
            self.methodFlag = num;





    def setListValue(self, listPosition, rollResults):
        
        #take the roll given, and set it at the (also given) index position, in the resultList list
        #resultList is a defined variable of the class.

        self.resultList[listPosition] = rollResults;

    def getListValue(self,listPosition):
        return self.resultList[listPosition];

    def getResultList(self):
        return self.resultList;

    def clearResultList(self):
    
        #make the resultList variable value blank.
        self.resultList = [];





    def getValueLists(self):
        return self.rollsetValuesList;

    def clearRollSetValuesList(self):
        self.rollsetValuesList = [];



    def getFP(self):
        return self.firstPlace;
    
    def getSP(self):
        return self.secondPlace;

    def getA1(self):
        return self.addOne;

    def getA2(self):
        return self.addTwo;

 
    def setFP(self,number):

        if(number < 0 or number > 1):
            print("error! invalid arguement");

            return;

        self.firstPlace = number;


    def setSP(self,number):
          
        if(number < 0 or number > 1):
            print("error! invalid arguement");
            return;

        self.secondPlace = number;


    def setA1(self, number):
 
        if(number < 0 or number > 1):
            print("error! invalid arguement");
            return;

        self.addOne = number;


    def setA2(self,number):

        if(number < 0 or number > 1):
            print("error! invalid arguement");
            return;

        self.addTwo = number;




    def getBinaryOne(self):
        return self.binaryOne;

    def getBinaryTwo(self):
        return self.binaryTwo;

    def getBinaryThree(self):
        return self.binaryThree;

    def setBinaryOne(self,number):

        if(number < 0 or number > 1):
            print("error! invalid arguement");
            return;

        self.binaryOne = number;

    def setBinaryTwo(self,number):
 
        if(number < 0 or number > 1):
            print("error! invalid arguement");
            return;

        self.binaryTwo = number;

    def setBinaryThree(self,number):

        if(number < 0 or number > 1):
            print("error! invalid arguement");
            return;

        self.binaryThree = number;





    def initRollSetList(self,repeatsNumber,method):
        
        #add a set of lists with initial values (to be replaced when actual rolls are done).

        row = [];

        if(method == 1):
            row = [10,10,10,10,10];

        elif(method == 2):
            row = [10,10,10,10]; 


        #example of a WHILE LOOP
        #
        #just add the initial list (row), n (repeatsNumber) number of times, to the 'resultList' variable
        #
        #below a 'while loop' is used. while counter is larger than 0, the initial (row) is repeatedly
        #attached to resultList. Counter is reduced by 1 after each attachment. So after repeatsNumber 
        #number of times of attaching the (row), the loop ends.
        
        counter = repeatsNumber;

        while(counter > 0):

            self.resultList.append(row);

            counter = counter - 1;

    #================================================================================================= 




#AN OBJECT OF THE MAIN CLASS OF THIS PROGRAM IS MADE BELOW.
#THE DISPLAY-MAIN-MENU FUNCTION OF THAT OBJECT IS THEN CALLED.

diceObject = BinaryDice();
diceObject.displayMainMenu();

