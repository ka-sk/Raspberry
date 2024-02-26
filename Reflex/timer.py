import time

class Timer:
    
    def __init__(self):
        self.init_time = time.perf_counter()
        self.times = []
        
    def start(self):
        self.init_time = time.perf_counter()
        
    def stop(self):
        self.times.append(time.perf_counter()-self.init_time)
        return self.times[-1]
        
    def all(self):
        return self.times
    
    def set_init_time(self, x):
        self.init_time = x
        
    def not_passed(self, sec):
        return True if self.init_time + sec > time.perf_counter() else False
