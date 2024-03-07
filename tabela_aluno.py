# Inicializar a lista de alunos
alunos = []

# Função para adicionar um aluno
def adicionar_aluno(id, nome, idade):
    aluno = {"id": id, "nome": nome, "idade": idade}
    alunos.append(aluno)

# Função para imprimir todos os alunos
def listar_alunos():
    for aluno in alunos:
        print(f"ID: {aluno['id']}, Nome: {aluno['nome']}, Idade: {aluno['idade']}")

# Adicionando alguns alunos
adicionar_aluno(3027584, "João", 17 )
adicionar_aluno(3026457, "Maria", 15 )
adicionar_aluno(3027978, "José", 16 )
adicionar_aluno(3024567, "Antônio",16 )
adicionar_aluno(3027004, "Bruno", 33 )
adicionar_aluno(3026533, "Gabriel", 19 )
adicionar_aluno(3025554, "Núbia", 18 )
adicionar_aluno(3025612, "Kátia", 20)
adicionar_aluno(3027226, "Yasmim", 14 )
adicionar_aluno(3026777, "Helena", 22 )


# Listando todos os alunos
listar_alunos()
