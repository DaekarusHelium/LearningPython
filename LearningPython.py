# -*- coding: utf-8 -*-
# Created on Sun Sep 29 23:22:54 2024
# @author: Steve Brent

###################################################################################################

# word = input("Please insert a word: ")
# counter = 0
# for w in word:
#         counter = counter + word.count(w)
# if counter == len(word):
#         answer = "True"
#         print(answer)
#         print(counter)
# else:
#     answer = "False"
#     print(answer)
#     print(counter)

#####

# num = 10
# fraction = 5/100
# print(f'{num*fraction} is {fraction*100}% of {num:,}')
# print(f'{num-fraction} is {num} stocazzo!')

# name = input('Enter your name: ')
# print('Are you really', name,'?')
# print(f'Are you really {name}?')
# print('Are you really ' + name + '?')

# n = input('Enter an integer: ')
# print(type(n))

# dateofbirth = input('Specify your birthday date in dd/mm/yyyy: ')
# print('You were born in the year: ', dateofbirth[6:len(dateofbirth)])

# print('Mluvíš anglicky?')

# Calculate the power of a number
# x = 3
# ans = 0
# num_iteration = 0
# while (num_iteration < x):
#     ans = ans + x
#     num_iteration = num_iteration + 1
# print(f'{x}*{x} = {ans}')

# Concatenate X to to_print num_x times
# num_x = int(input('How many times should I print the letter X? '))
# to_print = ''
# while num_x > 0:
#     to_print = to_print + 'X'
#     num_x = num_x - 1
# print(to_print)

# Find a positive integer that is divisible by both 11 and 12
# x = 1
# while True:
#     if x%11 == 0 and x%12 == 0:
#         break
#     x = x +1
# print(x, 'is divisible by both 11 and 12!')

# Input 10 numbers and print the largest odd number, message if no answer

# maximo = 0
# num1 = int(input('Inserisci numero: '))
# if num1 > maximo and num1%2 !=0:
#     maximo = num1
# num2 = int(input('Inserisci numero: '))
# if num2 > maximo and num2%2 !=0:
#     maximo = num2
# num3 = int(input('Inserisci numero: '))
# if num3 > maximo and num3%2 !=0:
#     maximo = num3
# num4 = int(input('Inserisci numero: '))
# if num4 > maximo and num4%2 !=0:
#     maximo = num4
# num5 = int(input('Inserisci numero: '))
# if num5 > maximo and num5%2 !=0:
#     maximo = num5
# num6 = int(input('Inserisci numero: '))
# if num6 > maximo and num6%2 !=0:
#     maximo = num6
# num7 = int(input('Inserisci numero: '))
# if num7 > maximo and num7%2 !=0:
#     maximo = num7
# num8 = int(input('Inserisci numero: '))
# if num8 > maximo and num8%2 !=0:
#     maximo = num8
# num9 = int(input('Inserisci numero: '))
# if num9 > maximo and num9%2 !=0:
#     maximo = num9
# num10 = int(input('Inserisci numero: '))
# if num10 > maximo and num10%2 !=0:
#     maximo = num10
# if maximo == 0:
#     print('No odd numbers!')
# else:
#     print('Max odd value is:', maximo)
    
#####

# x = 3
# ans = 0
# for num_iterations in range (abs(x)):
#     ans = ans + abs(x)
# print(f'{x}*{x} = {ans}')

##### SOMMA DEI VALORI DI UNA STRINGA

# total = 0
# stringa = input('Inserisci stringa di numeri da sommare: ')
# for c in stringa:
#     total = total + int(c)
# print(total)

##### TROVA LA SOMMA DEI NUMERI PRIMI DISPARI TRA 3 E 999

# oddnums = range(3, 15, 2)
# print('Lista da analizzare: ', list(oddnums))
# primesum = 0
# for o in oddnums:
#     check = True
#     print('Testo il numero: ', o)
#     for r in range(2, o):
#         if o % r == 0:
#             check = False
#     if check == True:
#         print('We have a WINNER!: ', o)
#         primesum = primesum + o
#         print('Primesum provvisorio è: ', primesum)
# print('primesum final: ', primesum)

###################################################################################################
#Print the sum of the prime numbers greater then 2 and less then 1000 (flag status version) 

# cumulative_sum = 0
# primalitytest = True
# for n in range(2,10):
#     if n % 2 != 0:
#         print('Current odd number: ',n)
#         for k in range(2,n-1):
#             if n%k == 0:
#                 primalitytest = False
#         if primalitytest == True:
#             print(n,'is a prime number!')
#             cumulative_sum = cumulative_sum + n
#             print('Temporary sum: ',cumulative_sum)
#         else:
#             print(n, 'is not a prime number!')
#     primality = True
# print ('Final sum is: ',cumulative_sum)

###################################################################################################
##### Print the integer Cube root of and integer (Exhaustive Enumeration Algorithm with Decrementing function: abx(Cube) - CubeRoot**3)

# Cube = int(input('Enter an integer: '))
# print(Cube)
# CubeRoot = 0
# print(CubeRoot)
# while CubeRoot**3 < abs(Cube):
#     print('Value of the decrementing function is:', abs(Cube)-(CubeRoot**3))
#     CubeRoot = CubeRoot + 1
#     print(CubeRoot)
# if CubeRoot**3 != abs(Cube):
#     print(Cube,'is not a perfect Cube')
# else:
#     if Cube < 0:
#         CubeRoot = -CubeRoot
#     print('Cube root of',Cube,'is',CubeRoot)

