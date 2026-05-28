#The Legend

#init
import random
import time
finish_line=50
tortoise_pos=0
hare_pos=0
is_hare_asleep= False # Hare startes awake

#Functions
for i in range (100):
    finish_line=50
    tortoise_pos=0
    hare_pos=0
    is_hare_asleep= False # Hare startes awake

    while tortoise_pos< finish_line and hare_pos<finish_line:
        tortoise_pos=tortoise_pos + random.randint(1,3)# Tortoise always moves a short distance between 1 - 3 meters at random
        sleep= random.randint(1,10)# Hare has a 30% chance of falling a sleep for a turn
        if sleep <4:
            is_hare_asleep= True
            hare_pos=hare_pos+0

        elif sleep > 3:
            is_hare_asleep= False
            hare_pos= hare_pos + random.randint(1,10)
        print (f' The tortioses possition is {tortoise_pos} meters 🐢')
        print (f'The Hares possition is {hare_pos} meters 🐇')

    if tortoise_pos >= finish_line:
        time=time.sleep(2)
        print("🐢 The Tortoise wins!")
    else:
        print("🐇 The Hare wins!")


# If Hare is awake, it will move 1 - 10 meters at random

# Print the positions of the Hare and Tortoise after each round

