#Dog_Breed.py


#Initilize
import time
import pandas as pd
data=pd.read_csv('Sheet1.csv')
name=data['Name'].tolist()
id=data['id'].tolist()
bg=data['Breed Group'].tolist()
job=data['BredFor'].tolist()
min_life=data['Minimum Life Span'].tolist()
max_life=data['Maximum Life Span'].tolist()
min_height=data['Minimum Height'].tolist()
max_height=data['Maximum Height'].tolist()
min_weight=data['Minimum Weight'].tolist()
max_weight=data['Maximum Weight'].tolist()
pic=data['Image'].tolist()
temp=data['Temperament'].tolist()

#Function

filter=[]
def dog_size(size):
    filter.clear()
    if size =='tiny':
        for i in range(len(data)):
            if min_weight[i]<= 10 :
                filter.append(name[i])
    elif size == 'small':
        for i in range (len(data)):
            if min_weight[i]<=25 and min_weight[i]> 10:
                filter.append(name[i])
    elif size == 'medium':
        for i in range (len(data)):
            if min_weight[i]<= 60 and min_weight[i]> 25:
                filter.append(name[i])
    elif size == 'large':
        for i in range (len(data)):
            if min_weight[i]>= 60:
                filter.append(name[i])
    else:
        print('Thats not a valid input, try putting something else!')
    print('Here are some dogs that fit your size prefreance')
    print (filter)
    filter.clear()

def dog_search(dog):
    filter.clear()
    for i in range(len(data)):
        if dog in name[i]:
            filter.append(name[i])
            filter.append(temp[i])
            filter.append(pic[i])
    print(filter)
    if (len(filter))==0:
        print ('Im sorry thats not a dog on our list, try searching a dirrerent name')

def dog_job(task):
    filter.clear()
    for i in range (len(data)):
        if task in job[i]:
            filter.append(name[i])
    print(filter)
    if (len(filter))==0:
        print ('Im sorry thats not a job dogs are breed for')


def menu():
    while True:
        print(' Hi I hear you are looking for a new forever friend!')
        choice=input (' Are you searching by the dogs (size, name, or job): ' )
        time.sleep(1)
        if choice== 'size':
            scale=input ('are you looking for a (tiny, small, medium, or large): ' )
            if scale=='tiny':
                dog_size('tiny')
            elif scale=='small':
                dog_size('small')
            elif scale=='medium':
                dog_size('medium')
            elif scale== 'large':
                dog_size('large')
            else:
                print('Thats not a valid input, try searching somthing else')
                time.sleep(1)
            escape= input('Would you like to keep looking (yes,no): ')
            if escape=='no':
                    break

        elif choice== 'name':
            title=input('What dog are you trying to find?: ')
            dog_search(title)
            escape= input('Would you like to keep looking (yes,no): ')
            if escape=='no':
                break
        elif choice=='job':
            occupation=input('What jobs do you want in a dog?: ')
            dog_job(occupation)
            escape= input('Would you like to keep looking (yes,no): ')
            if escape=='no':
                break

            continue









#Main
menu()

#Sources:
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en

