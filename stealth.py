import random
import time

def stealth_delay(strategy ="normal"):
    """This is made to introduce a form of delay while scanning."""
    if strategy == "normal":
        delay = random.uniform(0.5,2.0)
    elif strategy == "offensive":
        delay = random.uniform(0.1,0.5)
    elif strategy == "paranoia":
        delay = random.uniform(2.0, 5.0)
    elif strategy == "progressive":
        delay = random.choice([random.uniform(0.1,0.5), random.uniform(2.0,5.0)])
    else:
        delay = random.uniform(0.5,2.0)

    time.sleep(delay)
    return delay
