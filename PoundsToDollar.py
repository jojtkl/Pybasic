'''Exercise 1
Write Python code that prints your name, student number and email address. An example runs of the program: Bob ST1001 bob@gmail.com'''
#print('Guruvaayoor Unnikkannan')
#print('ST1001')
#print('Guruunni@gmail.com')
'''Exercise 2 
Write Python code that prints your name, student number and email address using escape sequences.'''
print('Bob\nST1001\nbob@gmail.com')
'''Exercise 3 
Write Python code that add, subtract, multiply and divide the two numbers. 
You can use the two numbers 14 and 7. An example run of the program: 14 + 7 = 21 14 * 7 = 98 14 – 7 = 7 14 / 7 = 2'''
'''A=7
B=14
print(f'sum={A+B}')
print(f"Substraction={A-B}")
print(f'Multiplication={A*B}')
print(f'Division={A/B}')'''

'''Exercise 4 
Write Python code that displays the numbers from 1 to 5 as steps.'''
#print('1\n2\n3\n4\n5')

'''Exercise 5 
Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen: '''
print('\"SDK\" stands for \"Software Development Kit\", whereas \n\"IDE\" stands for \"Integrated Development Environment\" ')
'''Exercise 6 
Practice and check the output'''
#print("python is an \"awesome\" language.")
#print("python\n\t2023")
#print('I\'m from Entri.\b')
#print("\65")
#print("\x65")
#print("Entri", "2023", sep="\n")
#print("Entri", "2023", sep="\b")
#print("Entri", "2023", sep="*", end="\b\b\b\b")


'''Exercise 7 
Define the variables below. Print the types of each variable. What is the sum of your variables? '''

'''Integer=61
print(type(Integer))
String="61"
print(type(String))
Decimal=91.3
print(type(Decimal))'''

'''Exercise 8 
calculate the number of minutes in a year using variables for each unit of time. print a statement that describes what your code does also. Create three variables to store no of days in a year, minute in a hour, hours in a day, then calculate the total minutes in a year and print the values (hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour'''

'''No_days=365
Hrs_day=24
Min_hr=60
print(f'Total minutes in an year is "{ No_days*Hrs_day*Min_hr}"')'''
'''Exercise 9 
Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting. An example runs of the program: Please enter you name: Tony Hi Tony, welcome to Python programming :)'''

'''X=input('Enter your Name :')
print(f'Hi {X}, welcome to Python programming')'''

'''Exercise 10 
Name your file: PoundsToDollars.py Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($) An example runs of the program: Please enter amount in pounds: XXX £ XXX are $ XXX'''
Pounds=float(input('Please Enter the Amount In Pounds:'))
Exchange_Rate=Pounds*1.33
print (f'£{Pounds} is ${Exchange_Rate}' )

