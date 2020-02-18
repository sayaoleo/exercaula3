dias={1:'Domingo', 2:'Segunda',3:'Terça',4:'Quarta',5:'Quinta',6:'Sexta',7:'Sábado'}
num_digitado = int(input('Digite um número de 1 à 7: '))

if num_digitado >= 1 and num_digitado <= 7:
    nome_dia = dias.get(num_digitado)
    print(nome_dia)
else:
    print('Valor não está entre 1 e 7')



