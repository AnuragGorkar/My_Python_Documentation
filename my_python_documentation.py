#***   MY PYTHON TUTORIALS NOTES  ***#
    # INTRODCTION TO PYTHON 
    # WHY PYTHON ?
        # 1)ENHANCED READABILITY
        #   In Python, uniform indents are used to delimit blocks of statements instead of curly brackets like in C, C++, and Java. This enhances readability.

        #         IN  C, C++, Java
        #             if (X%2==0)
        #             {
        #         if (x%3==0)
        #         System.out.println("divisible by 2 and 3");
        #         else
        #         System.out.println("divisible by 2 not divisible by 3");
        #         }
        #         else
        #         {
        #         if (x%3==0)
        #         System.out.println("divisible by 3 not divisible by 2");
        #         else
        #         System.out.println("not divisible by 3 nor by 2");
        #         }
                
        #         IN Python
        #         if num%2 == 0:
        #         if num%3 == 0:
        #             print ("Divisible by 3 and 2")
        #         else:
        #             print ("Divisible by 2 not divisible by 3")
        #         else:
        #             if num%3 == 0:
        #                 print ("Divisible by 3 not divisible by 2")
        #         else:
        #              print ("Not divisible by 3 nor by 2")
        
        
        # 2)DYNAMIC TYPING
        #   In Python, a variable to be used in a program need not have prior declaration of its name and type. You will learn details about variables in the next module.

        #       Java is statically typed
        #       String var;  // Variable is explicitly declared.
        #       var=”Hello”;
        #       var=1234; // Not allowed because the variable has been declared as a String.
               
        #       Python is dynamically typed
        #       var=”Hello” # Variable is NOT explicitly declared.
        #       var=1234 # Allowed although variable was initially String type


        # 3)INTERPRETED LANGUAGE
        #   Python is an interpreter-based language. An interpreter executes one instruction at a time. So if there is an error on line 7 of the code, it will execute instructions till line 6 and then stop. This is unlike a compiler which will not execute any of the instructions even if there is a single error. Thus, an interpreter is useful if you are new to programming because it allows you to see partial output of your code and identify the error location more easily.


        #       Java program  (Compiled)
        #       This program will not display any of the phrases as there is an error on line 7.
        
        #       1 public class test
        #       2 {
        #       3   public static void main(String args[])
        #       4   {
        #       5     System.out.println("Welcome to");
        #       6     System.out.println("Python training program");
        #       7     System.out.println(From Internshala);
        #       8   }
        #       9 }
        #       
        #       Python program (Interpreted)
        #       This program will display two phrases but not the third phrase as there is an error in line 3.
        
        #       print ("welcome to")
        #       print ("Python training program from")
        #       print (Internshala)  


        # 4)EXTENSIBLE LANGUAGE 
        #   Python extension modules implement new built-in object types and can call C libraries and system calls which Python doesn’t have direct access to.
        #   Python can be extended to work with other languages like C,C++ and Java. 



        # 5)STANDARD DB2 API
        # A standard data connectivity API facilitates using data sources such as Oracle, MySQL, and SQLite as a backend to a Python program for storage, retrieval, and processing of data. 
        # Standard DB2 API is a common interface provider to all the databases. Examples: Oracle, MySQL, DB2, etc.


        # 6)GUI PROGRAMMING
        # GUI programming is nothing but creating buttons, text boxes, other user interactable elements and attaching function to the events like button click, key press. 
        # The standard distribution of Python contains a Tkinter GUI kit, which is an implementation of the popular GUI library called Tcl/Tk. 
        # An attractive GUI can be constructed using Tkinter. Many other GUI libraries like Qt, GTK, WxWidgets, etc. are also ported to Python. 


        # 7)EMBEDDABLE
        # Python can be integrated with other popular programming technologies such as C, C++, Java, ActiveX, and CORBA.
        # Python provides libraries to embed Python code in other languages like Django can be used to embed python code in HTML etc.


# EXECUTE THE FOLLOWING CODE TO OUTPUT THE ZEN OF PYTHON BY TIM PETERS :  
# import this
    
    
    
    
    
    # CHAPTER 0
    #COMMAND LINE TUTORIALS\\***
# pwd : print_working_directory : it is used to print the current location of the command line.
# ls : list : it lists all the folders and files in a direcory 
# cd : change directory : to open a new file or a folder
# cd drive_name// : will move in another drive 
# clear : it is used to clear the command line screen
# mkdir : make directory :to create a new folder
# mkdir "folder name" : this command includes spaces in the folder name 
# mkdir folder name : this command makes two different folders file and name , so here we have to use _ notation
# touch : it is used to make new files
# echo -e "This is the content of the file. \n This is charachter escape sequence" >> file_name.txt : This is used to write contents to the file.
# cd .. : cahnge directory back : it takes the command line to the previous file/ folder
# rm : remove : it is used to delete  any file 
# rm *.txt : it is used to delete all the .txt files in the current folder.
# rm -rf : remove -recursive force : this command is used to delete an entire folder
# code : it is used to open any file to code in visual studio code. if a file doesnot exist then vs code will create a new file and open it to code
# mv : move : it is used to move a file as well as to rename a new file 
# mv "file name 1" file_name_1 : it is used to rename the file "file name 1" to file_name_1
# mv "file name" path of the new location : it is used to move the file to a new location(folder)
# mv "file name" .. : it is used to move the file to the previous location 
# cp : copy :it is used ti copy the file to a new location.
    
    # PYTHON DEBUGGER 
# Python provides an inbuilt debugger class.
# Just import pdb in the programme.
# Write pdb.set_trace() before the line at which you want to start debugging
# In Terminal while executing give commands : 
# l : is used to show all the lines in the code and an arrow is used to indicate the current line being executed.
# n : is used to execute the current line.
# c : is used to execute the code normally ie. all at once (not line by line)
# q : is used to quit debugger

    # MUTABLE AND IMMUTABLE DATA TYPES
# The property of whether or not data objects can be modified in the same memory location where they are stored is called mutability.
# To check for mutability just check whether the location of the data in memory is same before and after changing its value.
# use the id() function to check memory location
# a = 10 
# print(id(a))
# a = 2
# print(id(a)) # changed therefore numeric data type is immutable.
# Immutable: numeric, string, and tuple
# Mutable: list, dictionary


    
    
    
    # CHAPTER 1
    # MATHEMATICAL OPERATIONS
# print(round(2/3,10))
# print(4%-3)
# print(3**2,3\\2) #  ** is used to print powers and \\ is used to print integer division.   
    # TYPE FUNCTION 
# type(variable_name) # returns the type of variable - variable_name
    # PRINTING AN EMOJI
# print( " \U0001F92E " )
    
    
    
    
    
    # CHAPTER 2
    # OPEARTIONS ON STRINGS\\***
# name="anurag"
# print(name)
# no = 123
# name=name +"no"
# name+=str(no)# operator compiling 
# print(name)
# print(str(9.2930)+ str(name))
# j = int(input("what is your age ?")) #in order to obtain the input in int form
# j=j+4
# print(j)
# print ("your age after four years is "+ str(j))
    # NEW STRING INPUT METHODS \\***