###################################################################################################
# Calculations speed test

# MaxVal = int(input('Enter a positive integer: '))
# I = 0
# while I < MaxVal:
#     I += 1
#     print(I)
# print(I)

###################################################################################################
# Test if an int > 2 is prime. If not, print smallest divisor

# X = int(input('Enter an integer greater then 2: '))
# SmallestDivisor = None
# for Guess in range(2,X):
#      if X%Guess == 0:
#           SmallestDivisor = Guess
#           break
# if SmallestDivisor != None:
#      print('Smallest Divisor of',X,'is:', SmallestDivisor)
# else:
#      print(X,'is a prime number!')

###################################################################################################
# Test if an int > 2 is prime. If not, print largest divisor (inverted range version)

# X = int(input('Enter an integer greater then 2: '))
# LargestDivisor = None
# for Guess in range(X-1,1,-1):
#      print(Guess)
#      if X%Guess == 0:
#           LargestDivisor = Guess
#           break
# if LargestDivisor != None:
#       print('Largest Divisor of',X,'is:', LargestDivisor)
# else:
#       print(X,'is a prime number!')

###################################################################################################
# Test if an int > 2 is prime. If not, print largest divisor (x*y=z testing version)

# Z = int(input('Enter an integer greater then 2: '))
# LargestDivisor = None
# for GuessX in range(2,Z):
#      for GuessY in range(2,Z):
#           if GuessX * GuessY == Z:
#                print(GuessX, GuessY)
#                if GuessX > GuessY:
#                     LargestDivisor = GuessX
#                else:
#                     LargestDivisor = GuessY
#           break
# if LargestDivisor != None:
#       print('Largest Divisor of',Z,'is:', LargestDivisor)
# else:
#       print(Z,'is a prime number!')
      
###################################################################################################
# Test if and int > 2 is prime. If not, printer smallest divisor

# Z = int(input('Enter an integer greater then 2: '))
# SmallestDivisor = None
# if Z%2 == 0:
#      SmallestDivisor = 2
# else:
#      for Guess in range(3,Z,2):
#           if Z%Guess == 0:
#                SmallestDivisor = Guess
#                break
# if SmallestDivisor !=0:
#      print('Smallest Divisor is: ', SmallestDivisor)
# else:
#      print(Z,'is a prime number!')

###################################################################################################
# Input an integer Z and print two integers: root and pwr, such that 1 < pwr < 6 and root**pwr is equal to Z

# Z = int(input('Insert an integer: '))
# root = 0
# Pwr = 0
# test = 0
# test_final = 0
# root_final = 0
# pwr_final = 0
# while test <= Z:
#      root = root + 1
#      for pwr in range(2,6):
#          test = root**pwr
#          if test == Z:
#               test_final = test
#               root_final = root
#               pwr_final = pwr
# if test_final == 0:
#      print ('No luck!')
# else:
#      print('Root:',root_final,'Power:',pwr_final)
#      print(test_final)

###################################################################################################
# Approximationg the square root using exhaustive enumeration

# x = 123456
# epsilon = 0.01
# step = epsilon**3
# num_guesses = 0
# ans = 0.0
# delta = abs(ans**2 - x)
# while delta >= epsilon and ans*ans <= x:
#      delta = abs(ans**2 - x)
#      print('ANS',ans**2)
#      print('DELTA:',delta)
#      ans += step
#      num_guesses += 1
# print('Number of guesses =', num_guesses)
# if delta >= epsilon:
#      print('Failed on square root of', x)
# else:
#      print(ans, 'is close to square root of', x)

###################################################################################################
# Using bisection search to approximate cubic root

# x = -27
# epsilon = 0.01
# num_guesses = 0
# if x > 0:
#      low = 0
#      high = max(1, x)
# else:
#      low = x
#      high = max(x, -1)
# ans = (high + low)/2
# while abs(ans**3 - x) >= epsilon:
#       print('low = ',low,'high = ',high,'ans = ',ans)
#       num_guesses += 1
#       if x < 0:
#            if ans**3 < x:
#                low = ans
#            else:
#                high = ans
#       else:
#           if ans**3 > x:
#                high = ans
#           else:
#                low = ans
#       ans = (high + low)/2
# print('number of guesses = ',num_guesses)
# print(ans, 'is close to square root of',x)

###################################################################################################
# Using bisection search to estimate log base 2

# x = 0.10
# epsilon = 0.01
# # Find lower bound on ans
# lower_bound = 0
# while 2**lower_bound < x:
#      lower_bound += 1
# low = lower_bound - 1
# high = lower_bound + 1
# #Performa bisection search
# ans = (high + low) / 2
# while abs(2**ans - x) >= epsilon:
#      if 2**ans < x:
#           low = ans
#      else:
#           high = ans
#      ans = (high + low) / 2
# print(ans,'is close to the log base 2 of,',x)

###################################################################################################
# Empire State Building Eggs launch

