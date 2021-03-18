import sys
import deepdish as dd
import subprocess as sp

filee = sys.argv[1]
out_file = "edited." + filee

data = dd.io.load(filee)

#print(data)
#print(type(data))
#for k in data.keys():
#    data[k]['borealis_git_hash'] = 'v0.6'


for i,k in enumerate(data.keys()):
    new = {}
    new[k] = data[k]
    new[k]['borealis_git_hash'] = 'v0.6'

    if i == 0:
        dd.io.save(out_file, new)
    else:
        dd.io.save('tmp', new)
        cmd = 'h5copy -i tmp -o {} -s {} -d {}'.format(out_file, k, k)
        sp.check_output(cmd, shell=True)

