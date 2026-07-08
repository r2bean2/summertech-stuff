from random import randint
import os
import subprocess
import ast
import io
from pyflakes import api
from pyflakes import reporter
def check_vaild(code_string):
    warning_stream = io.StringIO()
    error_stream = io.StringIO()
    rep = reporter.Reporter(warning_stream, error_stream)
    api.check(code_string, "<mutation_string>", rep)
    syntax_errors = error_stream.getvalue()
    name_warnings = warning_stream.getvalue()
    print(name_warnings)
    print(syntax_errors)
    # 1. Catch absolute structural failures (SyntaxError)
    if syntax_errors:
        return False
        
    # 2. Catch typos like 'randi*nt' (UndefinedName)
    elif "undefined name" in name_warnings:
        return False
        
    else:
        return True
if not os.path.exists("index.txt"):
    with open("index.txt", "w") as file:
        file.write("1")
    index=1
else:
    with open("index.txt", "r") as file:
        index=int(file.read())
print(index)
old_index= index-1
file_path="evolve"+str(index)+".py"
while True:
    vaild_charecters = [ chr(i) for i in range(32, 127)]
    char_add = vaild_charecters.pop(randint(0,len(vaild_charecters)-1))
    print(char_add)
    with open("evolve" + str(old_index) + ".py", "r") as file:
        py_file=file.read()
    cut_point=randint(0,len(py_file))
    py_file = py_file[:cut_point] + char_add + py_file[cut_point:]
    try:
        ast.parse(py_file)
        if check_vaild(py_file):
            break
    except SyntaxError:
        continue

with open("evolve" + str(index) + ".py", "w") as file:
    file.write(py_file)
    






with open("index.txt", "w") as file:
    file.write(str(index + 1 ))