# total_floors_num = int(input('Total floors number?'))
# breaking_point = int(input('Breaking point?'))
# eggs_left = 7
# high = total_floors_num
# low = 0
# floor = 0
# while eggs_left > 0:
#      floor = (high + low) / 2
#      if floor >= breaking_point:
#           high = floor
#           print(high,'is too high!')
#      if floor < breaking_point:
#           low = floor
#           print(low,'is too low!')
#      eggs_left -= 1
# print('eggs left:',eggs_left)
# print(high)
# print(low)
# print('Breaking point is at least at: ',int(floor),'floor')

###################################################################################################
# Floating points bits exhaustion test (better use: "abs(x-y) < 0.0001" then "x == y")

# x = 0.0
# for i in range(10):
#      x = x + 0.1
# if x == 1.0:
#      print(x, '= 1.0')
# else:
#      print(x, 'is not 1.0')

###################################################################################################
# Implementation of Newton-Raphson method

# k = 25
# epsilon = 0.01
# print('epsilon:',epsilon)
# guess = k/2
# iterations = 0
# print('guess: ',guess)
# while abs(guess**2 - k) >= epsilon:
#      guess = guess - (((guess**2)-k)/(2*guess))
#      print('guess:',guess)
#      iterations += 1
# print('Square root of', k,'is about',guess)
# print('Iterations: ',iterations)

###################################################################################################
# Function for finding roots

# def find_root(x, power, epsilon):
#      #Find interval containing answer
#      if x < 0 and power%2 == 0:
#           return None
#      #Bisection search
#      low = min(-1,x)
#      high = max(1,x)
#      ans = (high + low)/2
#      while abs(ans**power - x) >= epsilon:
#           if ans**power < x:
#                low = ans
#           else:
#                high = ans
#           ans = (high + low)/2
#      return ans
# # Print the sum of three roots calling function
# print(find_root(25,2,0.001))
# print(find_root(-8,3,0.001))
# print(find_root(16,4,0.001))
# RootsSum = find_root(25,2,0.001) + find_root(-8,3,0.001) + find_root(16,4,0.001)
# print(round(RootsSum,1))

###################################################################################################
# Write a function is_in that checks if a string is inside the other:
# Function definition
# def is_in(string1,string2):
#      ans = (string1 in string2) or (string2 in string1)
#      return ans
# # Test function definition:
# def is_in_test(list1, list2):
#      for s1 in list1:
#           for s2 in list2:
#                print(is_in(s1,s2))
# # Test:
# list1 = ('icarus','daedalus','morph')
# list2 = ('dalus','carus','morpheus')
# is_in_test(list1,list2)

####################################################################################################
# Write a function mult that accepts either one or two ints as arguments.
# If called with two arguments, the function prints the product of the two arguments.
# If called with one argument, it prints that argument.

# def mean(*args):
#      tot = 0
#      for a in args:
#           tot += a
#           print(tot)
#      print(len(args))
#      return tot/len(args)

# print(mean(1,2,3,4,5,6,7,8,9))

####################################################################################################
# Understanding scoping and stack frames
####################################################################################################

# def f(x):
#      def g():
#           x = 'abc'
#           print('x = ', x)
#      def h():
#           z = x
#           print ('z = ', z)
#      x = x + 1
#      print('x = ', x)
#      h()
#      g()
#      print('x = ', x)
#      return g
# x = 3
# z = f(x)
# print('x = ', x)
# print('z = ', z)
# z()

####################################################################################################
# Lambda Expressions
####################################################################################################

# LambdaFunction = lambda x, y: x * y
# x = int(input('First number? '))
# y = int(input('Second number? '))
# z = LambdaFunction(x, y)
# print(z)

####################################################################################################

# def find_last(s,sub):
#      if len(s) or len(sub) == 0:
#           print('No empty strings allowed!')
#      else:
#           index = s.find(sub)
#           print(index)
# s = 'suburbia'
# sub = 'b'
# print(find_last(s,sub))

#################################################################################################### 

# def CreateEvalAns():
#      power = input('Enter a positive integer: ')
#      return lambda ans: ans**int(power)

# def LambdaFunctionContainer(Ans, Multi):
#      Ans = Ans*Multi
#      return

# Ans = 2
# EvalAns = CreateEvalAns()
# print(LambdaFunctionContainer(Ans, EvalAns))

# print("--- Linkedin Python Course ---")
# x = 5
# print(x)
# name = 'Ryan'
# print(name)
# print(type(name))
# print(type(x))
# print(type(1j * 1j))
# print(1j * 1j)
# print('1'+'1')
# false = True
# print(false)
# print(1 == 1)
# my_list = [1,2,3,4]
# print(my_list)
# print(len(my_list))
# my_list = [1,['topo'],2,['gigio'],3,4]
# print(my_list)
# print(len(my_list))
# my_set = {1,2,3,4,4,2,3,3,3,3}
# print((my_set))
# print(len(my_set))
# print('[1,2] == [1,2]', [1,2] == [1,2])
# print('[1,2] == [2,1]',[1,2] == [2,1])
# print('{1,2} == {2,1}', {1,2} == {2,1})
# my_tuple = ('uno', 'due', 'tre')
# print(my_tuple)
# my_list.append('4')
# print('Appending "4" to my_list:', my_list)
# print('Cannot ".append" to tuples!!!')
# my_dictionary = {
#     'apple': 'A red fruit',
#     'bear': 'A scary animal'
# }
# print(my_dictionary['apple'])
# print('Keys must be unique in dictionaries')
# print('Order of the elements is irrelevant in Sets and Dictionaries')
# #####
# a = True
# b = False
# c = True
# if a == True:
#     print('Oh, a is true!')
#     if b == True:
#         print('Also b is true!')
#         if c == True:
#             print('Also c is true!')
# else:
#     print('a is false')
# print('End of program')
# #####
# a = [1,2,3,4,5]
# for item in a:
#     print(item)
# #####
# print('While Loop')
# a = 0
# while a < 5:
#     print(a)
#     a = a + 1


