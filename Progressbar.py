import time
import sys
import os
import random
import numpy as np

def _print(string):
    sys.stdout.write(string)
    sys.stdout.flush()

def s_print(string, sleep_time_min = 0.1, sleep_time_max = 0.1):
    for i in string:
        st = random.uniform( abs ( sleep_time_min ), abs ( sleep_time_max ) )
        _print(i)
        time.sleep(st)

char_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !.,;:"
char_list = list( char_list )

text = np.random.choice(char_list, size = 50)

s_print(text, 0.0, 0.0)
print('\n')

os.system('cls')

xm = 0
n = 1
x_min = 0
x_max = 50
x = x_min
while ( x <= x_max):
    if ( n % 4 == 0 ):
        w = '(  '
    if ( n % 4 == 1 ):
        w = ' | '
    if ( n % 4 == 2 ):
        w = '  )'
    if ( n % 4 == 3 ):
        w = ' | '
    xp = int( ( ( x - x_min ) / ( x_max - x_min ) * 100) )
    xm = int( xp / 10 )
    n += 1
    b = ("Progress: " + w + " "  + "!" * xm + " " + str( xp ) +  "% ")
    sys.stdout.write( '\r' + b )
    time.sleep(random.uniform(0.1, 1.0))
    x += random.uniform(0.1, 2.0)

sys.stdout.write( '\r' + " " * len( b ) )
b = ("Progress: " + "Done!" )
sys.stdout.write( '\r' + b )
time.sleep(1.0)
