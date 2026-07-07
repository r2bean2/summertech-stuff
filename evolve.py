from random import *
import os
index=1
old_index= index-1
file_path="evolve"+index+".py"
vaild_charecters = [ chr(i) for i in range(32, 127)]
print(vaild_charecters)
char_add = vaild_charecters.pop(randint(0,len(vaild_charecters)))
print(char_add)
with open("evolve" + old_index + ".py", "r") as file:
    file=file.read()