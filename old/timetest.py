from datetime import datetime as dt

def randnum(low,high):
    return dt.now().microsecond%(high+1-low)+low

def choice(mlist):
    return mlist[randnum(0,len(mlist)-1)]

while True:
    print(choice(['jack','sam','robert','candice','jason']))
