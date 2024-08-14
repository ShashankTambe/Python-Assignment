# Q1. Write a Python program that prints "Hello, World!" to the console.

print("Hello, World!") #prints Hello, World! onto the terminal

# Q2. Create variables to store your name, age, and favorite hobby. Print these variables.

name = "Shashank"                                                         #creates a variable named "name" and assigns a string value Shashank
age = "21"                                                                #creates a variable named age and assigns a string value 21
fav_hobby = "Gaming"                                                      #creates a variable named fav_hobby and assigns a string value Gaming
print("Name: " +name + "\nAge: " +age +"\nFavorite Hobby: " +fav_hobby)   #prints all the values on next line using \n

# Q3. Add comments to your code explaining what each line does.

# Q4. Write a Python program that takes an integer input from the user and prints whether the number is positive, negative, or zero.

n = int(input("Enter any whole number :"))  #input from user
if (n > 0):                                 #start of if statement, checks if n > 0, if yes then
    print("Positive Number")                    #prints "Positive Number"
elif (n < 0):                               #checks if n < 0, if yes, then
    print("Negative Number")                    #prints "Negative Number" 
else:                                       #last case i.e n == 0
    print("Zero")                               #prints zero if given number is not positive or negative

# Q5. Create a program that checks if a given year is a leap year.
y = int(input("Enter any year: "))          #input from user
if (y % 400 == 0 and y % 100 == 0):         #start of if statement, checks if given year if div by 400 and 100
    print("Leap year")                          #if yes then prints Leap year
elif (y % 4 == 0 and y % 100 != 0):         #checks if y is div by 4 and not div by 100
    print("Leap year")                          #prints leap year
else:                                       #last case where y is odd or isnt divisible by 4
    print("Not a leap year")                    #prints not a leap year

# Q6. Write a Python program to print the first 10 natural numbers using a for loop.

n = 1                                       #initialize n = 1
print("Natural number till 10: ")           #just a print statement 
for n in range(0, 10):                      #start of loop which starts at 0 and end on 10
    n += 1                                      #incrementing n by 1
    print(n)                                    #printing n

# Q7. Create a program that prints the multiplication table of a given number using a while loop.

n = int(input("Enter any number :"))        #input from user
i = 1                                       #initialize i to 1
while i <= 10:                              #start of while loop, give condition i<=10
    temp = n * i                                #declare a temporary var temp which stores the value n multiplied by i
    print(temp)                                 #printing temp
    i += 1                                      #incrementing i by 1

# Q8. Write a Python program that iterates through numbers 1 to 10 and prints each number. Use the continue statement to skip numbers that are divisible by 3.

for n in range(0, 11):                      #giving the range of number in which loop should run
    if n % 3 == 0:                          #condition that if n is divisible by 3 
        continue                                #then continue to else
    else:                                   #other case than if
        print(n)                                #printing n

# Q9. Create a program that stops printing numbers when it encounters a number greater than 5 using the break statement.

INput = input("Enter numbers seperated with commas, no space: ")        #input from user
numbers = [int(num) for num in INput.split(',')]                        #converting each input from string to integer type
for n in numbers:                                                       #start of for loop
    if n > 5:                                                               #condition of if value of n is more than 5
        break                                                                   #using break statement
    else:                                                                   #other case than if
        print(n)                                                                #printing n

# Q10. Define a function called greet that takes a name as an argument and prints "Hello, [name]!".

name = input("Whats your name?: ")          #input from user
def greet(name):                            #using keyword "def" and naming our function greet with an argument named "name"
    print(f"Hello, {name}!")                    #using the f"" for printing the name 
greet(name)                                 #calling the function

# Q11. Create a function that takes two numbers as arguments and returns their sum.

a = int(input("Enter any number :"))        #first value
b = int(input("Enter any number :"))        #second value
def sum(a, b):                              #using keyword "def" and naming our function sum with two arguments a and b
    c = a + b                                   #temporary variable c to store the sum of a and b
    print("Sum: " +str(c))                      #printing c by converting it to string first
sum(a, b)                                   #calling the function