import random
from art import logo
from art import vs
from data import data

def select(index):
    person={
        'name':data[index]['name'],
    'work':data[index]['description'],
    'place':data[index]['country'],
    'followers':data[index]['follower_count']
    }
    return person
    


def play_game():
    flag=True
    person1=random.randint(0,len(data)-1)
    score=0
    print(logo)
    while flag:
        person2=random.randint(0,len(data)-1)
        print(f"Compare A: {select(person1)['name']}, a {select(person1)['work']}, from {select(person1)['place']}. ")
        print(vs)
        print(f"Against B:{select(person2)['name']}, a {select(person2)['work']}, from {select(person2)['place']}.")
        guess=input("Who do you think has more followers? Type 'A' or 'B'.")
        if guess=='A' and select(person1)['followers']>select(person2)['followers']:
            score=score+1
            person1=person2
            print(logo)
            print(f"Yes! That's correct! Your score: {score}")
        elif guess=='B' and select(person2)['followers']>select(person1)['followers']:
            score=score+1
            person1=person2
            print(logo)
            print(f"Yes! That's correct! Your score: {score}")
        else:
            print(f"Sorry! That's wrong. Final score: {score}")
            flag=False



while input("Do you want to play the game? Type 'Y' or 'N'.")=='Y':
    play_game()
    




