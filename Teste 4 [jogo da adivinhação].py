#jogo1
print('*><*><*><*><*><*><*><*><*><*><*><*><*><*><')
print('*><*><*><*>< advinhe o número ><*><*><*><*'.upper())
print('*><*><*><*><*><*><*><*><*><*><*><*><*><*><\n')
chance = 3
num_prog = 30
print('Regra do jogo: você terá que descobrir o número inteiro programado. Porém, para isso, você terá apenas 3 chances.')
while(chance >= 1):
    perg = int(input('Qual o número?\n'))
    if(perg == 30):
        print('você ganhou!!!'.upper())
        break
    elif(perg < 30):
        print('{} é menor que o número programado.'.format(perg))
    elif(perg > 30):
        print('{} é maior que o número programado.'.format(perg))
    chance = chance - 1
print('você perdeu.'.upper())
print('FIM DO JOGO.')