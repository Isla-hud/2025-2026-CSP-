#Recommend.py
#Isla Hudecek

#Initilize
import webbrowser

#Function
movies=['https://tinyurl.com/2trvrn9b', #10 Thinks I Hate about you
        'https://tinyurl.com/4xykwpbz', # The village
        'https://tinyurl.com/ymn5tkep', # Indiana Jones Raiders of the lost
        'https://tinyurl.com/3uy3dtre'  #Knives out
        ]
des=['An movie about an unlikly couple wich differs from most movies you have seen. Though on the older side its a movie everyone should watch young and old and is a great movie to bridge gaps between generations',
     'The Village is a masterpice of a movie and does a great job stinging its audience along. With twist and turnes that have you on the edge of your seat.',
     'Indiana Jones is a fast pace action movie that is perfect for any group, with great humor and exiting fight sequences this movie will hold the attendion of all its watchers.',
     'Knives out it one of the best murder mysterys to come out in recent years wityh popular actors and a great stoyline, this movie keeps you on the edge of your seat and its endingis somthing you will never see coming']
def movie():
    print('Welcome to Movie Generator Here to Give you the best Recomendation for ANY situation!')
    croud= input ('Who are you waching with (friends or family): ')
    if croud== 'family':
        age= input('Will kids be watching (yes,no)' )
        if age=='no':
                print('Awsome, no age restrictions then')
                genre= input ('Are you in the mood for (action or romance): ')
                if genre =='romance':
                    webbrowser.open(movies[1])
                    print(des[1])
                elif genre=='action':
                    webbrowser.open(movies[2])
                    print(des[2])
        elif age=='yes':
            genre= input ('Are you in the mood for (action or romance): ')
            if genre =='romance':
                webbrowser.open(movies[0])
                print(des[0])
            elif genre=='action':
                    webbrowser.open(movies[2])
                    print(des[2])

    elif croud =='friends':
                genre= input ('Are you in the mood for (mystery, romance, thriller): ')
                if genre =='romance':
                    webbrowser.open(movies[0])
                    print(des[0])
                elif genre=='thriller':
                    webbrowser.open(movies[1])
                    print(des[1])
                elif genre== 'mystery':
                    webbrowser.open(movies[3])
                    print(des[3])


#Main
movie()

#Picture of the 10 Things I hate about you Movie poster
#URL: 'https://www.imdb.com/title/tt0147800/'
#Article Name: 10 Things I hate about You
#Website Name: imdb.com

#Picture of The Village Poster
#URL: 'https://www.imdb.com/title/tt0368447/'
#Article Name: The village
#Website Name: imdb.com

#Picture of Indiand Jones Raiders of the Lost
#URL: 'https://www.imdb.com/title/tt0082971/'
#Article Name: Indiana Jones Raisder of the Lost
#Website Name: imdb.com


#Picture of Knives Out poster
#URL: 'https://www.imdb.com/title/tt8946378/'
#Article Name: Knives Out
#Website Name: imdb.com
