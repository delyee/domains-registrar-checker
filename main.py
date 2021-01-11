from queue import Queue
import threading
from sys import argv
from time import sleep as time_sleep
from whois import query
from random import choice as random_choice
#from whois.exceptions import UnknownTld, WhoisCommandFailed


lock = threading.Lock()
uselessQueue = Queue()
COUNTER = 0
THREADS = int(input('[Threads] press Enter(6) or type 32 :> ') or 6)
REGISTRAR = input('[Registrar] press Enter(RU-CENTER) or type REG-RU :> ') or 'RU-CENTER'
GOODS, BADS = [], []


class UselessClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            self._elem = uselessQueue.get()
            self.scanner(self._elem)
            uselessQueue.task_done()
            with lock:
                global COUNTER
                COUNTER += 1

    def scanner(self, _elem):
        try:
            __rec_counter = 1
            # todo: custom whois.CACHE_FILE, query(cache_file=None)
            _ = query(_elem.strip(), force=0, slow_down=random_choice([1,2]))

            while _ == None and __rec_counter < 3:
                __rec_counter += 1
                _ = query(_elem.strip(), force=1, slow_down=random_choice([3,4])) # 5,6,7

            # 'RU-CENTER-RU' of responce != 'RU-CENTER' in user input
            if REGISTRAR in _.__dict__.get('registrar'):
                with lock:
                    GOODS.append(_elem)
            else:
                pass
                #print('Bad registrar:', _.get('registrar'), _elem)

        # (UnknownTld, WhoisCommandFailed)
        except Exception as e:
            with lock:
                BADS.append(_elem)
            pass

with open(argv[1], 'r') as __:
    for _ in __.readlines():
        uselessQueue.put(_)

print('[!] {} domains loaded\n[!] Wait starting threads...'.format(uselessQueue.qsize()))

for _ in range(THREADS):
    __ = UselessClass()
    __.setDaemon(True)
    __.start()


try:
    while not uselessQueue.empty():
        print('[%] Processed: {} | Queue size: {} | Active threads: {}'.format(COUNTER, uselessQueue.qsize(), threading.active_count()-1))
        time_sleep(5)
    uselessQueue.join()

except KeyboardInterrupt:
    pass

finally:
    with open('goods.txt', 'w') as goods_file:
        goods_file.writelines(GOODS)
    with open('bads.txt', 'w') as bads_file:
        bads_file.writelines(BADS)
    
    print('[+] Len of success domains:', len(GOODS))

# killmeforthiscode ._.