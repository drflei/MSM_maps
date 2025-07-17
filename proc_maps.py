import os
import shutil
import subprocess

os.chdir('/home/flei/onedrive/magcos-runs/rigidity/450')
#dirs = ('2030','2025','2020','2015','2010','2005','2000','1995','1990','1985','1980','1975','1970','1965','1960','1955')
dirs = ('2020',)
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
    with open(file, 'w') as f:
        f.writelines(new_lines)
    return 

for dir in dirs:
    for directory, dirnames, fileList in os.walk(dir):
        for fi in fileList: 
            if (not fi.endswith('.out')) or fi.startswith('nohup'):
                continue
            file = directory+'/'+fi
            preprocfile(file)
            year = dir
            kp = file.split('-')[0][-1]
            ut = file.split('-')[-1].split('.')[0][2:]
            cmd = f"/home/flei/MSM_maps/premap {year} {kp} {ut:0>2} {file}"
            outfile = f"AVKP{kp}T{ut:0>2}.AVG"
            subprocess.run(cmd, shell=True)
            shutil.move(f"/home/flei/onedrive/magcos-runs/rigidity/450/{outfile}",f"/home/flei/MSM_maps/{year}/{outfile}")
            #plotmapfile(file)
os.chdir('/home/flei/MSM_maps')