# name1, age, gender=input(ENTER YOUR NAME AND AGE and GENDER).split()#use spaces to separate 
# name2 ,age2,gender2=input("ENTER YOUR NAME ,AGE AND GENDER(commas to separate inputs)").split(",")
# print("YOUR NAME IS " + name2+".\t"+"YOUR AGE IS "+age2+".\t""YOUR GENDER IS "+gender2+".\t")
    # NEW STRING FORMATTING METHODS\\***
# print(f"YOUR NAME IS {name2} AND YOUR AGE IS {age2}")# never froget the "f" #need not worry about the data type
    # EXERSICE\\***
# NO_1,NO_2,NO_3=input("ENTER ANY THREE NUMBERS ").split(",")
# print(f"THE AVERAGE OF THE THREE NUMBERS IS {(int(NO_1)+int(NO_2)+int(NO_3))/3}")#donot forget the int() to convert to int form from string
    # INDEXING OF THE STRING
# string="Avani_Gorkar"
# the index values of the characters is :
# A=0,-5
# v=1,-4
# a=2,-3
# n=3,-2
# i=4,-1
# print(string[3],string[-2])
    # STRING SLICING/STEPPING \\***
# print(string[2:10])# syntax::[start argument:end argment -1]#[:]prints whole string
# print(string[2:10:2])# syntax::[start argument:end argment -1:step argument] # to print reverse use negative step
#how does it even print the reverse of the string when I give input (string[::-1])
    # STRING FUNCTIONS / METHODS \\***
# name="     AvaNi  b"
# print(len("anurag")) #len() function prints length of the string 
# print(name.lower()) #lower() method pirnts all the characters in lower case
# print(name.upper()) #upper() method pirnts all the characters in upper case
# print(name.title()) #title() method pirnts all the starting character in upper case even after space.
# print(name.count("a")) #count() method counts the appearance of the character ""
    # EXERSICE\\**
# name,C=input("ENTER ANY STRING AND CHARACTER (comma separated)").split(",")
# print(f"THE CHARACTER {C} APPEARS {name.lower().count(C.lower())} TIMES IN YOUR STRING")
    # REPLACE METHOD AND FIND METHOD \\***
# name.replace("c1","c2","n") #removes c1 by c2 , for first n times  in the character /string 
    #IMP::strings in python are immutable thus they cannot be changed ,the replace method changes the characters of the string in another copy of the string ,reprinting the string after replace method will only print original string.however we can alter the string as a variable .
# name.find("c",loc.)#returns the location of the character c ,starts searching from location loc.in the string
    # STRIP METHOD \\***
# name.strip() # removes the spaces before and after the input character/string
# name.lstrip() #removes the spaces before the  character/string 
# name.rstrip() #removes the spaces after the  character/string
# name.replace(" ","") #removes the sapces in the character /string
# print (name.replace(" ",""))
    # CENTER METHOD \\***
#name.center("len(name)+N","*")#adds N no. of stars before and after the name string 
    
    
    
   
   
    # CHAPTER 3
    # CONDITIONAL STATEMENTS \\***
    # IF-ELSE STATEMENTS\\***
# if condition:
    #operatoins #here the ":" is imp. syntax ,also all operations in if block should always be written with tab indentation.
# else:
    #operatons
# elif:
    #operations #elseif statement
    # if-else operations
# pass statement can be used in palce of operations to exit the if block
# if condition1 and conditoin2 :"and' is the syntax to implement AND operator
# if 1>2 and 2<3: # condition is false
# if condition1 or conditoin2 :"or" is the syntax to implement OR operator
# if 2>1 or 3>2: # condition is true 
# if "character" in "string" :"in" is the keyword which checks whether the character is present in the string.
# if 'a' in "Anurag":
# if string: # returns 1 if string is not empty 
# if "Anurag":
    # WHILE LOOP \\**
# i=0
# while i<5:
#     print("ANURAG")
#     i+=1
# while True: # this is the syntax for an infinite loop
    # EXERSICE\\**
#  The following is a programme to count the appearance of all chatacters in a string
# name=input(print("ENTER ANY STRING AS INPUT"))
# temp=""
# i=0
# while i<len(name.lstrip()):
#     if name[i] not in temp:
#         temp=temp+name[i]
#         print(f"{name[i]}:{name.count(name[i])}")
#     i=i+1
    # FOR LOOP \\***
# for i in range (starting argument ,ending argument) ::#the value of i goes from strartnig argument to (ending argument-1)#if we donot specify any starting argument it starts from 0 by default
# for i in range (starting argument ,ending argumet, stepping argument) ::#stepping argument specifies the change in the value of i
# python provides another simple syntax of writing any for loop
# to print all the characters of a string   
# for i in "Anurag":
#     print(i)
# OR
# total =0
# for i in "123456":
#     total += int(i)
# print (f"{total}")
    # BREAK AND CONTINUE KEYWORD
#break keyword is used to exit any loop at any point  in the loop
#continue keyword is used to terminate any single iteration of the loop and continue with th next
    #RANDOME METHOD
# random.randint(1,100) # is used to generate any random no. between 1 and 100.
    
    
    
    
    
    #CHAPTER 4
    #FUNCTOINS \\***
    # DOC STRINGS 
# While writing any function it is good to provide info about what the function does. it can be done as:
# def func_name ():
#   ''' This is what the function does '''
# To view the doc of any function simply write : print(func_name.__doc__)
    # HELP FUNCTION
# For help in using any function write.
# print(help(func_name))
# def function_name(arguments) list...)# here def is the key word used , for documentation of the function we can use triple double quotes"""
# help(function_name) # returns the documentation line provided in the code
# return key word is used to return the value of the function
    #IMP:: python is a dynamic language which can accept any type of input as parameter to the function
# def dyn_fun(a,b):
#     print(a+b)
# dyn_fun(int(2),int(3))
# dyn_fun("2","3") # same function can take integer as well as string as input
# #    IMP :: a very pythoninc way of writing a function in order to check whether a number is odd or even is as ;
# def odd_even(num):
#     return  num%2==0 #this function returns True if the input no. is even and false when odd
# n = int(input("ENTER ANY NUMBER"))
# print (odd_even(n))
    #IMP default arguments ::the default arguments must always be last in the arguments list
    #IMP scope of variables
# x=12
# def func():
#     global x #even within function we can change the value of global variable using global keyword  
#     return x
# print(func())
# print(x)
    
    
    
    
    
    # CHAPTER 5
    # LISTS \\***
# list_name=[1,2,3,"anurag","avani"] # the elements of a list may not have a single data type . the list has same data indexing and slicing methods as that of strings.
# list_anu=[1,2,3,"archana"]
# print ( list_anu )
# print (list_anu[3])
# print (list_anu[:2])
# list_anu[1]="two" #replacing an element of the string of a list 
# print(list_anu)
    # METHODS IN LISTS
    # APPEND METHODS
# list_anu.append("gorkar") # append method adds an element in the list at the and
# print ( list_anu )
    # INSERT METHOD IN LISTS
# list_anu.insert(2,"apple") # inserts an element at the second position in the list 
# print(list_anu)
    # CONCATINATE LISTS 
# list_old= ["new element"]
# list_new= list_anu+list_old # it is used to create a new list by combining two lists 
# print(list_new)
    # EXTENDIG OF LISTS 