# -*- coding: utf-8 -*-
# Created on Sun Sep 29 23:22:54 2024
# @author: DaekarusHelium

#
#print("Yankees rule,","but not in Boston!")
#
# pi = 3
# radius = 11
# area = pi * (radius**2)
# radius = 14
# print ("Area is: ",area)

######

# x = int(input('Enter an integer: '))
# cube = 0
# while cube**3 < abs(x):
#      cube = cube + 1
# if cube**3 != abs(x):
#      print(x, 'is not a perfect cube')
# else:
#      if x < 0:
#           cube = -cube
#      print('Cube root of',x,'is',cube)

###################################################################################################

# word = input("Please insert a word: ")
# counter = 0
# for w in word:
#         counter = counter + word.count(w)
# if counter == len(word):
#         answer = "True"
#         print(answer)
#         print(counter)
# else:
#     answer = "False"
#     print(answer)
#     print(counter)

###################################################################################################

# num = 10
# fraction = 5/100
# print(f'{num*fraction} is {fraction*100}% of {num:,}')
# print(f'{num-fraction} is {num} anche no!')

# name = input('Enter your name: ')
# print('Are you really', name,'?')
# print(f'Are you really {name}?')
# print('Are you really ' + name + '?')

# n = input('Enter an integer: ')
# print(type(n))

# dateofbirth = input('Specify your birthday date in dd/mm/yyyy: ')
# print('You were born in the year: ', dateofbirth[6:len(dateofbirth)])

# print('Mluvíš anglicky?')

# Find a positive integer that is divisible by both 11 and 12

# x = 1
# while True:
#     if x%11 == 0 and x%12 == 0:
#         break
#     x = x +1
# print(x, 'is divisible by both 11 and 12!')

###################################################################################################
# Input 10 numbers and print the largest odd number, message if no answer

# maximo = 0
# num1 = int(input('Inserisci numero: '))
# if num1 > maximo and num1%2 !=0:
#     maximo = num1
# num2 = int(input('Inserisci numero: '))
# if num2 > maximo and num2%2 !=0:
#     maximo = num2
# num3 = int(input('Inserisci numero: '))
# if num3 > maximo and num3%2 !=0:
#     maximo = num3
# num4 = int(input('Inserisci numero: '))
# if num4 > maximo and num4%2 !=0:
#     maximo = num4
# num5 = int(input('Inserisci numero: '))
# if num5 > maximo and num5%2 !=0:
#     maximo = num5
# num6 = int(input('Inserisci numero: '))
# if num6 > maximo and num6%2 !=0:
#     maximo = num6
# num7 = int(input('Inserisci numero: '))
# if num7 > maximo and num7%2 !=0:
#     maximo = num7
# num8 = int(input('Inserisci numero: '))
# if num8 > maximo and num8%2 !=0:
#     maximo = num8
# num9 = int(input('Inserisci numero: '))
# if num9 > maximo and num9%2 !=0:
#     maximo = num9
# num10 = int(input('Inserisci numero: '))
# if num10 > maximo and num10%2 !=0:
#     maximo = num10
# if maximo == 0:
#     print('No odd numbers!')
# else:
#     print('Max odd value is:', maximo)
    
########################################################################################################



###################################################################################################
# SOMMA DEI VALORI DI UNA STRINGA

# total = 0
# stringa = input('Inserisci stringa di numeri da sommare: ')
# for c in stringa:
#     total = total + int(c)
# print(total)

###################################################################################################
# TROVA LA SOMMA DEI NUMERI PRIMI DISPARI TRA 3 E 999

# oddnums = range(3, 15, 2)
# print('Lista da analizzare: ', list(oddnums))
# primesum = 0
# for o in oddnums:
#     check = True
#     print('Testo il numero: ', o)
#     for r in range(2, o):
#         if o % r == 0:
#             check = False
#     if check == True:
#         print('We have a WINNER!: ', o)
#         primesum = primesum + o
#         print('Primesum provvisorio è: ', primesum)
# print('primesum final: ', primesum)

###################################################################################################
#Print the sum of the prime numbers greater then 2 and less then 1000 (flag status version) 

# cumulative_sum = 0
# primalitytest = True
# for n in range(2,10):
#     if n % 2 != 0:
#         print('Current odd number: ',n)
#         for k in range(2,n-1):
#             if n%k == 0:
#                 primalitytest = False
#         if primalitytest == True:
#             print(n,'is a prime number!')
#             cumulative_sum = cumulative_sum + n
#             print('Temporary sum: ',cumulative_sum)
#         else:
#             print(n, 'is not a prime number!')
#     primality = True
# print ('Final sum is: ',cumulative_sum)

###################################################################################################
# Print the integer Cube root of and integer (Exhaustive Enumeration Algorithm with Decrementing function: abx(Cube) - CubeRoot**3)

