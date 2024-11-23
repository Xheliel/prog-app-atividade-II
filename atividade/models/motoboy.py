from models.abstracts.funcionario import Funcionario
from models.enums.setor import Setor
from models.enums.sexo import Sexo

class Motoboy(Funcionario):
    def __init__(self, cnh: str, nome: str, data_nascimento: str, sexo: Sexo, setor: Setor, salario_base: float):
        super().__init__(nome, data_nascimento, sexo, setor, salario_base)
        self.cnh = cnh

    def salario_final(self):
        return self.salario_base

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"CNH: {self.cnh}"
            f"\nSalário final: {self.salario_final():.2f}\n"

        )