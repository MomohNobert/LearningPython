import threading

class NobertsMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = NobertsMessenger(name='Send out messages.')
y = NobertsMessenger(name='Receive messages.')
x.start()
y.start()