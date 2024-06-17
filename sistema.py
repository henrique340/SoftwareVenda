from time import sleep
import os
import datetime
import sqlite3

# Criando as tabelas do banco de dados

conect = sqlite3.connect('crm.db')
banco = conect.cursor()

banco.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    nome TEXT NOT NULL,
    contato TEXT,
    creatina INTEGER NOT NULL,
    scoop INTEGER,
    sexo TEXT NOT NULL,
    idade INTEGER NOT NULL,
    regiao TEXT NOT NULL,
    status TEXT NOT NULL
)
''')

conect.commit()
conect.close()

# ----------------------------- #
# Funcao para adicionar cliente #
# ----------------------------- #

def adicionar_cliente(data, nome, contato, creatina, scoop, sexo, idade, regiao, status):
    conect = sqlite3.connect('crm.db')
    banco = conect.cursor()

    banco.execute('''
    INSERT INTO clientes (data, nome, contato, creatina, scoop, sexo, idade, regiao, status)
    VALUES (?,?,?,?,?,?,?,?,?)
    ''',(data, nome, contato, creatina, scoop, sexo, idade, regiao, status))

    conect.commit()
    conect.close()

# ---------------------------- #
# Funcao pra consultar cliente #
# ---------------------------- #

def consultar_cliente():

    conect = sqlite3.connect('crm.db')
    banco = conect.cursor()

    banco.execute('SELECT * FROM clientes')
    for linha in banco.fetchall():
        print(linha)
    conect.close()

# ----------------------------- #
# Funcao para atualizar cliente #
# ----------------------------- #

def atualizar_cliente(id, data, nome, contato, creatina, scoop, sexo, idade, regiao, status):

    conect = sqlite3.connect('crm.db')
    banco = conect.cursor()

    banco.execute('''
    UPDATE clientes
    SET data = ?, nome = ?, contato = ?, creatina = ?, scoop = ?, sexo = ?, idade = ?, regiao = ?, status = ?
    WHERE id = ?
    ''', (data, nome, contato, creatina, scoop, sexo, idade, regiao, status, id))

    conect.commit()
    conect.close()

while True:
    print('-'*50)
    print('Sistema de venda de creatina'.center(50))
    print('-'*50)
    print('[1] - Ver pessoas cadastradas')
    print('[2] - Cadastrar pessoas')
    print('[3] - Sair do programa')
    opc = int(input("Digite a sua opção: "))

    if opc == 1:
        print('='*50)
        print("Pessoas".center(50))
        print('='*50)
        consultar_cliente()
        while True:
            enter = input(('Digite enter para continuar ...'))
            if enter == "":
                sleep(1)
                os.system('cls')
                break

    elif opc == 2:
        print('='*50)
        print("Cadastrar pessoas".center(50))
        print('='*50)

        # Entrada do usuário
        data = input("Digite a data [DD/MM/AA]: ")
        data_formada = datetime.datetime.strptime(data, '%d/%m/%Y').date()
        nome = input("Digite o nome do cliente: ")
        ctt = input("Digite quem foi o contato: ")
        creatina = int(input("Digite a quantidade [150]/[450]: "))
        scoop = int(input("Quantos scoops foram usados: "))
        sexo = input("Digite o sexo do cliente [M]/[H]: ").upper()
        idade = int(input("Digite a idade do cliente: "))
        cep = input("Digite a regiao que mora: ")
        status = input("Digite o status [Concluido]/[Espera]/[Recusado]: ")

        # Adicionando informações na planilha
        adicionar_cliente(data_formada, nome, ctt, creatina, scoop, sexo, idade, cep, status)
        sleep(1)
        os.system('cls')

    elif opc == 3:
        print("Fim do programa")
        sleep(3)
        break

    else:
        print("Erro! Digite uma opcao valida!")
        sleep(2)
        os.system('cls')
