tarefas = []
estadotarefas = []

def adicionar(nometarefa):
    tarefas.append(f"{nometarefa}")
    estadotarefas.append("Pendente")
    i = tarefas.index(nometarefa)
    print(f'ADICIONANDO... Tarefa {tarefas[i]} adicionada')

def buscar(nometarefa):
        if nometarefa in tarefas:
            i = tarefas.index(nometarefa)
            print(f"\nBUSCANDO... Tarefa: {nometarefa} || Estado: {estadotarefas[i]}")
        else:
            print("404")

def concluir(nometarefa):
        if nometarefa in tarefas:
            i = tarefas.index(nometarefa)
            estadotarefas[i] = "Concluído"
            print(f'\nCONCLUINDO... Tarefa {nometarefa} concluída')
        else:
            print("404")

def remover(nometarefa):
        if nometarefa in tarefas:
            i = tarefas.index(nometarefa)
            tarefas.pop(i)
            estadotarefas.pop(i)
            print(f"\nREMOVENDO... Tarefa {nometarefa} removida")
        else:
            print("404")

def listar():
    print("\nLISTANDO...")
    for i in (0,len(tarefas)-1):
        print(f"Tarefa: {tarefas[i]}|| Estado: {estadotarefas[i]}")
    print()

adicionar("Matemática")
adicionar("Português")
adicionar("Biologia")
adicionar("Filosofia")

buscar("Matemática")

concluir("Português")

remover("Filosofia")

listar()