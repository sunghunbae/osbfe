import os
for i in range(0,2):
    os.system('qsub -t 1-80:1 jobscript{0}'.format(i))
