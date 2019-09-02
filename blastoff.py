## Countdown from inputted with a 1 second delay on print

import time

countDown = int(input("Pick a number to start the BlastOff Counter!: "))
while countDown > 20: 
    countDown = int(input("Pick a number less then 20: "))
while countDown < 20:
    while (countDown >= 1):
        print(countDown)
        countDown = countDown - 1
        time.sleep(1)
        if countDown == 0:
            print("Blastoff!!!")
            break
    break