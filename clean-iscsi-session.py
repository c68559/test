import subprocess
import os
from pprint import pprint as pp
'''
   remove all sessions at once
'''
cmd = ['/usr/sbin/iscsiadm', '-m', 'session']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o, e = p.communicate()

SESS = [[s.split()[2].split(',')[0], s.split()[3]] for s in o.split('\n') if s.__contains__('tcp') ]

for c in SESS:
    cmdline = 'iscsiadm --m node -T ' + c[1] + " --portal " + c[0] + ' -u'
    pp(cmdline)
    os.system(cmdline)
    cmdline = 'iscsiadm --m node -T ' + c[1] + " --portal " + c[0] + ' -o delete'
    pp(cmdline)
    os.system(cmdline)
 

