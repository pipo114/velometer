import RPi.GPIO as g
from time import sleep

GPIO_VELO=2
GPIO_FORWARD=12
SLEEP=0.1

g.setmode(g.BCM)
g.setup(GPIO_VELO, g.IN, pull_up_down=g.PUD_UP)
g.setup(GPIO_FORWARD, g.OUT)

revcount = 0
previous_state= 0

while True: 
    #print("GPIO: " +str(g.input(GPIO_VELO)))
    #print("previous_state=" + str(previous_state))
    if g.input(GPIO_VELO) == 1:
        if previous_state == 0:
            revcount +=1
            print(revcount)
            g.output(GPIO_FORWARD, 0)
            sleep(SLEEP)
            g.output(GPIO_FORWARD, 1)
            sleep(SLEEP)
    previous_state=g.input(GPIO_VELO)