# list_anu.extend(list_old) # extend is used to attatch a list at the list at the end at the end of another without creating any new one
# print(list_anu) 
    # DELETION OF ELEMENTS IN THE LIST
    # POP METHOD 
# list_anu.pop() # using without any argument causes deletion of the last element of the list 
# list_anu.pop(1) # deletes the first element of the  list
# print(list_anu) 
# print(list_anu.pop(1)) # pop method  can also be used to return the popped values
# print(list_anu)  
    # DELETE METHOD 
# list_anu.delete(2) # deletes the second element of the list (similar to pop method)
# print(list_anu)
    # REMOVE METHOD
# list_anu.remove(3) # this method is used to remove an element from the list without specifying its no. # if an element occurs twice in the list then it removes the first appearance of the element.
# print(list_anu)
    # TO CHECK IF AN ELEMENT IS PRESENT IN A LIST :
# if "archana" in list_anu:
    # COUNT METHOD 
# list_anu.count("archana") # counts the appearance of any element in the list 
# print(list_anu)
    # SORT METHOD
# list_anu.sort() # sorts the elements in the list in alphabetical or numerical order 
# print(list_anu)
    # SORTED FUNCTION 
# print(sorted(list_anu)) # this function only prints the list in sorted order but doesn't  change the orginal list
# print(list_anu)
    # COMPARISON BETWEEN LISTS
# "==" operator compares the  elements of the list 
# is keyword checks whether the two lists appear in the same memory location
    # CONVERTING STRINGS TO LIST AND VICE-VERSA
    # SPLIT METHOD
# string2="anurag gorkar dilip".split() # this converts the string in a list by separating the elements in list by spaces
# string2="anurag , gorkar, dilip".split(",") # this converts the string in a list by separating the elements in list by commas
# print(string2)
    # JOIN METHOD
# list2=["anurag","dilip","gorkar"] # this converts the list in a string  by combining the elements separated by a comma.
# print(','.join(list2))
    # MIN AND MAX FUNCTIONS
# min(list_name) # returns the smallest number in the list- list_name
# max(list_name) # returns the largest number in the list- list_name
    # LOOPING IN STRINGS 
# matrix = [ [1,2,3], [4,5,6],[7,8,9] ]
# for i in matrix :
#     for j in i:
#         print(j)
    # GENERATING LIST WITH RANGE FUNCTION
# numbers = list(range (1,11)) # it will create a list from numbers 1 to 10
    # INDEX METHOD 
# list_name.index(list_member) # it is used to return the  least index of the  given no.
# list_name.index(list_member,start_argument,stop_argument) # it is used to specify from which position in the string to star and stop searching
    # PASSING LIST AS ARGUMENT TO A FUNCTION
    #  EXERSICE \\***
#  following is a programme to print the square of the numbers in the list 
# n =  int(input ("ENTER THE LAST INTEGER IN THE LIST "))
# numbers = list(range(1,n+1))
# def func(l):
#     square =[]
#     for i in l:
#         square.append(i**2)
#     return (square)
# print(func(numbers))
    #  EXERSICE \\***
# following is a programme to print the reverse of the numbers in the list 
# n =  int(input ("ENTER THE LAST INTEGER IN THE LIST "))
# numbers = list(range(1,n+1))
# print(numbers)
# def func(l):
#     rev =[]
#     for i in range(0,len(l)):
#         rev.append(l.pop())
#     return(rev)
# print(f'THE REVERSE OF THE STRING IS {func(numbers)}')





    # CHAPTER 6
    # TUPLE \\***
# A tuple is a collection of related data similar to a list but it cannot be changed or updated (i.e tuples are immutable)
# tuple_name = (member1,member2) # note here the members are enclosed in ()
# tuple_name = (only_member,) # note here that the syntax for a single membered tuple includes a comma after the first element otherwise it is treated as a single data element and is not a tuple
    # TUPLE WITHOUT PARANTHESIS
# tuple_name = member1, member2 
    # TUPLE UNPACKING
# data1,data2 = (tuple_name) # this assigns value member1 to data1 and member2 to data2 respectively # The no. of data items must be same as the no. of members of the tuple, less will give error and more will assogn no value.
# tuple_name = (member1, member2,[anurag,123,avani]) # lists can be tuple members and can be altered using methods and functions.
# name = tuple(range(1,11)) # it makes a tuple from 1 to 10
# print (name)
    # RETURNNG MORE THAN ONE VALUES BY A FUNCTION
##  IMP :: Whenever a function is to return two values then it returns them in the form of a tuple. those values can be unpacked.
    # EXAMPLE
# def func(int1,int2):
#     add = int1+int2
#     mul =int1*int2
#     return add, mul
# ad , ml = (func(2,3))
# print(ad, ml)
    # TUPLE TO STRINGS/LIST CONVERSION
# name = list(name) # convert tuple to list 
# print (name)
# name = str(name) # convert tuple to string
# print (name)





    # CHAPTER 7 
    # DICTIONARIES \\ ***
# A dictionary is a data structure in which data can be stored in a more complex manner. It can be used to represent real world data .There is no indexing in dictionary .
    # DEFINING A DICTIONARY 
# dictionary_name = {'key' : 'value/s','key1' : 'value/s" } # key provides information about the type of the data which can have many values.
# dictionary_name = dict( key = 'value') # note that here keyword used is dict and he key is not inside ''.
## IMP :: If a dictionary has same key repeated then it will take the last defined value and overwrite all previous values. This can be used in word counting algorithms.  
    # ACCESSING DATA IN DICTIONARY
# user = dict(name='Anurag', age=18 , gender ='Male')
# print(type(user))
# print(user['name'])
# print(user['age'])
    # DICITONARY/LIST  WITHIN DICTIONAY
# user1 = dict(name='Anurag', age=18, gender ='Male',fav_movies=['The Prestige','Inception','COCO'] ) 
# print (user1)
# users = dict(
# user1 = dict(name='Anurag', age=18, gender ='Male', fav_movies=['The Preatige','Inception','COCO'])
#   user2 = dict(name='Avani', age=8, gender ='Female', fav_movies=['Chota Bheem','Frozen','COCO']),
# )
# print (users)
    # ADDING DATA TO DICTIONARY 
# users['user3'] = dict(name='Archana', age=48, gender ='Female', fav_movies=['Mumbai-Pune-Mumbai','Andhaadhun','MAherchi Saadi'])
# print(users)
    # UPDATE METHOD 
# update_dict = dict(name ="Andu",fav_sports=['Circket', 'Vollyball', 'Badminton'])
# update_dict2 = dict(name='Anurag Gorkar') # on updating this Dictionsry to user1 any common keys value is overwritten and a new keys value is added. If we simply add a new name then the  new name gets added to the list of names.
# user1.update(update_dict)
# user1.update() # nothing is added to the Dictioary and the dictionary is unaltered 
# print(user1)
    # POPPING ITEMS FROM A LIST 
    # POP METHOD
    # IMP :: Never forget '' while popping any item 
# popped_item = user1.pop('name')
# print(f"POPPED ITEM IS {popped_item}. TYPE OF POPPED ITEM IS {type(popped_item)}")
# print(user1)
# popped_item1 = users.pop('user1')
# print(f"POPPED ITEM IS {popped_item1}. TYPE OF POPPED ITEM IS {type(popped_item1)}")
# print(users)
    # POPITEM METHOD
