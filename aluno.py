# Classe Aluno
class Aluno:
    # Construtor da classe
    def __init__(self, nome, semestre, notas, frequencia):
        self.__nome = nome
        if float(frequencia) <= 70:
            self.__evasao = True
        else:
            self.__evasao = False
        self.__historico = HistoricoEscolar(semestre, notas, frequencia)

    # Métodos get/set
    def set_nome(self, nome):
        self.__nome = nome
    def set_evasao(self, evasao):
        self.__evasao = evasao
    def set_historico(self, historico):
        self.__historico = historico  # Atualiza o histórico
    def get_nome(self):
        return self.__nome
    
    # Outros Métodos
    def exibir_historico(self):
        print(f"Nome: {self.__nome}")
        print(f"Evasão: {self.__evasao}")
        self.__historico.exibir_historico()  # Chama o método da classe HistoricoEscolar

# Classe HistoricoEscolar
class HistoricoEscolar:
    # Construtor da classe
    def __init__(self, semestre, notas, frequencia):
        self.__semestre = semestre
        self.__notas = notas
        self.__frequencia = frequencia
        self.__media = sum(notas) / len(notas) if notas else 0  # Calcula a média das notas

    # Métodos get/set
    def set_semestre(self, semestre):
        self.__semestre = semestre
    def set_frequencia(self, frequencia):
        self.__frequencia = frequencia
    def get_semestre(self):
        return self.__semestre
    def get_media(self):
        return self.__media
    def get_frequencia(self):
        return self.__frequencia

    # Método para exibir o histórico
    def exibir_historico(self):
        print(f"Semestre: {self.__semestre}")
        print(f"Notas: {', '.join(map(str, self.__notas))}")
        print(f"Frequência: {self.__frequencia}%")
        print(f"Média: {self.__media:.2f}")  # Exibe a média formatada
