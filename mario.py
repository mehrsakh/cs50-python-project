

from cs50 import get_int
# import cs50

h = get_int("height : ")

while h < 1 or h > 8:
    h = get_int("height : ")


for i in range(1, h+1):
    print(" " * (h - i) + "#" * i)
