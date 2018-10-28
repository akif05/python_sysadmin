from time import sleep
from signal import *
# SIGHUB turns debug printing on and off
debug = False
def sighup_handler(signum, frame):
    global debug
    debug = not debug

signal(SIGHUP, sighup_handler)

# SUGUSER1 report current status
def report_status(signum, frame):
    global primes_list
    print("found %d primes so far" % len(primes_list))

signal(SUGUSR1, report_status)

signal(SUGINT, SIG_IGN)
signal (SIGQUIT, SIG_IGN)
signal (SIGTERM, SIG_IGN)


n = 1
primes_list = []

while True:
    if isprime(n):
        if debug:
            printf("%d is prime" % n)
        primes_list.append(n)
    n += 1

