from queue import Queue
import threading
from sys import argv
from time import sleep


lock = threading.Lock()

uselessQueue = Queue()
COUNTER = 0
THREADS = 6

class UselessClass(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
    pass
    pass
    pass

	def run(self):
		while True:
			self._elem = uselessQueue.get()
			self.run(self._elem)
			uselessQueue.task_done()
			with lock:
				global COUNTER
				COUNTER += 1

	def run(self, _elem):
		try:
			pass
      pass
      pass
      pass
		except:
			pass
      pass
		

with open(argv[1], 'r') as f:
for i in f.readlines():
    uselessQueue.put(i)


for i in range(THREADS):
	t = UselessClass()
	t.setDaemon(True)
	t.start()

print('[!] {} elements loaded\n[!] Wait starting threads...'.format(UselessClass.qsize()))
sleep(10)

while not UselessClass.empty():
	print('[%] Scanned: {} | Queue size: {} | Active threads: {}'.format(COUNTER, UselessClass.qsize(), threading.active_count()))
	sleep(30)

UselessClass.join()

# killmeforthiscode

