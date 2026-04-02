import time
import random

def random_delay(min_s, max_s):
    delay = random.randint(min_s, max_s)
    print(f"Sleeping for {delay}s")
    time.sleep(delay)