from abc import ABC, abstractmethod
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.abstracts.funcionario import Funcionario

class Diretor(Funcionario):
    def __init__(self, nome: str, data_nascimento: str, sexo: Sexo, setor: Setor, salario_base: int):
        super().__init__(nome, data_nascimento, sexo, setor, salario_base)
        

    class Contratacao(ABC):
        @abstractmethod
        def admitir(self):
            pass

        def demitir(self):
            pass

    def salario_final(self):
        PREMIO = 0.2
        return self.salario_base * PREMIO
    
    def __str__(self):
        return (
            f"{super().__str__()}"
            f"Salário final: {self.salario_final():.2f}"
        )
