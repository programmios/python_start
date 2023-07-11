# Q2. Calculate surface volume and area of ​​a cylinder
# Constant PI
# define PI #incorrect2
PI = 3.14
R = float(input("Please enter a float value as a Radius: "))
H = float(input("Please enter a float value as a Height: "))
# volume = PI * (R ^ 2) * H #incorrect3 (^=**)
volume = PI * (R ** 2) * H
sur_area = ((2*PI*R) * H) + ((PI*R**2)*2)
# print("volume is a :  ", volume + "\n sur_area is a : ", sur_area) #incorrect4
print("volume is a : " + str(volume) + "\n sur_area is a : " + str(sur_area))
