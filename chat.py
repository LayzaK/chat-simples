import os 

mensagens = []

nome = input('nome: ')

while True:

    #limpando o terminal com a importação do 'os'
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'],'-', m['texto'])

        print('_______________')
    
    #obtendo texto
    texto = input('mensagem: ')
    #texto = fim -> o loop para/da um break
    if texto == 'fim':
        break

    #adicionando mensagem na lista
    mensagens.append({
        'nome': nome,
        'texto': texto

    })




