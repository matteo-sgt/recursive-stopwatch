import time
import datetime

now = datetime.datetime.now()

ymd = datetime.datetime.strftime(now, "%Y-%m-%d")

start_time = str(ymd) + " 14:59:30"
t = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")

def stopwatch(seconds):
    start = time.time() - 1
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print ("loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed) )
        time.sleep(1)
         
while True:
    time.sleep(1)
    if(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) == str(t)):
        while True:
            stopwatch(36)
            print("\n")
