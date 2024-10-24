from database import criar_tabela, adicionar_tarefa, listar_tarefas, editar_tarefa, excluir_tarefa

def main():
    criar_tabela()  # Cria a tabela se não existir

    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Editar Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            descricao = input("Descrição da tarefa: ")
            adicionar_tarefa(descricao)
            print("Tarefa adicionada com sucesso!")

        elif opcao == '2':
            tarefas = listar_tarefas()
            print("\nLista de Tarefas:")
            for tarefa in tarefas:
                print(f"{tarefa[0]}: {tarefa[1]} [{tarefa[2]}]")  # Exibe id, descrição e status

        elif opcao == '3':
            id = int(input("ID da tarefa que deseja editar: "))
            nova_descricao = input("Nova descrição da tarefa: ")
            editar_tarefa(id, nova_descricao)
            print("Tarefa editada com sucesso!")

        elif opcao == '4':
            id = int(input("ID da tarefa que deseja excluir: "))
            excluir_tarefa(id)
            print("Tarefa excluída com sucesso!")

        elif opcao == '5':
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
