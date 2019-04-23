from datetime import datetime
from pprint import pprint as pp
dd = []
logfile = "perf.log"
KeyWords = "execution of poll_system"
with open(logfile, 'r') as file:
    for line in file:
        if line.__contains__(KeyWords):
            tt = line[0:16]
            try:
                test = dd.index(tt)
            except ValueError:
                dd.append(tt)
            else:
                pass


TimeStamp = [datetime.strptime(d, "%Y-%m-%d %H:%M") for d in dd]
GapAllowed = 1
for i in range(1, len(TimeStamp)):
    diff = (TimeStamp[i] - TimeStamp[i-1]).seconds/60
    if diff != GapAllowed: print("line{0}: {1} ~ {2}".format(i-1, TimeStamp[i-1], TimeStamp[i])) 