# Cube = int(input('Enter an integer: '))
# print(Cube)
# CubeRoot = 0
# print(CubeRoot)
# while CubeRoot**3 < abs(Cube):
#     print('Value of the decrementing function is:', abs(Cube)-(CubeRoot**3))
#     CubeRoot = CubeRoot + 1
#     print(CubeRoot)
# if CubeRoot**3 != abs(Cube):
#     print(Cube,'is not a perfect Cube')
# else:
#     if Cube < 0:
#         CubeRoot = -CubeRoot
#     print('Cube root of',Cube,'is',CubeRoot)

###################################################################################################
# Calculations speed test

# MaxVal = int(input('Enter a positive integer: '))
# I = 0
# while I < MaxVal:
#     I += 1
#     print(I)
# print(I)

##### Test if an int > 2 is prime. If not, print smallest divisor

# X = int(input('Enter an integer greater then 2: '))
# SmallestDivisor = None
# for Guess in range(2,X):
#      if X%Guess == 0:
#           SmallestDivisor = Guess
#           break
# if SmallestDivisor != None:
#      print('Smallest Divisor of',X,'is:', SmallestDivisor)
# else:
#      print(X,'is a prime number!')

###################################################################################################
# Test if an int > 2 is prime. If not, print largest divisor (inverted range version)

# X = int(input('Enter an integer greater then 2: '))
# LargestDivisor = None
# for Guess in range(X-1,1,-1):
#      print(Guess)
#      if X%Guess == 0:
#           LargestDivisor = Guess
#           break
# if LargestDivisor != None:
#       print('Largest Divisor of',X,'is:', LargestDivisor)
# else:
#       print(X,'is a prime number!')

###################################################################################################
# Test if an int > 2 is prime. If not, print largest divisor (x*y=z testing version)

# Z = int(input('Enter an integer greater then 2: '))
# LargestDivisor = None
# for GuessX in range(2,Z):
#      for GuessY in range(2,Z):
#           if GuessX * GuessY == Z:
#                print(GuessX, GuessY)
#                if GuessX > GuessY:
#                     LargestDivisor = GuessX
#                else:
#                     LargestDivisor = GuessY
#           break
# if LargestDivisor != None:
#       print('Largest Divisor of',Z,'is:', LargestDivisor)
# else:
#       print(Z,'is a prime number!')
      
###################################################################################################
# Test if and int > 2 is prime. If not, printer smallest divisor

# Z = int(input('Enter an integer greater then 2: '))
# SmallestDivisor = None
# if Z%2 == 0:
#      SmallestDivisor = 2
# else:
#      for Guess in range(3,Z,2):
#           if Z%Guess == 0:
#                SmallestDivisor = Guess
#                break
# if SmallestDivisor !=0:
#      print('Smallest Divisor is: ', SmallestDivisor)
# else:
#      print(Z,'is a prime number!')

##### Input an integer Z and print two integers: root and pwr, such that 1 < pwr < 6 and root**pwr is equal to Z

# Z = int(input('Insert an integer: '))
# root = 0
# Pwr = 0
# test = 0
# test_final = 0
# root_final = 0
# pwr_final = 0
# while test <= Z:
#      root = root + 1
#      for pwr in range(2,6):
#          test = root**pwr
#          if test == Z:
#               test_final = test
#               root_final = root
#               pwr_final = pwr
# if test_final == 0:
#      print ('No luck!')
# else:
#      print('Root:',root_final,'Power:',pwr_final)
#      print(test_final)

###################################################################################################
# Approximationg the square root using exhaustive enumeration

# x = 123456
# epsilon = 0.01
# step = epsilon**3
# num_guesses = 0
# ans = 0.0
# delta = abs(ans**2 - x)
# while delta >= epsilon and ans*ans <= x:
#      delta = abs(ans**2 - x)
#      print('ANS',ans**2)
#      print('DELTA:',delta)
#      ans += step
#      num_guesses += 1
# print('Number of guesses =', num_guesses)
# if delta >= epsilon:
#      print('Failed on square root of', x)
# else:
#      print(ans, 'is close to square root of', x)

###################################################################################################
# Using bisection search to approximate cubic root

# x = -27
# epsilon = 0.01
# num_guesses = 0
# if x > 0:
#      low = 0
#      high = max(1, x)
# else:
#      low = x
#      high = max(x, -1)
# ans = (high + low)/2
# while abs(ans**3 - x) >= epsilon:
#       print('low = ',low,'high = ',high,'ans = ',ans)
#       num_guesses += 1
#       if x < 0:
#            if ans**3 < x:
#                low = ans
#            else:
#                high = ans
#       else:
#           if ans**3 > x:
#                high = ans
#           else:
#                low = ans
#       ans = (high + low)/2
# print('number of guesses = ',num_guesses)
# print(ans, 'is close to square root of',x)

###################################################################################################
# Using bisection search to estimate log base 2

# x = 0.10
# epsilon = 0.01
# # Find lower bound on ans
# lower_bound = 0
# while 2**lower_bound < x:
#      lower_bound += 1
# low = lower_bound - 1
# high = lower_bound + 1
# #Performa bisection search
# ans = (high + low) / 2
# while abs(2**ans - x) >= epsilon:
#      if 2**ans < x:
#           low = ans
#      else:
#           high = ans
#      ans = (high + low) / 2
# print(ans,'is close to the log base 2 of,',x)