# popped_item = user1.popitem() # No argument is given in popitem
# print (f"POPPED ITEM IS {popped_item}") # popitem pops the last item in the Dictionary
    # LOOPING AND in KEYWORD IN DICTIONARIES
# Check whether key is present in Dictionary
# if 'user1' in users:
#     print("PRESENT")
# else:
#     print("ABSENT")
    # METHODS IN DICTIONARY
    # VALUES METHOD
 # Check if value is present in Dictionary 
# if 'Anurag' in  user1.values():
#     print("PRESENT")
# else :
#     print("ABSENT")
 # Print the Dictionary using looping
# for i in user1:
#     print(i) # prints keys
#     print(user1[i]) # prints values
# for i in user1.values(): # print values only using values method
# print(i)
# user1_values = user1.values()
# print (type(user1_values)) # it prints all values of the Dictionary in type dict_values. This type is not a list as it cannot be altered
    # KEYS METHOD
# user1_keys = user1.keys()
# print (user1_keys) # it prints all keys of the Dictionary in type dict_keys. This type is not a list as it cannot be altered
    # ITEMS METHOD 
# This is an important method to return the values of a Dictionary.
# user_items = user1.items()
# print(user_items)  # it prints the key and value collection in list of tuples with type dict_items
 # items method can be used to represent the keys and values of a Dictionary using for loop
# for i,j in user1.items():
#     print(f"{i} :: {j}")
# for i,j in users.items():
#     print(f"{i} :: {j}") 
    # FROM KEYS 
# from keys are used when different keys have to be assigned same values
# dict_name = dict.fromkeys(('name','age','weight'),'common_value')
# dict_name = dict.fromkeys(('abc',),'common_value') # IMP giving comma will treat abc as a single key but by not giving comma the values are assigned to a,b, and c separately. 
# dict_name = dict.fromkeys((range(1,11)),'common_value') # Such definition creates keys from 1 to 10.
# print(dict_name)
    # GET METHOD
# When we extract any single value by using keys normally then on giving invalid key-name compiler files an error.
# print(user1.get('name')) # get method outputs None value for invalid key name . It can also be used to check conditions.
# print (user1.get('name', NOT FOUND))  # this returns not found instead of None if key is invalid.  
    # CLEAR METHOD 
# dict_name.clear() # This method clears all values of the Dictionary to make empty dictionary. 
    # COPY METHOD
# dict_new = dict_old.copy() # copies the old dictionary to the new dictionary.These are different Dictionaries.
# dict_old = dict()
# dict_new = dict_old # dict_new and dict_old are the same Dictionary with different names . Any changes made in one are carried forward to the other Dictionary.
## IMP :: "is" checks whether two values are same ie. they occupy the same space in memory, while "==" only compares their values even if they are the same entity with the same name.
# print(dict_new is dict_old)




    # CHAPTER 8
    # SETS \\ ***
# A set is also an unordered collection of data which only stores one value once discarding all the other values.
# However we cannot have lists or dictionaries as members of a list.Indexing of set is not. 
# The main use of a set isi to remove dupicate data from lists 
# set_name = {1,2,3,3,4,5,5}
# print(set_name)
    # SET METHODS 
# set_name.clear() # clears all data from a set 
# set_name.add(argument) # adds data from a set 
# set_name.remove(argument) # removes data from a set  # But removing data not present in the set flags an error.
# set_name.discard() # removes data from a set # But doesnot flag error whwn argument provided is not in set.
    # CONVERTING LIST TO SET 
# set_new = set(listname)
    # in KEYWORD IN SET
# if 1 in set_name:
#     print("PRESENT")
# else:
#     print("ABSENT")
#     # LOOPING IN SET
# for set_member in set_name:
#     print(set_member) 
    # OPERATINS ON SETS
    # SET UNION
# s1 ={1,2,3,3,4}
# s2 ={3,3,4,5,6}
# s3 = s1 | s2 
# print(s3)
    # SET INTERSECTION
# s3 = s1 & s2
# print(s3)

    
    
    
    
    # CHAPTER 9 
    # LIST COMPREHENSION  \\***
    # FOR LOOP
    #  EXERSICE 1 \\***
# The following is a normal programme to obtain the first characters of strings in the list.
# names = ['Anurag', 'Archana', 'Avani', 'Dilip']
# initials = []
# for i in names:
#     initials.append(i[0])
# print(initials)
# The following is the same programme written using list comprehension
# initials = [i[0] for i in names]
# print(initials)
    #  EXERSICE 2 \\***
# The following is a programme to reverse all the strings in a list by normal methods.
# list = [ 'abc', 'def', 'ghi', 'jkl']
# rev_list=[]
# for string in list:
#     rev_list.append(string[::-1])
# print(rev_list)
# The following is the same programme using comprehension
# rev_list=[string[::-1] for string in list ]
# print(rev_list)
    # IF CONDITION
    #  EXERSICE 3 \\***
# The following is a programme to obtain even numbers from a list of numbers
# num_list = list(range(1 , 11))
# even_num = []
# for num in num_list:
#     if num%2==0:
#         even_num.append(num)
# print(even_num)
# The following is the same programme written using list comprehension
# even_num=[num for num in num_list if num%2==0]
# print(even_num)
    #  EXERSICE 4 \\***
# The follwing is a programme to seperate all data types elements of a list using list comprehension
# mixed_list = [True, False, "String1", "String2", 1,10,3 ] 
# num_list = [i for i in mixed_list if type(i)==int]
# bool_list = [i for i in mixed_list if type(i)==bool]
# string_list = [i for i in mixed_list if type(i)==str]
# print(num_list)
# print(bool_list)
# print(string_list)
    # IF ELSE CONDITION
## IMP :: While using if else in list comprehension write if and else conditions before for loop.
    #  EXERSICE 5 \\***
# The follwing is a programme to multiply even numbers by two and negate all odd numbers using list comprehension
# new_list = [i*2 if i%2==0 else -i for i in range(1,12)] 
# print(new_list)
    # NESTED LIST
# The following is a programme to obtain a list of three identical lists using list comprehension
# nested_list = [[i for i in range(1,6)] for i in range(3)]
# print(nested_list)
    # DICTIONARY COMPREHENSION \\**
    #  EXERSICE 1 \\***
# The following is a programme in-order to create a dictionary of numbers and their squares.
# squares = { num : num**2 for num in range(1,11)}
# for k,v in squares.items():
#     print(f" SQUARE OF {k} IS : {v}")
    # IF ELSE CONDITION
    #  EXERSICE 2 \\***
# The following is a programme to create a dictionary of odd and even numbers upto ten
# odd_even_dict = {f"THE NUMBER {i} IS ":('ODD' if i%2!=0 else 'EVEN') for i in range(1,11)}
# for k,v in odd_even_dict.items():
#     print(f"{k} {v}")
    # SET COMPREHENSION
    #  EXERSICE 1 \\***
# The following is a programme to reverse all the strings in a list by normal methods.
# set = { 'abc', 'def', 'ghi', 'jkl'}
# rev_set={string[::-1] for string in list }
# print(rev_list) # However the order might not remain same.





    # CHAPTER 10 
    # *args \\***
