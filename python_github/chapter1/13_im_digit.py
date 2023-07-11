# Q13. Write a program that reads a two-digit number and calculates the sum of the digits and its reverse
Number = int(input("Please inter an integer value as a Number: "))
# im
Ones = Number % 10
# im
# Tens = int(Number/10) #traditional
# Modern : Number // 10
Tens = Number // 10
Sum = Ones + Tens
print("Reverse is: " + str(Ones) + str(Tens))
print("Sum is: " + str(Sum))
