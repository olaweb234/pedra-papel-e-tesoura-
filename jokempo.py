from random import randint

obj =['pedra','papel','tesoura']
pc=randint(0,2)
print(''' 
          [0] pedra
          [1] papel
          [2] tesoura ''')


user=int(input('Fale sua jogada:'))

while user>=3:
    print('jogda invalida')
    user=int(input('Fale sua jogada:'))


print('-='*30)
print(f'o pc jogou {obj[pc]} e vc jogou {obj[user]}')
print('-='*30)



if pc == 0:
    if user == 0:
        print('empate')
    elif user == 1:
        print('ganhou')
    elif user == 2:
        print('perdeu ')
  
    

if pc == 1:
    if user== 0:
        print('perdeu')
    elif user == 1:
        print('empate')
    elif user == 2:
        print('ganhou') 
  

if pc == 2:
    if user==0:
        print('ganhou')
    elif user==1:
        print('perdeu')
    elif user == 2:
        print('empate')
    

    
