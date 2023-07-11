# Q16. Input an integer (n) and computes the value of n+nn+nnn
n = int(input("Please enter an integer value as a n: "))
nn = str(n) + str(n)
nnn = str(nn) + str(n)
print(n + int(nn) + int(nnn))
