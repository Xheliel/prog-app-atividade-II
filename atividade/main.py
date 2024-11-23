from models.abstracts.funcionario import Funcionario
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.diretor import Diretor
from models.motoboy import Motoboy
import os

#funcionario1 = Funcionario("XXXXXX", "XX/XX/XXXX", Sexo.MASCULINO, Setor.OPERACOES, 3500)
diretor1 = Diretor("XXXXX", "XX/XX/XXXX", Sexo.MASCULINO, Setor.FINANCEIRO, 7000)
motoboy1 = Motoboy("XXXXXXX", "XXXXX", "XX/XX/XXXX", Sexo.FEMININO, Setor.OPERACOES, 1400)

os.system("cls || clear")
print(diretor1)
print(motoboy1)