## IMP :: Normally a function takes only a fixed number of values as arguments but by using * operator we can take as many input parameters.
# Note that args is not a key word but is a mere convention . * operator passes arguments in the form of a tuple.
# def func_name(*args):
#     sum = 0
#     for i in args:
#         sum+=i
#     return sum
# print(func_name(1,2,3,4,5))
    # args WITH NORMAL PARAMETERS 
# Note that we can also define normal arguments with *agrs . However they must always be present before the *arguments as *arguments will contain all the values passed.
# def func_name(normal_arg,*args):
#     sum = 0
#     for i in args:
#         sum+=i
#     print(normal_arg)
#     return sum
# print(func_name(1,2,3,4,5)) # Here 1 will be taken as a normal argument. Which is mandatory to be given *may be empty.
    # USING LIST,SETS AS ARGUMENTS
# def func_name(*args): # Define the function with *args 
# func_name(*list/dict/set_name) # The problem with passing the lists as arguments is that the tuple contains the whole list as a single element . Thus to unpack the elements of the list we use * operator while calling the function.
    # EXERSICE \\*** # EXPLAIN SCOPE
# nums =[1,2,3,4,5,6]
# pows = []
# def power (normal_arg, *args):
#     pows = [i**normal_arg for i in args]
#     print (pows)
# power(2,*nums)
# print (pows)
   
    # **kwargs (keyword arguments)
# key word arguments can be used to accept dictionaries as parameter to a function.
# user = dict (name="Anurag", age="18", height="176")
# def func (**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k} : {v}")
# func(**user) # while passing dictionary as an argument to a function use ** operator for dictionary unpacking
    # PADK (normal parameters, arguments, default parameters, keyword arguments)
# This is the sequence in which the arguments must be specified while defining any function .
    # EXERSICE \\***
# names = ['anurag', 'dilip', 'archana', 'archana']
# def func(list_ip, *args):
#     if args:
#     new_names = [i[::-1] for i in list_ip]
#     new_names1 =  []

    
 
    

    # CHAPTER 11.0
    # LAMBDA EXPRESSION \\***
# lambda a,b : a+b # This syntax defines an anonymous function with no name.
# add = lambda a,b : a+b # Here the value has been assigned to a variable.  
    # EXAMPLE 1
# is_even = lambda a : a%2==0 # returns True if a is even and False if a is odd. 
# print(is_even(8))
    # EXAMPLE 1
# lent = lambda s : True if len(s) > 5 else False
# print(lent)           
# print(lent('Anurag'))





    # CAHPTER 11.1
    # BUILT IN FUNCTIONS IN PYHTON \\***
    # ENUMERATE FUNCTION \\***
# This function is used to track the position of any counter or ay increment in a loop.
# A normal function:
# pos = 0
# list = [ "Anurag","Archana", "Dilip", "Avani" ]
# for i in list :
#     print (f"{i} ----> {pos}")
#     pos +=1
# Same function using Enumerate function
# for pos , i in enumerate(list):
#     print(f"{i} ----> {pos}")
# The following s a function to return the position of a string in a list using enumerate function.
# def find(string):
#     for position, names in enumerate(list):
#         if names == string:
#             return position
#     return "NOT FOUND"
# print(find("Archana"))
    # MAP FUNCTION \\***
# The following is a simple function to find the squares of all numbers in a list using different methods.
# numbers = [1,2,3,4,5,6,7,8,9,10]
# 1) Normal Method
# squares= []
# def square (a):
    # for i in a:
#         squares.append(i**2)
#     print(squares)
# square(numbers)
# 2) List Comprehension
# squares = [i**2 for i in numbers]
# print(squares)
# 3) Map Function
# def square (a):
#      return a**2
# print(type(map(square,numbers))) # creates an object of class map
# print(map(square,numbers))
# squares = list (type(map(square,numbers))) # syntax to obtain object in form of a list
# 4) Map Function and Lambda Expression
# squares = list (map(lambda a: a**2,numbers))
# print (squares)
    # FILTER FUNCTION \\***
# filter function is a function which returns a bool type variable.
# syntax similar to map function.
    # ITERATOR AND ITERABLES
# iter() is a function which is used to convert a normal list/tuple/string into an iterable type. This same happens when a for loop works.
# During the functioning of a for loop first an iterable is created and then the next function is called which assigns the next value in the list to the variable.
# for i in list:  # WORKS AS THE FOLLOWING
# iterable_list = iter(list) # convert list to an iterable such that it can be used as an argument for next function.
# next(iterable_list) # 
    # ZIP FUNCTION
# user_id =["user1","user2","user3"]
# user_name = ["Anurag","Avani","Dilip"]
# collection = zip(user_id, user_name) # zip function returns a zip object by combining two or more lists.
# print(list(collection))
# print(dict(collection)) #  we can only convert a tuple having two items into a dictionary.
    #  LIST UNPACKING * operator with ZIP function by unpacking 
# print(list(zip(*collection))) # rints separaed lists
# l1 , l2 = (list(zip(*collection))) # assigns the separated lists.
# The following is a function to separate maximum of the pairs in zipped function.
# num_list1 = [1,2,3,4,5,6]
# num_list2 = [7,8,9,10,11,12]
# coll = list(zip(num_list1,num_list2))
# print(coll)
# max_list = []
# for i in coll:
#     max_list.append(max(i))
# print(max_list)
# max_list = [min(pair) for pair in zip(*coll)] # creates two lists and returns minimum element in each list
# print(max_list)
    # ANY AND ALL FUNCTION
# all() checks if all the values in the list are true . If even one value is false then the function returns false else true.
# any() checks if any value of the list is true then it returns true.
    # EXERSICE \\***
# The following is a function to check all input types in addition function:
# def sum (*args):
#     sum = 0
#     if all([(type(arg)==int or type(arg)==float) for arg in args ]):
#         for i in args :
#             sum+=i
#         return sum
#     else :
#         return("WRONG INPUTS")
# sum(1,2,3,4,5)  
# names = ['Anurag','Dilip','Archana','Chinnamma']
# # print(max([len(i) for i in names]))
    # SORTED FUNCTION
# The sort method can  be used to sort the items of a list. But to sort the items of tuple or a set we need to use sorted function.
# sorted(tuple_name/set_name)
# The sorted function can also be used to sort complex data structures. like...
# mangoes = [ {'name' : 'Alphonso', 'price':100},{'name' : 'Payari', 'price':80},{'name' : 'Gavran', 'price':70},{'name' : 'Makkhi Choos', 'price':50}]
# print(sorted(mangoes, key = lambda dictionary : dictionary.get("price")))





    # CAHPTER 12
    # PRE_DIRECTOR INTRODUCTION \\***
    # ASSIGINING FUNCTION TO A VARIABLE
# def square(a):
#     return a**2
# s = square # here we have assigned the variable s to be a pointer to the function square. Note no parantehsis.
# print(s)
# print(square)# both will print the same memory location as s points to the location of the function square.  
# print(s.__name__)#will print the name square same as...
# print(square.__name__)
# print(s(8))# will call the function.
    # PASSING FUNCTION AS AN ARGUMENT 
