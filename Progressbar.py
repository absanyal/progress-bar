import time
import sys
import os
import random

def _print(string):
    sys.stdout.write(string)
    sys.stdout.flush()

def s_print(string, sleep_time_min = 0.1, sleep_time_max = 0.1):
    for i in string:
        st = random.uniform( abs ( sleep_time_min ), abs ( sleep_time_max ) )
        _print(i)
        time.sleep(st)


text = "Some random stuff"

s_print(text)
print('\n')

os.system('cls')

xm = 0
n = 1
x_min = 0
x_max = 15
x = x_min
while ( x <= x_max):
    if ( n % 4 == 0 ):
        w = '/'
    if ( n % 4 == 1 ):
        w = '-'
    if ( n % 4 == 2 ):
        w = '\\'
    if ( n % 4 == 3 ):
        w = '|'
    xp = int( ( ( x - x_min ) / ( x_max - x_min ) * 100) )
    xm = int( xp / 5 )
    n += 1
    b = ("Progress: " + w + " "  + "#" * xm + " " + str( xp ) +  "% ")
    sys.stdout.write( '\r' + b )
    time.sleep(random.uniform(0.1, 1.0))
    x += random.uniform(0.1, 2.0)

sys.stdout.write( '\r' + " " * len( b ) )
b = ("Progress: " + "Done!" ) #+ " "  + "#" * ( xm + 1 ) + " " + str( 100 ) +  "% ")
sys.stdout.write( '\r' + b )
