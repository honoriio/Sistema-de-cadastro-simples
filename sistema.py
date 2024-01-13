from time import sleep

from lib.arquivo import *

arquivo = 'pessoas_cadastradas.txt'

if not arquivoexiste(arquivo):
    criararquivo(arquivo)

while True:
    cabecalho('CADASTRO PESSOAL V-0.1.1')
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar pessoas cadastradas
        lerarquivo(arquivo)
    elif resposta == 2:
        # Cadastro de pesosa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção incorreta no menu
        cabecalho('\033[31mERRO!: Digite uma opção válida!\033[0m')
    sleep(1)