# def square(a):
#     return a**2
# l = [1,2,3,4,5,6,7]
# def my_func(function , list):
#     new_list = []
#     for item in list:
#         new_list.append(function(item))
#     return new_list
# print(my_func(square , l))
# # we can also pass lamda function as argument to the function my_func
# print(my_func(lambda a : a**3,l)) 
    # FUNTIN RETURNING FUNCTION 
# def outer_function(message):
#     print("INSIDE OUTER FUNCTION \n")
#     def inner_function():
#         print("INSIDE INNER FUNCTION \n ")
#         print(f"THE MESSAGE IS {message}")
#     return inner_function # function outer_function returns inner_function 
# variable = outer_function(" HELLO WORLD ! ")
# variable()
    # FUNCTION CLOSURE EXAMPLE 
# def to_power (x):
#     def power (n):
#         return n**x
#     return power
# cube = to_power(3)
# print(cube(6))
# square = to_power(2)
# print(square(7))
# print(to_power(3))
    # DECOTRATORS
# Decotatros are used to enhance the functionality of any other function.
# @ is used for implicitly calling decorator function
# The folowing is an example of a decorator function 
# def decorator_function  (function):
#     def wrapper_function():
#         print("THIS IS ADDITIONAL FUNCTIONALITY")
#         function()
#     return wrapper_function
# @ decorator_function # This adds the additional functionality of decorator_function() to the function func() impicitly every time it is called.
# def func():
#     print ("THIS IS FUNCTION func()")
# func()
# However the problem with the above decorator_function() is that, if we pass any argument to the function which is decorated it give an error.
# Here we need to understand that dectorator_function is simply a function which calls another function.
# However here the wrapper function does not take any arguments. Thus to solve ths problem we can use *args and **kwargs as follows
# def decorator_function_argument (function):
#     def wrapper_function(*args,**kwargs):
#         print("THIS IS ADDITIONAL FUNCTIONALITY")
#         function(*args,**kwargs)
#     return wrapper_function
# @ decorator_function_argument # This adds the additional functionality of decorator_function() to the function func() impicitly every time it is called.
# def func(a,b,c,d):
#     print (f"THIS IS FUNCTION func() TAKING ARGUMENTS {a} {b} {c} {d}")
# func(3,4,5,6)
    # NESTED RETURNING
# Using decorator funcion for a function that returns a value.
# def decorator_function_return (function):
#     def wrapper_function(*args,**kwargs):
#         print("THIS IS ADDITIONAL FUNCTIONALITY")
#         return function(*args,**kwargs) # Here the function 
#     return wrapper_function
# @ decorator_function_return # This adds the additional functionality of decorator_function() to the function func() impicitly every time it is called.
# def func(a,b,c,d):
#     print (f"THIS IS FUNCTION func() TAKING ARGUMENTS {a} {b} {c} {d} AND RETURNS THEIR SUM : \n")
#     return a+b+c+d
# print(func(3,4,5,6))
    # USING DOC STRINGS WITH DECORATOR FUNCTIONS
# The folowing is an example of a decorator function using doc strings 
# def decorator_function  (function):
#     def wrapper_function():
#         """THIS IS WRAPPER FUNCTION"""
#         print("THIS IS ADDITIONAL FUNCTIONALITY")
#         function()
#     return wrapper_function
# @ decorator_function # This adds the additional functionality of decorator_function() to the function func() impicitly every time it is called.
# def func():
#     """THIS IS func() FUNCTION"""
#     print ("THIS IS FUNCTION func()")
# print(func.__doc__) # instead of printing the doc string it prints the doc string for wrapper function. 
# So for  the following is the syntax.
# from functools import wraps # IMP
# def decorator_function  (function):
#     @wraps(function)
#     def wrapper_function():
#         """THIS IS WRAPPER FUNCTION"""
#         print("THIS IS ADDITIONAL FUNCTIONALITY")
#         function()
#     return wrapper_function
# @ decorator_function # This adds the additional functionality of decorator_function() to the function func() impicitly every time it is called.
# def func():
#     """THIS IS func() FUNCTION"""
#     print ("THIS IS FUNCTION func()")
# print(func.__doc__) # Now this will print the doc string for the function func()
    # DECORATOR TO CALCULATE THE TIME OF EXECUTION FOR A PARTICULAR FUNCTION
# from functools import wraps
# import time
# def time_decorator(function):
#     @wraps(function)
#     def wrapper_func(*args,**kwargs):
#         print("THIS IS ADDITIONAL FUNCTINOALITY \n")
#         print(f"THIS IS FUNCTION {function.__name__}")
#         initial_time  = time.time()
#         returned_value = function(*args,**kwargs)
#         end_time  = time.time()
#         print(f"TIME TAKEN TO EXECUTE FUNCTION IS {end_time - initial_time}")
#         return returned_value
#     return wrapper_func
# @time_decorator
# def addition(a,b,c,d):
#     return a+b+c+d
# print(addition(2,3,4,5))
    # DECOATOR FUNCTION TO CHECK THE DATA TYPES OF THE ARGUMENTS PASSED TO A FUNCTION
# Here assume that all the arguments passed to the function to be passed should all be integers
# from functools import wraps
# def arg_decorator (function):
#     @wraps(function)
#     def wrapper_function (*args ,**kwargs):
#         if(all([type(arg) == int for arg in args ])):
#             return function (*args ,**kwargs)
#         else:
#             return "INVALID ARGUMENTS"
#     def wrapper_function (*args ,**kwargs):
#          data_types = []
#          for i in args:
#              data_types.append(type(i) == int)
#          if all(data_types):
#              return function(*args ,**kwargs)
#          else:
#              return "INVALID ARGUMENTS"
#     return wrapper_function
# @arg_decorator
# def addition(a,b,c,d):
#     return a+b+c+d
# print(addition(2,3,4,"name"))
# print(addition(2,3,4,5))
    #   DECORATOR NESTING
# In the above function arg_decorator we defined it only for integers. 
# from functools import wraps
# def any_type(data_type):
#     def arg_decorator (function):
#         @wraps(function)
#         def wrapper_function (*args ,**kwargs):
#             if(all([type(arg) == data_type  for arg in args ])):
#                 return function (*args ,**kwargs)
#             else:
#                 return "INVALID ARGUMENTS"
#         return wrapper_function
#     return arg_decorator
# @any_type(int)
# def addition(a,b,c,d):
#     return a+b+c+d
# print(addition(2,3,4,"name"))
# print(addition(2,3,4,5))





    # CHAPTER 13
    # GENERATORS 
# Generators are iterators which are generated at runtime unlike lists.
# A list is a collection of data items which is stored in the memory as a whole. This might be ideal for applications involving permanant storage of data and manipulating the same.
# But in conditions which require using the stored data only once and the size of the data is large it makes sense to just create an object which creates the data only while in use and delete it after the scope is finished.
    # CREATING YOUR OWN GENERATOR
# def nums_generator (n):
#     for i in range (1,n+1):
#         yield i # yield is a keyword which is used to create a generator.
# numbers = nums_generator(10) # here we have assigned the generator to numbers 
# for i in numbers:
    # print(numbers) # The for loop generates each number one at a time and the destroys the memory.
# for i in numbers:
    # print(numbers) # This will not print the numbers as all the memory has been destroyed.
# for i in nums_generator(10):
    # print(numbers) # This will print the numbers as we are generating the numbers again.
    # GENERATOR COMREHENSION
