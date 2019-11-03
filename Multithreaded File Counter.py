import threading
import time
from os import listdir
from os.path import isfile, join

# print(os.listdir())

# class MyThread(threading.Thread):
	

# 	def __init__(self,name):
# 		super().__init__()
# 		self.name = name

	# def run(self):
	# 	threadLock.acquire()
	# 	fileList = getFiles()
		
		# for file in fileList
		# 	if file is folder:
		# 		newThread.start()
		# 	else:
		# 		fileCount += 1
	# run(self)		


		# print("hello from", self.name)
		# threadLock.release()
		# time.sleep(2)	#sleep to simulate a large computation
		# threadLock.acquire()
		# print("goodbye from", self.name)
		# threadLock.release()


# thread1 = MyThread("Thread1")
# thread2 = MyThread("Thread2")

# thread1.start()
# thread1.join()

# thread2.start()
# thread2.join()

rootPath = "C:/Users/joelc"
fileCount = 0

def getFiles(fileCount, path):
	print(os.path.listdir(path))
	
	for file in os.listdir(path):
		try: 
			if os.path.isfile(file):
				print("yes")
				path = path+file
				getFiles(fileCount,path)

			else:
				fileCount+=1
				# print("file"+str(fileCount))
				# print(file)
		# except FileNotFoundError:
			# continue
		except OSError:
			continue
		
	print(fileCount)


getFiles(fileCount, rootPath)

		# for i in range(100):
		# 	tempThread = MyThread("Thread " + str(i))
		# 	threadList.append(tempThread)

		# for thread in threadList:
		# 	thread.start()

		# for thread in threadList:
		# 	thread.join()