###################################################################################################
# Empire State Building Eggs launch

# total_floors_num = int(input('Total floors number?'))
# breaking_point = int(input('Breaking point?'))
# eggs_left = 7
# high = total_floors_num
# low = 0
# floor = 0
# while eggs_left > 0:
#      floor = (high + low) / 2
#      if floor >= breaking_point:
#           high = floor
#           print(high,'is too high!')
#      if floor < breaking_point:
#           low = floor
#           print(low,'is too low!')
#      eggs_left -= 1
# print('eggs left:',eggs_left)
# print(high)
# print(low)
# print('Breaking point is at least at: ',int(floor),'floor')

###################################################################################################
# Floating points bits exhaustion test (better use: "abs(x-y) < 0.0001" then "x == y")

# x = 0.0
# for i in range(10):
#      x = x + 0.1
# if x == 1.0:
#      print(x, '= 1.0')
# else:
#      print(x, 'is not 1.0')

###################################################################################################
# Implementation of Newton-Raphson method

# k = 25
# epsilon = 0.01
# print('epsilon:',epsilon)
# guess = k/2
# iterations = 0
# print('guess: ',guess)
# while abs(guess**2 - k) >= epsilon:
#      guess = guess - (((guess**2)-k)/(2*guess))
#      print('guess:',guess)
#      iterations += 1
# print('Square root of', k,'is about',guess)
# print('Iterations: ',iterations)

###################################################################################################
# Function for finding roots

# def find_root(x, power, epsilon):
#      #Find interval containing answer
#      if x < 0 and power%2 == 0:
#           return None
#      #Bisection search
#      low = min(-1,x)
#      high = max(1,x)
#      ans = (high + low)/2
#      while abs(ans**power - x) >= epsilon:
#           if ans**power < x:
#                low = ans
#           else:
#                high = ans
#           ans = (high + low)/2
#      return ans
# # Print the sum of three roots calling function
# print(find_root(25,2,0.001))
# print(find_root(-8,3,0.001))
# print(find_root(16,4,0.001))
# RootsSum = find_root(25,2,0.001) + find_root(-8,3,0.001) + find_root(16,4,0.001)
# print(round(RootsSum,1))

###################################################################################################
# Write a function is_in that checks if a string is inside the other:
# Function definition
# def is_in(string1,string2):
#      ans = (string1 in string2) or (string2 in string1)
#      return ans
# # Test function definition:
# def is_in_test(list1, list2):
#      for s1 in list1:
#           for s2 in list2:
#                print(is_in(s1,s2))
# # Test:
# list1 = ('icarus','daedalus','morph')
# list2 = ('dalus','carus','morpheus')
# is_in_test(list1,list2)

###################################################################################################
# Write a function mult that accepts either one or two ints as arguments.
# If called with two arguments, the function prints the product of the two arguments.
# If called with one argument, it prints that argument.

# def mean(*args):
#      tot = 0
#      for a in args:
#           tot += a
#           print(tot)
#      print(len(args))
#      return tot/len(args)

# print(mean(1,2,3,4,5,6,7,8,9))

###################################################################################################
# Understanding scoping and stack frames

# def f(x):
#      def g():
#           x = 'abc'
#           print('x = ', x)
#      def h():
#           z = x
#           print ('z = ', z)
#      x = x + 1
#      print('x = ', x)
#      h()
#      g()
#      print('x = ', x)
#      return g
# x = 3
# z = f(x)
# print('x = ', x)
# print('z = ', z)
# z()

###################################################################################################
# Lambda Expressions ?

# x = 1
# y = 2
# lambda x, y: x * y

###################################################################################################
# Searching for sub-strings

# def find_last(s,sub):
#      if len(s) or len(sub) == 0:
#           print('No empty strings allowed!')
#      else:
#           index = s.find(sub)
#           print(index)
# s = 'suburbia'
# sub = 'b'
# print(find_last(s,sub))

###################################################################################################
# Playing with tuples

# L1 = [1,2,3]
# L2 = [4,5,6]
# L3 = L1 + L2
# print('L3 added = ',L3)
# L1.extend(L2)
# print('L1 extended = ',L1)
# L1.append(L2)
# print('L1 appended = ',L1)

###################################################################################################
# Common methods associated with lists

# L = [1,2,3,4,5,6,7,8,9]
# L.append(10)
# print('Appended: ',L)
# print('Counted (5): ',L.count(5))
# L.insert(10,11)
# print('Inserted: ',L)
# L.extend(L)
# print('Extended: ',L)
# L.remove(11)
# print('Removed: ',L)
# print('Indexed (11): ',L.index(11))
# L.pop(20)
# print('Popped (20th): ',L)
# L.sort()
# print('Sorted: ',L)
# L.reverse()
# print('Reversed: ',L)

###################################################################################################
# Cloning issues

# def RemoveDups(L1,L2):
#      """Assumes that L1 and L2 are lists. Remove any element from L1 that also occurs in L2"""
#      for e1 in L1[:]: # L[:] cloned the list so it does not mutate throughout the for loop
#           if e1 in L2:
#                L1.remove(e1)
# L1 = [1,2,3,4]
# L2 = [1,2,5,6]
# RemoveDups(L1,L2)
# print('L1 = ',L1)

