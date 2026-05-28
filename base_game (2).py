#Isla Hudecek and Sasha
#Base Game
#Create the basic version of the game. The computer chooses a random number, and players guess until they get it right.
# Add tension: a 5-guess limit and Hot/Warm/Cold hints
#Upgrade the game with three difficulty modes. Each diffcuty expands the range of the secret number.

#initalize
import time
import random



#Function



def main():
    name = input ('Pleas Enter your Username: ')
    print ('Welcome to Guess the NUMBER')
    time.sleep(1)
    print ('Here is how it works')
    time.sleep(1)
    print('We have a number you have to guess, BUT you have to do it in 5 tries')
    print("Depending on your time, you will get points. DON'T RUN OUT")
    level=input("Would you like to play easy(range of 1 to 10), medium(range of 1 to 20), or hard(range of 1 to 30)?: ")
    if level.lower() == "easy":
        start_time=time.time()
        num = random.randint(1,10)
        i=0
        while i<5:
            check= int(input('Your guess: '))
            if check != num:
                if check==num+2 or check==num-2:
                    print ("Warmer")
                elif check==num+1 or check==num-1:
                    print ("Hot")
                else:
                    print ("Colder")
                i=i+1
                continue
            elif check == num:
                print ('You got it!')
                break
        if i >=6:
            print("You lose play again")
        end_time=time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        if elapsed_time <= 10:
            print("50 points")
        elif elapsed_time <= 20:
            print("25 points")
        elif elapsed_time <= 30:
            print("10 points")
        elif elapsed_time >= 30:
            print("Sorry 0 points")
    elif level.lower() == "medium":
        start_time=time.time()
        num = random.randint(1,20)
        i=0
        while i<5:
            check= int(input('Your guess: '))
            if check != num:
                if check==num+2 or check==num-2:
                    print ("Warmer")
                elif check==num+1 or check==num-1:
                    print ("Hot")
                else:
                    print ("Colder")
                i=i+1
                continue
            elif check == num:
                print ('You got it!')
                break
            if i >=6:
                print("You lose play again")
        end_time=time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        if elapsed_time <= 10:
            print("50 points")
        elif elapsed_time <= 20:
            print("25 points")
        elif elapsed_time <= 30:
            print("10 points")
        elif elapsed_time >= 30:
            print("Sorry 0 points")

    elif level.lower() == "hard":
        start_time=time.time()
        num = random.randint(1,30)
        i=0
        while i<5:
            check= int(input('Your guess: '))
            if check != num:
                if check==num+2 or check==num-2:
                    print ("Warmer")
                elif check==num+1 or check==num-1:
                    print ("Hot")
                else:
                    print ("Colder")
                i=i+1
                continue
            elif check == num:
                print ('You got it!')
                break
        if i >=6:
            print("You lose play again")
        end_time=time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        if elapsed_time <= 10:
            print("50 points")
        elif elapsed_time <= 20:
            print("25 points")
        elif elapsed_time <= 30:
            print("10 points")
        elif elapsed_time >= 30:
            print("Sorry 0 points")

#Main
main()
