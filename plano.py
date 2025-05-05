import math
print("Seja bem vindo")

def coletor_materia(n):    #função de materias  
    materias = []             
    for i in range(n):        
        nome = input(f"Digite o nome da matéria {i+1}: ")  
        materias.append(nome)  
    return materias;

horas=int(input("Quantas horas pretende estudar?"))
n_materias = int(input("Quantas matérias você vai estudar? "))
materias = coletor_materia(n_materias)


print("\nVocê vai estudar:")
for m in materias:
    print(f"-{m}")
   

#função de dia  
def dia(): 
    print("DIA")

#função da semana

def semana():
    print("SEMANA")
    

#MENU
def menu():
    while True:
        print("\n---MENU---")
        print("1-dia")
        print("2-semana")
        print("3-Sair")

        escolha=input("Escolha uma opção:")

        if escolha=="1":
            dia()
        elif escolha=="2":
            semana()
        elif escolha =="3":
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()