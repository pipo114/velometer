import RPi.GPIO as g
from time import sleep

GPIO_VELO=27
GPIO_FORWARD=6
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
            print(f"port {GPIO_FORWARD}:"+str(g.input(GPIO_FORWARD)))
            sleep(SLEEP)
            g.output(GPIO_FORWARD, 1)
            print(f"port {GPIO_FORWARD}:"+str(g.input(GPIO_FORWARD)))
            sleep(SLEEP)
    previous_state=g.input(GPIO_VELO)
        
