#Isla Hudecek
#Keep asking for the password untill correct one is inputted

#Function
def main():
    while True:
        check= input ('Enter Password: ')
        if check != 'Python35':
            print ('Incorrect Password, Please Try Agian')
            continue
        elif check== 'Python35':
            print ('Access Granted!')
            break

#Main
main()
