import random

def schimbare(nr):
    if nr == 1:
        return 'piatra'
    elif nr == 2:
        return 'hartie'
    elif nr == 3:
        return 'foarfeca'

def rezultat(player , AI_player):
        if player.lower() == AI_player:
            print("Este egalitate")
        elif player.lower() == 'piatra' and AI_player == 'foarfeca':
            print("Ai castigat")
        elif player.lower() == 'piatra' and AI_player == 'hartie':
            print ('Ai pierdut')
        elif player.lower() == 'hartie' and AI_player == 'piatra':
            print ('Ai castigat')
        elif player.lower() == 'hartie' and AI_player =='foarfeca':
            print ('Ai pierdut')
        elif player.lower() == 'foarfeca' and AI_player == 'hartie':
            print('Ai castigat')
        elif player.lower() == 'foarfeca' and AI_player == 'piatra':
            print('Ai pierdut')

while True:
    start = input("Salut , vrei sa te joci piatra , hartie ,foarfeca? da/nu ")
    if start.lower() == "da":
            play = True
            break
    elif start.lower() == "nu":
            play = False
            break
    else:
        print('Introdu una dintre optiunile da/nu')
        continue



while play:
        while True:
            player = input('Alege piatra/hartie/foarfeca : ')
            if player.lower() == "piatra" or player.lower() == "hartie" or player.lower() == "foarfeca":
                break
            else:
                print('Introdu una dintre obtiunile piatra/hartie/foarfeca')
                continue


        AI_player = random.randint(1,3)
        AI_player = schimbare(AI_player)
        print(f'Calculatorul a  ales {AI_player}')
        rezultat(player,AI_player)
        while True:
            exit = input("Vrei sa mai joci o runda? da/nu : ")
            if exit.lower() =='da':
                play = True
                break
            elif exit.lower() == 'nu':
                play = False
                break
            else:
                print('Introdu una dintre obtiunile da/nu')
                continue

print('Ok ,pa')
