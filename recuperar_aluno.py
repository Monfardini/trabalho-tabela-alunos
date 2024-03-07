from tabela_aluno import alunos

# Função para recuperar um aluno pelo ID
def recuperar_aluno_por_id(id):
    for aluno in alunos:
        if aluno["id"] == id:
            print("Aluno encontrado:")
            print(f"ID: {aluno['id']}, Nome: {aluno['nome']}, Idade: {aluno['idade']}")
            return aluno
    return None and print("Aluno não encontrado.")

