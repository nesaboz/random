'''
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''
import time


def scheduler(f, n):
    '''
    f (function): to execute
    n (float): ms delay
    '''
    time.sleep(n / 1000.0)
    print('waiting')
    return f


# print(scheduler(sum, 10)([4,5]))


from time import sleep
import threading


class Scheduler:
    def __init__(self):
        self.fns = []  # tuple of (fn, time)
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000
            for fn, due in self.fns:
                if now > due:
                    fn()
            self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
            sleep(0.01)

    def delay(self, f, n):
        self.fns.append((f, time() * 1000 + n))


a = Scheduler()
a.fns = [(lambda: sum(4, 5), 10)]