###################################################################################################
# Cloning solutions

# import copy
# L = [2] # ! list are mutable !
# L1 = [L] # ! list are mutable !
# L2 = L1[:] # ! list are mutable !
# L2 = copy.deepcopy(L1) # copy makes a stable copy of L1
# L.append(3)
# print(f'L1 = {L1}, L2 = {L2}')

###################################################################################################
# Copying a tuple containing itself

# import copy
# L1 = [2]
# L1.append(L1)
# L2 = copy.deepcopy(L1) # copy keeps copying all the way to the bottom
# print(L2)

######

# def f(expr, OldList, test = lambda x: True):
#      NewList = []
#      for e in range(10):
#           if e%2 == 0:
#                NewList.append(expr(e))
#      return NewList
# expr = [1,2,'a','z',8.1]
# print(expr)
# [[] for _ in range(10)]

# Python code​​​​​​‌‌‌​​​​‌‌‌‌​​‌​‌​​​‌​​​​​ below

def encodeString(stringVal):
    dictVal = dict(stringVal)
    print(dictVal)
pass

# def decodeString(encodedList):
#     # Your code goes here.
#     pass

a = "Ottuplicerrimo"
encodeString(a)

##### FUNCTIONS

# def multiply_by_three(val):
#     return 3 * val
# print(multiply_by_three(4))
# def multiply(v1, v2):
#     return v1 * v2
# print(multiply(1,7))
# myList = [1,2,3,4]
# def appendFive(list):
#     list.append(5)
# print(myList)
# appendFive(myList)
# print(myList)
# print("# Functions can just perform operations on parameters, they don't always need to return a value")
# print(print("# For example the 'print' function value is:"))
# print("Type of None: ",type(None))
# ####
# print("--- Classes ---")
# class Dog:
#     def __init__(self):
#         self.name = "Rover"
#         self.legs = 4
#     def speak(self):
#         print(self.name + " says: Bark!")
# myDog = Dog()
# myOtherDog = Dog()
# myDog.speak()
# myOtherDog.speak()

##### EXERCISE (ME)

# def factorial(num):
#     if type(num) != int:
#         return None
#     fact = 0
#     if num == 0:
#         return 1
#     if num < 0:
#         return None
#     else:
#         fact = num
#         while (num-1) > 0:
#             fact = fact * (num-1)
#             num = num - 1
#         return fact

# print("Testing with 5: ", factorial(5))

##### EXERCISE (TEACHER)

# def factorial(num):
#      if type(num) != int:
#           return None
#      if num < 0:
#           return None
#      fact = 1
#      counter = 1
#      while counter <= num:
#           fact = fact * counter
#           counter = counter + 1
#      return fact

# print("Testing with 5: ", factorial(5))

##### type(Dog('Rover')) = Dog

##### TYPES #####

# print("##### int() str(), etc...are built-in CLASSES of Python (exceptional lower case first letter) used for 'casting'")
# print("##### Casting a string '100' to the integer 100: ", int('100'))
# print("int('100', 2):", int("100", 2))
# print("int('16a', 2):", int("16a", 16))
# print("Warning: unprecise output with floating points as in: 1,2 - 1,0: ", 1.2 - 1.0)
# from decimal import Decimal, getcontext
# print("Decimal(1) / Decimal(3): ", Decimal(1) / Decimal(3))

##### BOOLEAN #####

# goodWeather = False
# haveUmbrella = False
# if goodWeather or haveUmbrella:
#     print("Go out!")
# else:
#     print("Stay inside")

# bool(1)

# import math
# myName = "My name si SB"
# print(myName[0])
# print(myName[1])
# print(myName[0:7])
# print(myName[:7])
# print(myName[2:])
# myList = [0,1,2,3,4,5]
# print(myList[0:3])
# print(len(myName))
# print(len(myList))
# print("My number is: " + str(5))
# print(f"My number is {5} and the second best is {8}")
# print(f"Pi is: {math.pi:.2f}")
# myString = '''
# Ciao
# come
# stai
# '''
# print(myString)

##### BYTE OBJECTS

# myBytes = bytes(4)
# print(myBytes)
# smilebytes = bytes("😁", "utf-8")
# print(smilebytes)
# print(smilebytes.decode("utf-8"))
# smilebytes = bytearray("😁", "utf-8")
# print(smilebytes)
# smilebytes[3] = int("85", 16)
# print(smilebytes)
# print(smilebytes.decode("utf-8"))


##### EXERCISE (ME): Converts a string hexadecimal number into an integer decimal; If hexNum is not a valid hexadecimal number, returns None

# ​​​‌​‌‌‌‌‌​‌​‌​‌​‌​hexNumbers = {
#     '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
#     'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
# }

# def hexToDec(hexNum):
#     decNum = 0
#     if type(hexNum) != str or len(hexNum) > 3:
#         return None
#     else:
#         c = int(len(hexNum))
#         e = int(len(hexNum)) - 1
#         while c > 0: 
#             for i in hexNum:
#                 if i not in hexNumbers:
#                     return None
#                 else:
#                     decNum = decNum + ((16 ** e) * hexNumbers[i])
#                     c = c - 1
#                     e = e - 1
#     return(decNum)
# pass

# Lists

