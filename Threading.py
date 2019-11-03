import threading
import time

class MyThread(threading.Thread):
	def __init__(self,name):
		super().__init__()
		self.name = name

	def run(self):
		threadLock.acquire()
		print("hello from", self.name)
		threadLock.release()
		time.sleep(2)	#sleep to simulate a large computation
		threadLock.acquire()
		print("goodbye from", self.name)
		threadLock.release()
# thread1 = MyThread("Thread1")
# thread2 = MyThread("Thread2")

# thread1.start()
# thread1.join()

# thread2.start()
# thread2.join()
threadLock = threading.Lock()
threadList = []

for i in range(100):
	tempThread = MyThread("Thread " + str(i))
	threadList.append(tempThread)

for thread in threadList:
	thread.start()

for thread in threadList:
	thread.join()