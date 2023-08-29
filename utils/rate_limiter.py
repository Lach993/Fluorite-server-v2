from collections import deque
import logging
import time

class Rate_Limit:
    def __init__(self, calls_per_period, period, buffer=0, name="Rate_Limit"):
        """
        calls_per_period: int
        period: int (Must be in seconds)
        buffer (optional): float 
        
        buffer is the percentage that the rate limit will be reduced by, 
        this is to prevent the rate limit from being exceeded with high ping
        recomended 5% (0.05) if used"""

        if buffer > 1 or buffer < 0:
            logging.warning(f"Rate limit '{name}' has an invalid buffer value of '{buffer}', no buffer is used")
            buffer = 0
        
        if period <= 0:
            logging.warning(f"Rate limit '{name}' has a period less than 0, this will disable the rate limit")
            period = 0
        
        if calls_per_period < 0:
            logging.warning(f"Rate limit '{name}' has a calls_per_period less than 0, this will disable the rate limit")
            calls_per_period = 1
            period = 0

        self.name = name
        self.calls_per_period = calls_per_period
        self.period = period * (1-buffer) # in seconds
        self.calls = deque(maxlen=calls_per_period)
    
    def clear_elapsed_calls(self):
        """Removes all calls that are older than the period"""
        if self.period == 0:
            return
        
        while len(self.calls) > 0 and time.time() - self.calls[0] > self.period:
            self.calls.popleft()
        

    def __call__(self):
        """Returns True if the rate limit is not exceeded"""
        logging.debug(f"Rate limit '{self.name}' called at {time.time()} with {len(self.calls)}/{self.calls_per_period} calls")
        if self.period == 0:
            return True
        
        if len(self.calls) < self.calls_per_period:
            self.calls.append(time.time())
            logging.debug(f"Rate limit '{self.name}' passed at {time.time()} with {len(self.calls)}/{self.calls_per_period} calls")
            return True
        else:
            # if the first call is older than the period, remove it and add the new call
            if time.time() - self.calls[0] > self.period:
                self.calls.popleft()
                self.calls.append(time.time())
                logging.debug(f"Rate limit '{self.name}' passed at {time.time()} with {len(self.calls)}/{self.calls_per_period} calls")
                return True
            else:
                logging.warning(f"Rate limit '{self.name}' exceeded")
                return False
            
    def is_ready(self):
        """Returns True if the rate limit is not exceeded, does not add a call"""
        self.clear_elapsed_calls()
        return len(self.calls) < self.calls_per_period

    def time_between_call(self):
        """Returns the time between calls"""
        return self.period/self.calls_per_period


        