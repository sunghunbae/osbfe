import os
for i in range(0,12):
    os.system('qsub jobscript{0}'.format(i))