## Slicing

# myList = [0,1,2,3,4,5,6,7,8,9,10]
# print(myList[3:5])
# print(myList[3:])
# print(myList[3::2])
# print(myList[::2])
# for i in range(100):
#     print(i)
# a = range(10)
# print("type(range): ", type(range))
# b = type(range(10))
# print("type(range(10): ", b)
# rangeList = list(range(10))
# print("list(range(10)): ", rangeList)
# print("list(range(10)): ", rangeList[::-1])

## Modifying:

# myList = [1,2,3,4,5]
# myList.append(6)
# print(myList)
# myList.insert(3,100)
# print(myList)
# myList.remove(100)
# print(myList)
# myList.pop()
# print(myList)
# a = [1,2,3]
# b = a
# a.append(4)
# print(a)
# print(b)
# a = [1,2,3]
# b = a.copy()
# a.append(4)
# print(a)
# print(b)

##### Sets:

# mySet = {"a","b","c"}
# print("mySet = {'a','b','c'} (set): ", mySet)
# mySet = set(["a","b","c"])
# print("mySet = set(['a','b'','c']) (list): ", mySet)
# mySet = set(('a','b','c'))
# print("mySet = set(('a','b','c')) (tuple): ", mySet)
# myList = [1,2,3,3,3]
# print("myList = ", myList)
# myList = list(set(myList))
# print("list(set(myList) = ", myList)
# print("The set object is not subscriptable (cannot be indexed as in mySet[1] or 1[0])")
# mySet.add("x")
# print(mySet)
# print("x" in mySet)
# print(len(mySet))
# while len(mySet):
#     mySet.pop()
#     print(mySet)
# mySet = set(('a','b','c'))
# mySet.add("x")
# print(mySet)
# mySet.discard("x")
# print("mySet.discard('x') = ", mySet)

# Tuples

# myTuple = ('a', 'b', 'c')
# print("# myTuple = ('a', 'b', 'c'):")
# print(myTuple)

# def ReturnMultipleValues():
#     return 1,2,3

# # ReturnMultipleValues(): ")
# print(ReturnMultipleValues())
# # type(ReturnMultipleValues())
# print(type(ReturnMultipleValues()))
# # In tuples declaration 'myTuple = (1,2,3)' is the same as 'myTuple = 1,2,3', but first is preferred
# # In functions 'return 1,2,3' is the same as 'return (1,2,3)', but first is preferred --> it defaults to tuples
# a, b, c = ReturnMultipleValues()
# # a, b, c = ReturnMultipleValues()
# # Print (a, b, c) ("unpacking variables")
# print(a, b, c)

# Dictionaries

# animals = {
#     'a': 'Aardvark',
#     'b': 'Bear',
#     'c': 'Cat',
# }

# print(animals)
# # Dictionaries are indexable
# print(animals['a'])
# # Dictionaries are mutable and new elments can be added through assignment
# animals['d'] = 'Dog'
# print(animals)
# animals['a'] = 'Antelope'
# print(animals)
# # Keys and Values are dictionary types, immutable, interables, convertible in list
# print("# animals.keys():")
# print(animals.keys())
# print("# animals.values()): ")
# print(animals.values())
# animalsList = list(animals.keys())
# print(animalsList)
# # Retrieve an element of dictionary (if present)
# print(animals.get('b'))
# print(animals.get('e'))
# # Lenght of a dictionary
# print(len(animals))
# # Dictionary where the values are lists
# pets = {
#     'A': ["Aardvark", "Antelope"],
#     'B': ["Bear"],
# }
# pets['B'].append("Bison")
# print(pets)
# pets['C'] = "Cat"
# print(pets)
# if 'd' not in pets:
#     pets['d'] = []
# pets['d'].append('Dog')
# print(pets)
# # Defaultdict can create a dictionary with default type (lists) and can append new items without overwriting existing ones
# from collections import defaultdict
# animals = defaultdict(list)
# animals['e'].append('Elephant')
# print(animals)
# animals['e'].append('Emu')
# print(animals)

# List Comprehensions

# myList = [1,2,3,4,5]
# print([2*item for item in myList])

# # List Comprehensions with filter

# myList = list(range(100))
# filteredList = [item for item in myList if item % 10 == 0]
# print(filteredList)

# # List compreshensions with functions

# myString = "My name is Steve Brent. I live in Italy"
# print(myString.split("."))
# print(myString.split())

# def CleanWord(word):
#     return word.replace(".", "").lower() # chaining functions

# print([CleanWord(word) for word in myString.split()])
# print([CleanWord(word) for word in myString.split() if len(CleanWord(word)) < 3])

# # Nested list comprehensions

# print([[CleanWord(word) for word in sentence.split()] for sentence in myString.split(".")])

## Dictionary Comprehensions

# List of tuples
AnimalList = [("A", "Aardvark"), ("B", "Bear"), ("C", "Cat"), ("D", "Dog")]
# Generating dictionary from list of tuples
animals = {item[0]:item[1] for item in AnimalList}
print(animals)
# Generating dictionary from list of tuples (alternative)
animals = {key:value for key, value in AnimalList}
print(animals)
# Restoring dictionary back to a list
print(animals.items())
print(list(animals.items()))
# Modifying list with list comprehension
print([{'letter': key, 'name': value} for key, value in animals.items()])