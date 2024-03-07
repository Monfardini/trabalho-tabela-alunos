from tabela_aluno import alunos
from tabela_aluno import listar_alunos
from recuperar_aluno import recuperar_aluno_por_id


def mostra_lista():
    print("LISTA DE ALUNOS")
    return listar_alunos()

def recupera_aluno():
    id= input("Digite o Id que deseja recuperar:")
    return recuperar_aluno_por_id(id)

print("--------- banco de alunos ---------")
print("oq deseja fazer?\n [1] - para banco de alunos\n [2] - para recuperar aluno por ID\n")

option = input("digite sua escolha:")

if option == "1":
    mostra_lista()
if option =="2":
    recupera_aluno()
else:
    print("Opção Inválida.")


    
    