# squares_generator = (i**2 for in range(1,11))
    # COMPARING TIME BETWEEN LIST AND GENERATORS 
# import time 
# t1 = time.time()
# list = [i for i in range(1000000000) ]
# print(time.time() - t1) # Time taken to create list
# t2 = time.time()
# generator = (i for i in range(1000000000))
# print(time.time() - t2) # Time taken to create generator is less than that for lists





    # CHAPTER 14 
    # OBJECT ORIENTED PROGRAMMING IN PYTHON 
    # BASIC OOP CONCEPTS
        # ENCAPSULATION
        # Encapsulation is defined as the wrapping up of data under a single unit. 
        # It is the mechanism that binds together code and the data it manipulates.Other way to think about encapsulation is, it is a protective shield that prevents the data from being accessed by the code outside this shield.
        # It is also known as data-hiding.
        # ABSTRACTION
        # Data abstraction is one of the most essential and important feature of object oriented programming in C++. 
        # Abstraction means displaying only essential information and hiding the details. 
        # Data abstraction refers to providing only essential information about the data to the outside world, hiding the background details or implementation.
        # NAMING CONVENTIONS AND NAME MANGLING 
        # Python does not use the concepts of private, protected and public access types for data as in C++. All data is public in python.
        # Python developers use _varible_name to denote that the variable of name variable_name is private and should not be changed outside the class.
# class Variable:
#     def __init__(self, variable_name ,_variable_value):
#         self.__variable_name = variable_name  # Here Python changes variable_name to _Variable__variable_name to avoid accidental changes to the variable, this is called name mangling . 
#         self._variable_value = _variable_value # _ before _variable_value is just to denote that it is private.
# v1 = Variable("Anurag", 19)
# print(v1.__dict__) # prints :: {'_Variable__variable_name': 'Anurag', '_variable_value': 19} thus changing variable_name to _Variable__variable_name.
    # INSTANCE VARIABLES AND INSTANCE METHOD (CONSTRUCTORS)
# Instance method is a class function which takes a class object as a parameter.
# class Person:
#     def __init__(self, first_name, last_name, age):
#         print("INITIATOR CALLED")
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def full_name(self):
#         return (f"THE FULL NAME IS {self.first_name}  {self.last_name} ")
# p1 = Person('Anurag', 'Gorkar', 19) # p1 First instance variable (object) created 
# p2 = Person('Avani', 'Gorkar', 8) # p2 Second instance variable (object) created 
# print(p1.full_name())
# # p1.full_name() is interpreted as . Hence the significance of writing self.
# print(Person.full_name(p1))
    # CLASS VARIABLES AND CLASS METHODS 
# Class methods are class functions which take class as parameter.
# Class methods can also be used to create custom consrtuctors. 
# class Circle:
#     pi = 3.141 # pi is a class variable.
#     colour = "Red" # colour is a class variable.
#     class_instance  =  0 # class_instance is a class variable.
#     def __init__(self, radius, name): # initiator for Circle class 
#         print("CIRCLE CREATED.")
#         self.radius = radius # radius is a instance variable. 
#         self.name = name # name is a instance variable.
#         Circle.class_instance += 1 # class_instance is a class variable hence it is accessed using class variable                                                                                
#     @classmethod
#     def string_constructor(cls, string): # This is a class method used as a constructor which takes first parameter as class and next are values of the circle radius and colour in a string.
#         radius, name = string.split(',')
#         return cls(radius,name) # returns the radius and name to initiator of the class and the init method is executed 
#     @classmethod # decorator to define a class method.
#     def no_of_insatnces(cls): # cls represents class which s a parameter for the mehod no_of_instances
#         print(f"THE CLASS {cls.__name__} HAS A TOTAL OF {cls.class_instance} INSTANCES.") 
#     def cal_circumferance(self):
#         print(f"THE CIRCUMFERANCE OF THE CIRCLE IS {2*Circle.pi*self.radius}. ")# pi is a class variabe accessed by class name Circle.
#     def disp_circle_colour(self):
#         print(f"THE COLOUR OF THE CIRCLE IS {self.colour}. ") # Here python checks if the object self has an instance variable called colour if not it outputs the default value of colour as a class variable.
# c1 = Circle(10 , "Anurag")
# c2 = Circle(5 , "Avani")
# c3 = Circle.string_constructor("15,Dilip")
# c2.colour = "Green" # Adds a new instance variable to the object c2
# Circle.no_of_insatnces() # As no_of _instances is a class method we use class name to acess it.
# c2.no_of_insatnces() # However it can also be accessed using a class instance 
# print(c1.__dict__)
# print(c2.__dict__)
# c1.cal_circumferance()
# c2.cal_circumferance()
# c2.disp_circle_colour()
# c1.disp_circle_colour()
    # PROPERTY AN DECORATOR ##################################################################################################
    # INHERITANCE
# class Parent:
#     def __init__(self, name, age, height, weight):
#         self.name = name
#         self.age = age 
#         self.height = height
#         self.weight = weight 
# class Child(Parent):
#     def __init__(self, name, age, height, weight, school_name, standard):
#         # Parent.__init__(self, name, age, height, weight) # Uncommon method - execute either one 
#         super().__init__(name, age, height, weight) # Common method execute - either one
#         self.school_name = school_name
#         self.standard = standard
# child_1 = Child("Anurag", 19 , 176, 62, "AVEMHS", 10)
# print(child_1.__dict__) 
    # METHOD RESOLUTION ORDER AND METHOD OVERRIDING
# The following is an example of multilevel inheritance. Phone -> Smart_phone -> Flagship_phone
# Method full_specs has been overridden in the following example   
# class Phone :
#     def __init__(self, brand, model_name, price):
#         self.brand = brand 
#         self.model_name = model_name
#         self.price = price 
#     def full_specs(self):
#         return f"THE DETAILS ARE {self.brand}   {self.model_name}   {self.price}"
# class Smart_Phone (Phone) :
#     def __init__(self, brand, model_name, price, front_camera_mp, rear_camera_mp):
#         super().__init__(brand, model_name, price)
#         self.front_camera_mp = front_camera_mp
#         self.rear_camera_mp = rear_camera_mp
#     def full_specs(self):
#         return f"THE DETAILS ARE {self.brand}   {self.model_name}   {self.price}    {self.front_camera_mp}  {self.rear_camera_mp}"   
# class Flagship_phone(Smart_Phone):
#     def __init__(self, brand, model_name, price, front_camera_mp, rear_camera_mp, gpu, finger_print_scanner):
#         super().__init__(brand, model_name, price, front_camera_mp, rear_camera_mp)
#         self.gpu = gpu 
#         self.finger_print_scanner = finger_print_scanner
#     def full_specs(self):
#         return f"THE DETAILS ARE {self.brand}   {self.model_name}   {self.price}    {self.front_camera_mp}  {self.rear_camera_mp}   {self.gpu}  {self.finger_print_scanner}" 
# one_plus7T = Flagship_phone("One Plus","7T", 50000, 20, 40, "Yes", "Yes")        
# print(one_plus7T.__dict__)
# # Method Resolution Order defines the order in which Python looks for the methods called by the instance of any class.
# print(help(one_plus7T)) # Searches first in Flagship_phone if not found then in Smart_Phone and after that in Phone.
# print(Flagship_phone.mro()) # Alternate ways to print MRO for a class.
# print(Flagship_phone.__mro__)
#     # isinsatnce AND issubclass
# print(isinstance(one_plus7T, Flagship_phone)) # Prints true if the object is an instance of the mentioned class
# print(isinstance(one_plus7T, Smart_Phone)) # Prints true because the Flagship_phone is child of Smart_Phone class
# print(issubclass(Flagship_phone, Phone)) # Prins true if the fist class is derived from the second class.
    # SPECIAL METHODS DENDER METHODS ############################################################################################################################################
    
    



    # CHAPTER 15  
    # BUILT IN ERRORS IN PYTHON
        # Types of errors in Python 
        # Syntax Error : Using wrong syntax.
