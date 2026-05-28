# To create a fun and interactive game that allows users to input words and generate a nonsensical story.
#Isla Hudecek

#init
import random
#Function
def madlibs():
    list=input ('Would you like to randomize your responses(yes,no)? ')
    if list=='yes':
        places=['beach','restaurant','sports','game']
        place = random.choice(places)
        names=['Sasha','Matthew','Michael','Emily']
        name=random.choice(names)
        emotions=['angery', 'scared','happy','joyful']
        emotion=random.choice(emotions)
        animals=['hampster','owl','chicken','cow']
        animal=random.choice(animals)
        persons=['Tom Hank', 'Jeffery Star', 'Tom Holland']
        person=random.choice(persons)
        verbs=['jump', 'fly', 'dance','hang']
        verb=random.choice(verbs)
        numbers=['5','6','10','15','30']
        number=random.choice(numbers)
        rooms=['bathroom','basment','bedroom']
        room=random.choice(rooms)
        buildings=['Eiffel tower', 'Brooklan Bridge', 'Water Tower']
        building=random.choice(buildings)

    #gather input
    elif list =='no':
        place =input ('Please enter an Location: ' )
        name=input ('Plese pick a name: ')
        emotion= input('Please pick an emotion: ')
        animal=input ('Please choose an Unique Animal: ')
        person=input ('Choose any person and try to be diffrent: ')
        verb=input('Please choose an action verb:')
        number= input('Choose a random number:')
        print('Two more question')
        room=input('Pick any room in your house:')
        building=input('What is your favorite building?: ' )

    #story
    print(f"""I went to a \033[1m{place.upper()}\033[0m with my friend \033[1m{name.upper()}\033[0m.
I was so \033[1m{emotion.upper()}\033[0m when we bumped into a gang of \033[1m{animal.upper()}\033[0m we tried getting away
when \033[1m{person.upper()}\033[0m steped out from the gang of \033[1m{animal.upper()}\033[0m.
They surrounded us so I pushed \033[1m{name.upper()}\033[0m forward and \033[1m{verb.upper()}\033[0m.
I got all the way back home and locked myself in \033[1m{room.upper()}.\033[1m{number.upper()}\033[0m years
later while on my way home I was pushed off \033[1m{building.upper()}\033[0m.
On my way down I cought a glimps of the person behind it \033[1m{name.upper()}\033[0m with an army of \033[1m{animal.upper()}\033[0m at their back.""")

#Main
madlibs()
