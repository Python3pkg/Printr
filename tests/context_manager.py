from printr import EllipsisPrintr
from time import sleep

with EllipsisPrintr('Printing') as p:
    for i in range(30):
        p.update()
        sleep(0.1)
