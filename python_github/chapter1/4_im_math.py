# Q4. Calculate the area of a regular polygon
# p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
# incorrect5 # import math was not written
import math
# OR         #from math import tan
PI = 3.14
n_sides = int(input("please enter an integere value as a n_sides : "))
s_length = float(input("Please enter a float vlaue as a s_length: "))
# p_area = n_sides * (s_length ** 2) / (4 * tan(PI / n_sides)) #incorrect6 #tan is wrong... math.tan is true
p_area = n_sides * (s_length ** 2) / (4 * math.tan(PI / n_sides))
print("p-area is a : ", p_area)
