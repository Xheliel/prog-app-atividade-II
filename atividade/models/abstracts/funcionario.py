from abc import ABC, abstractmethod
from models.enums.setor import Setor
from models.enums.sexo import Sexo

class Funcionario(ABC):
    def __init__(self, nome: str, data_nascimento: str, sexo: Sexo, setor: Setor, salario_base: float):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.setor = setor
        self.salario_base = salario_base

    @abstractmethod
    def salario_final(self):
        pass

    def __str__(self):
        return (
            f"\nFuncionário\n"
            f"\nNome: {self.nome}"
            f"\nData de nascimento: {self.data_nascimento}"
            f"\nSexo: {self.sexo.value}"
            f"\nSetor: {self.setor.value}"
            f"\nSalário base: {self.salario_base:.2f}\n"
        )