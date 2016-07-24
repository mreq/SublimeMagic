import time, threading

# taken from http://stackoverflow.com/a/34388942/910868

class Messenger(object):
    def __init__(self):
        self.timeout = 1
        self.view = self.timer = None

    def message(self, view, msg, overwrite):
        self.cancel_timer()
        self.view = view
        if overwrite:
            self.view.set_status('SublimeMagic', msg+'\n')
        else:
            self.view.set_status('SublimeMagic', msg)
        self.start_timer()

    def cancel_timer(self):
        if self.timer != None:
            self.timer.cancel()

    def start_timer(self):
        self.timer = threading.Timer(self.timeout, self.clear)
        self.timer.start()

    def clear(self):
        self.view.erase_status('SublimeMagic')
