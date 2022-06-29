# swap two number

'''no1 = int(input("Enter Your First Number: "))
no2 = int(input("Enter Your Second Number: "))
swap = no1
no1 = no2
no2 = swap
print("The Value Of no1 after swapping: {}".format(no1))
print("The Value Of no2 after swapping: {}".format(no2))'''

# another method we can use
'''x = int(input("Enter first value: "))
y = int(input("Enter Second value: "))

x,y = y,x
print("First Value After Swapping {}".format(x))
print("Second Value After Swapping {}".format(y))'''

# Program to check whether a number is even or odd

'''class check_even_odd:
    def even(self):
        no = int(input("Enter Your Number: "))
        if no % 2 == 0:
            print("You Entered Even Number {}".format(no))
        else:
            print("You Entered Odd Number {}".format(no))


output = check_even_odd()
output.even()'''

# print even and odd no till 50
'''class check_even_odd:
    
    def even_odd(self):
        no = 0
        while no < 50:

            no = no + 1
            if no % 2 == 0:

                print("Even Number: {}".format(no))

            elif no % 2 != 0:

                print("Odd Number: {}".format(no))


output = check_even_odd()
output.even()'''

# Program to get Quotient And Remainder Calculator

'''class calculator:
    def quotient_remainder(self):
        n1 = int(input("Enter Dividend: "))
        n2 = int(input("Enter Divisor: "))

        quotient = n1 / n2
        print("Quotient: ", quotient)
        remainder = n1 % n2
        print("Remainder: ", remainder)


output = calculator()
output.quotient_remainder()'''

# Program to check Alphabet is vowel or consonant

'''class alphabet:
    def vowel_consonant(self):
        alp = input("Enter Your Alphabet: ")

        if alp == 'A' or alp == 'a' or alp == 'E' or alp == 'e' or alp == 'I' \
                or alp == 'i' or alp == 'O' or alp == 'o' or alp == 'U' or alp == 'u':
            print(" {} is Vowel. ".format(alp))
        else:
            print("{} is Consonant. ".format(alp))


output = alphabet()
output.vowel_consonant()'''


# Program to find largest among three numbers

'''class largest:
    def among_three(self):
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
        num3 = int(input("Enter Third Number: "))

        if num1 >= num2 and num1 >= num3:
            largest = num1
        elif num2 >= num1 and num2 >= num3:
            largest = num2
        else:
            largest = num3
            print("Largest Among Three Numbers Are: ", largest)


output = largest()
output.among_three()'''