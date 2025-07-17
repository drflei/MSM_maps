import os
import shutil
import subprocess

os.chdir('/home/flei/onedrive/magcos-runs/rigidity/450')
dirs = ('2015',)

def preprocfile(file):
    # Preprocess the file to prepare it for mapping, i.e., replace Null values with 0 or the average of the values before and after in the column.
    with open(file, 'r') as f:
        lines = f.readlines()
    new_lines = []
    for i in range(len(lines)):
        if not lines[i][0].isalnum() and not lines[i].startswith('-'):
            print(lines[i])
            while not lines[i][0].isalnum() and not lines[i].startswith('-'):
                #print(lines[i][1:])
                lines[i] = lines[i][1:]
            aa = lines[i-1].split()
            bb = lines[i].split()
            add_line = [(float(a) + float(b)) / 2 if a != 'NUL' and b != 'NUL' else '0' for a, b in zip(aa, bb)]
            aline = "".join(f"{num:.4e}\t" for num in add_line)
            new_lines.append(aline+ '\n') 
            print(new_lines[-1])
        new_lines.append(lines[i])
    with open("test.txt", 'w') as f:
        f.writelines(new_lines)
    return 

file = '/home/flei/onedrive/magcos-runs/rigidity/450/2015/WorldMapKp7-Ut3.out'
preprocfile(file)
