# my first python project 
# word guessing 

import random

#creating a dictionary for storing the words and there clue 


dic = {  'pen':'An instrument used by kids and adult for same purpose ' ,
            'modem':'A device used for using the internet',
            'clock': 'A device that shows us something that never get enough of ',
            'money':'It is an illusion created by the powerfull for the powerless ',
            'future':'The one thing that you can control or maipulate '} 

name = input('enter your name please : ')

print(
    'Hello',name,
     'welcome to hangman '
     'hope you know the rule of this game '
     '    you have to guess a random word ')
word = random.choice(list(dic.keys())) 
nguesses = 10 
n = len(word)
     
#definig a fuction program for case coversion when needed 
def case(a) :
    if a.isupper()  :
        return a.lower() 
    else :
        return a
        
#defining a function prgram to check the guesses 
def inword(b) :
    if b in  word  :
        return True   
    else :
        print('\nNope wrong guess!')
        return None
            
#game starting sequence         
input_command1  = input('press y to start the game  ')
start = case(input_command1)
if start == 'y' :
    while(n != 0)  :   
        space = '_ ' * n
        nguesses -= 1
        print(' clue : ', dic[word])
        print(space)
        for i in range(n) :
            
            guess0 = input('enter the letter : ')
            guess1 = case(guess0)
            guess = inword(guess1)
            if guess == True :
                n -= 1              
                print(guess0,'_ ' * n)
                if nguesses == 0 :
                    print("YOU HAVE WON !")
            else : 
                print('wrong guess!')
       
        if nguesses == 0 :
            
            break 
else :
    print('venda myre vendaa nee ! ')
    print('game over ', name )            
    
    
        