# print"Hello"
        # Indentation Error : Giving wrong/invalid  indentation while writing programme. 
# def func():
#         print("Hello")
#             print("Indentation Error")
#         return 0
        # Name Error : Using a variable that has no been defined yet.
# print(s+3)
        # Type Error : Using invalid data types together like adding an integer and a string.
# print(3 + "Anurag")
        # Value Error : Converting invalid data types like converting non-numeric string into integer.
# s = "Anurag"
# print(int(s))
        # Attribute Eror : Calling nonexisting method for a class
# l = [1,2,3,4]
# l.push(12)
        # Key Error : Using key snot defined in a dictionary.
# d = {"Name" : "Anurag", "Surname" : "Gorkar" }
# print(d["Age"])
    # RAISING ERRORS
# def addition (a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     raise TypeError("INVALID TYPE OF ARGUMENTS ARE PASSED") # raise is keyword and TypeError is the type of the error.
# addition ("anurag",1)
    # ABSTRACT METHODS / NotImplementedError
# NotImplementedError is an error which is raised when the we have not implemented a  instance method in the child of a parent class which has to be compusorily done.
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def sound(self):
#         raise NotImplementedError("YOU HAVE TO DEFINE SOUND METHOD FOR ALL THE DERIVED CLASSES")
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed
#     def sound(self):
#         return ("BOW-WOW BOW-WOW ")
# class Cat(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed
# doggy  =  Dog("Spike", "Bulldog")
# print(doggy.sound())
# kitty  =  Cat("Tom", "Persian")
# print(kitty.sound()) # Raises NotImplementedError
    # EXCEPTION HANDLING 
# try block is used in that part of the programme which might throw an error
# while True:
#     try:
#         Roll_no  =  int(input("Enter your rollno."))
#         break
#     except ValueError: # Executes if ValueError occurs while executingthe programme 
#         print("You entered wrong data type for Roll_no")
#     except : # Executes if the error is not of type ValueError or is used as default type.
#         print("Unexpected Error")
# print("Age taken as input")
# The following is a programme used to check ZeroDivisionError.
# def divide (a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as error :
#         print(error)
#     except TypeError as err :
#         print(err)
#     except :
#         print("UNEXPECTED ERROR.")
# print(divide(10,"anurag"))
# print(divide(10,0))
    # CUSTOM EXCEPTION 
# class PasswordTooShort(ValueError) :
#     pass
# def validate (password):
#     if len(password)<5 :
#         raise PasswordTooShort("Password is too short")
# password  = input ('Enter your password : ')
# validate(password)
# print("THANKYOU ! ! !")





    # CAHPTER 16
    # FILE HANDLING IN PYTHON 
#   # OPEN METHOD
# f = open("pfile.txt", 'r') # open method is used to open a file in python. 'r' specifies that file is to be opened in read mode. 'w' is used to open file in write mode .File is opened in default read mode.  
#   # TELL METHOD
# print(f"CURSOR POSITION IS : {f.tell()}") # tell method returns the current position of the read cursor. 
#   # READ METHOD 
# print(f.read()) # read method returns all the contents of the file. 
# print(f"CURSOR POSITION IS : {f.tell()}") # Read cursor is at the end of the file.
# print(f.read()) # does not output anything as the reading cursor is at the last of the file after first read operation.
#    # SEEK METHOD
# f.seek(0) # seek method is used to set cursor position to specified position in the file.
# print(f.read()) # read method returns all the contents of the file. 
#   # READLINE METHOD 
# print(f.readline(), end = "") # readline method is used to read single line at a time. end is used to remove the extra space between the  lines outputted on the screen.
# print(f.readline())
#   # READLINES METHOD 
# lines = f.readlines() # readlines method returns a list of all the lines in the file.
# print (lines)
# print(len(lines))
# for l in lines:
#     print(l ,end = "")
#   # DATA DESCRIPTORS
# print(f.name) # name prints the name of the file.
# print(f.closed) # closed returns boolean whether the file is closed or not.
# #   # CLOSE METHOD 
# f.close() # close method closes the file.
# print(f.closed)
# f = open(r"C:\Users\lenovo\Desktop\PROGRAMME FILES\MY PYTHON CODES\pfile.txt") # r is used to skip any character escape sequences.
# for line in f: # f is an iterator .
#     print(line, end = "")
# f.seek(0)
# for l in f.readlines()[:2]:
#     print(l , end = "")
# f.close()
    # WITH BLOCK (context manager)
# with open("pfile.txt") as f: # with block is a context manager which automatically closes the file.
#     print(f.read())
# print(f.closed)
    # WRITIING IN A FILE
# with open('pfile.txt', 'w') as f: # w writes the data to a file overiding the original data.
#     f.write("hello")
# with open('pfile.txt', 'a') as f: # a wirtes the data to a file after the initial data. 
#     f.write(" how you doin' ?")
# with open('pfile.txt', 'r+') as f: # r+ wirtes the data to a file by repalcing the initial bytes of the original string by the one to be written. 
#     f.write("Avani")
# with open('pfile.txt', 'r+') as f: # r+ wirtes the data to a file by repalcing the initial bytes of the original string by the one to be written. 
#     f.seek(len(f.read())) # To set the file pointer at the end of the file and then write data to it  at the end of the file. 
#     f.write(". \nFine.")
    # READING CSV FILE IN PYTHON
# csv is a file type to store tabular form of data.     
    # READ CSV FILE USING reader method
# from csv import reader
# with open("pcsvfile.csv", 'r') as rf:
#     csv_read = reader(rf) # reader returns the file contets in the form of a list.
#     for r in csv_read:
#         print(r)
#     # READ CSV FILE USING DictReader method
# from csv import DictReader
# with open("pcsvfile.csv", 'r') as rf:
#     csv_read = DictReader(rf) # DictReader returns the file contets in the form of a dictionary. 
#     for r in csv_read:
#         print(r['name']) # prints only data having key name.
    # WRITE DATA TO CSV FILE
# import pandas as pd
# from csv import writer
# with open("pcsvfile2.csv", 'w', newline="") as wf:
#     csv_write = writer(wf)
#     wf.head(3) 
#     csv_write.writerow(["Name" , "Age"])
#     csv_write.writerow(["Anurag" , '20'])
#     # df.set_value(1, "Age", 30)
#     csv_write.writerow(["Avani" , '8'])
#     csv_write.writerows([["Dilip",'50'],["Archana", '45']])
# wf.close()

  








 






 



        









 




            
    




 





