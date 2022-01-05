import winsound
from random import randrange

frequency = randrange(5000)
duration = randrange(30000)
winsound.Beep(frequency, duration)

