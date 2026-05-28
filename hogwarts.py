#Isla Hudecek
#Hogwarts Challeng 3

#Init
import time
import random
#Function
def main():
    print ('Welcome to Hogwarts!')
    name= input('What is your name?: ')
    time.sleep(1)
    print('..')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('....')
    print(f'Your House is {house(name)}')


def house(x):
    if x =='Harry'or x =='Hermione'or x =='Ron':
        return 'Gryffindor'
    elif x =='Newt' or x== 'Nyphadora' or x== 'Pamona':
        return 'Hufflepuff'
    elif x=='Luna' or x== 'Cho' or x== 'Filius':
        return 'Ravenclaw'
    elif x=='Voldemort' or x== 'Draco' or x== 'Severus':
        return 'Slytherin'
    else:
        rand_house= random.randint(1,4)
        if rand_house==4:
            return'Gryffindor'
        elif rand_house==3:
            return'Hufflepuff'
        elif rand_house==2:
            return'Ravenclaw'
        else:
            return'Slytherin'







#Main
main()
