
#init
import random
import time
finish_line=50
tortoise_pos=0
hare_pos=0
is_hare_asleep= False # Hare startes awake

hare_win=[]
tortoise_win=[]

#Functions
for i in range (100000):
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
        #print (f' The tortioses possition is {tortoise_pos} meters 🐢')
        #print (f'The Hares possition is {hare_pos} meters 🐇')

    if tortoise_pos >= finish_line:
        tortoise_win.append("Win!")
        print("🐢 The Tortoise wins!")

    else:
        print("🐇 The Hare wins!")
        hare_win.append("WIN!")

print(f"The Tortoise won {len(tortoise_win)} races")
print(f"The Hare won {len(hare_win)} races")




