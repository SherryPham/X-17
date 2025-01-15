### THE VIRUS STARTS HERE ###

import sys
import glob

code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virus_area = False

for line in lines:
    if lines == '### THE VIRUS STARTS HERE ###':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### THE VIRUS ENDS HERE ###':
        break

python_scripts = glob.glob('*.py')

print(python_scripts)


### THE VIRUS ENDS HERE ###
