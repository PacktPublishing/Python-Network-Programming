import datetime
from threading import Thread

def checksequential():
    for x in range(1,10):
        print (datetime.datetime.now().time())

def checkparallel():
    print (str(datetime.datetime.now().time())+"\n")


checksequential()

print ("\nNow printing parallel threads\n")
threads = []
for x in range(1,10):
    t = Thread(target=checkparallel)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
