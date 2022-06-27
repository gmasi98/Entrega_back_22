class Professor:

    def __init__(self, nome_pro):
        self.nome_pro = nome_pro
    
    # os professores add devem estar numa lista
    def adicionar_professor(self):
        self.nome_pro = input("Digite o nome do professor a ser adicionado: ")
        print(f"Professor {self.nome_pro} foi adicionado ao sistema")
        prof_add = []
        prof_add.append(self.nome_pro)
        print(prof_add)
       

        
    def excluir_professor(self):
        self.nome_pro = input("Digite o nome do professor excluído: ")
        print(f"Professor {self.nome_pro} foi excluído do sistema")
        prof_excluido = []
        prof_excluido.append(self.nome_pro)
        print(prof_excluido)

add_prof = Professor("x")
add_prof.adicionar_professor()
exclui_prof = Professor("x")
exclui_prof.excluir_professor()

class Aluno:

    def __init__(self, nome_al):
        self.nome_al = nome_al
    
    def add_aluno(self):
        self.nome_al = input("Digite o nome do aluno a ser adicionado: ")
        print(f"Aluno {self.nome_al} foi adicionado ao sistema")
        al_add = []
        al_add.append(self.nome_al)
        print(al_add)
       

    def excluir_aluno(self):
        self.nome_al = input("Digite o nome do aluno excluído: ")
        print(f"Aluno {self.nome_al} foi excluído do sistema")
        al_excluido = []
        al_excluido.append(self.nome_al)
        print(al_excluido)

adicionar_aluno = Aluno("y")
adicionar_aluno.add_aluno()
exclui_al = Aluno("y")
exclui_al.excluir_aluno()      

class Sala_de_aula:

    def __init__(self, sala):
        self.sala = sala

    def add_sala(self):
        self.sala = input("Digite a sala a ser adicionada: ")
        print(f"Sala {self.sala} foi adicionada ao sistema")
        sala_de_aula_add = []
        sala_de_aula_add.append(self.sala)
        print(sala_de_aula_add)

    def excluir_sala(self):
        self.sala = input("Digite a sala a ser excluída: ")
        print(f"Sala {self.sala} foi excluída do sistema")
        sala_de_aula_excluida = []
        sala_de_aula_excluida.append(self.sala)
        print(sala_de_aula_excluida)

add_sala_de_aula = Sala_de_aula("z")
add_sala_de_aula.add_sala()
exclui_sala_de_aula = Sala_de_aula("z")
exclui_sala_de_aula.excluir_sala() 

class Disciplina:

    def __init__(self, nome_da_disciplina):
        self.nome_da_disciplina = nome_da_disciplina

    def add_disciplina(self):
        self.nome_da_disciplina = input("Digite a disciplina a ser adicionada: ")
        print(f"Disciplina {self.nome_da_disciplina} foi adicionada ao sistema")
        disciplina_add = []
        disciplina_add.append(self.nome_da_disciplina)
        print(disciplina_add)

    def excluir_disciplina(self):
        self.nome_da_disciplina = input("Digite a disciplina a ser excluída: ")
        print(f"Disciplina {self.nome_da_disciplina} foi excluída do sistema")
        disciplina_excluida = []
        disciplina_excluida.append(self.nome_da_disciplina)
        print(disciplina_excluida)

adicionar_disciplina = Disciplina("w")
adicionar_disciplina.add_disciplina()
exclui_disciplina = Disciplina("w")
exclui_disciplina.excluir_disciplina() 

