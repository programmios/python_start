# Q33. if input = 12345
# output = 1   2   3   4   5
number = int(input("Please enter an integer 5-digit as a value: "))
digit0 = number % 10
digit1 = (number // 10) % 10
digit2 = (number // 100) % 10
digit3 = (number // 1000) % 10
digit4 = (number // 10000) % 10
print("   " + str(digit4) + "   " + str(digit3) + "   " +
      str(digit2) + "   " + str(digit1) + "   " + str(digit0))
