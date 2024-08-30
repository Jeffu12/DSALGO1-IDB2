'''
Exercise 1
'''
nintendoWii = 100
userMoney = float(input("Enter amount of your money:"))
print ("You have " , userMoney, " amount of money!")
print ("You can buy ", int(userMoney/nintendoWii), " piece/s of Nintendo Wiis!")
add = nintendoWii-(userMoney%nintendoWii)
print ("You need another: ", add, " amount of money to buy additional Nintendo Wii")

'''
Excercise 2
'''
print("")
fact = 1
input0 =  int(input("Enter number for factorial: "))
for a in range (1, input0 + 1):
    fact = fact * a
print (fact, " is the factorial of your number")

'''
Exercise 3
'''
print("")
factor = []
input1 = int(input("Enter number to show factor: "))
for x in range (1, input1+1):
    if input1 % x == 0:
        factor.append(x)
print("The factors of ", input1, " is " , factor)