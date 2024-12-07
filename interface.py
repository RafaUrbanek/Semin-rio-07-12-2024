# Programa principal
from aluno import Aluno

alunos = []

# Função para mostrar o menu e pegar a opção do usuário
def menu():
    print("==================================")
    print("1- Adicionar aluno")
    print("2- Consultar Histórico")
    print("3- Sair do sistema")
    opcao = input("Escolha uma das opções acima: ")
    print("==================================")
    return opcao

# Função para registrar um aluno
def registra_aluno(nome, semestre, lista_de_notas, frequencia):
    aluno = Aluno(nome, semestre, lista_de_notas, frequencia)
    alunos.append(aluno)  # Adiciona o aluno na lista

# Função para consultar o histórico de um aluno
def consultar_historico(nome):
    for aluno in alunos:
        if aluno.get_nome() == nome:  # Verifica se o nome do aluno corresponde
            return aluno
    return None  # Retorna None caso o aluno não seja encontrado

# Programa Principal
opcao = menu()
while(opcao != "3"):
    if(opcao == "1"):
        nome = input("Digite o nome do aluno: ")
        semestre = input("Digite o semestre: ")
        notas = input("Digite as notas (separadas por espaço): ")
        frequencia = float(input("Digite a frequência em %: "))
        
        # Convertendo as notas para uma lista de floats
        lista_de_notas = [float(nota) for nota in notas.split()]
        
        # Registrando o aluno
        registra_aluno(nome, semestre, lista_de_notas, frequencia)

    elif(opcao == "2"):    
        nome = input("Digite o nome do aluno para ser consultado: ")
        aluno = consultar_historico(nome)  # Consultando o histórico do aluno
        if aluno:  # Se o aluno for encontrado
            aluno.exibir_historico()  # Exibe o histórico do aluno
        else:
            print("Aluno não encontrado!")
    else:
        print("Opção inválida, tente novamente!")
    opcao = menu()
