import tkinter as tk
from tkinter import messagebox
import pandas as pd
from itertools import cycle

materias = []

def adicionar_materia():
    materia = entrada_materia.get().strip().capitalize()
    if materia:
        materias.append(materia)
        lista_materias.insert(tk.END, materia)
        entrada_materia.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Digite o nome da matéria.")

def gerar_plano():
    try:
        horas = int(entrada_horas.get())
        if horas <= 0:
            messagebox.showerror("Erro", "Horas devem ser maiores que zero.")
            return
        if not materias:
            messagebox.showerror("Erro", "Adicione pelo menos uma matéria.")
            return

        dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        tabela = []
        ciclo_m = cycle(materias)

        for _ in range(horas):
            linha = [next(ciclo_m) for _ in dias]
            tabela.append(linha)

        df = pd.DataFrame(tabela, columns=dias)
        df.index = [f"{6 + i}h" for i in range(horas)]

        plano_texto.delete(1.0, tk.END)
        plano_texto.insert(tk.END, df.to_string())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido de horas.")

# interface
janela = tk.Tk()
janela.title("Plano de Estudos")

# Campo horas
tk.Label(janela, text="Horas de estudo por dia:").pack()
entrada_horas = tk.Entry(janela)
entrada_horas.pack()

# Campo  matéria
tk.Label(janela, text="Digite uma matéria:").pack()
entrada_materia = tk.Entry(janela)
entrada_materia.pack()

# Botão para adicionar matéria
tk.Button(janela, text="Adicionar matéria", command=adicionar_materia).pack()

# Lista de matérias adicionadas
tk.Label(janela, text="Matérias adicionadas:").pack()
lista_materias = tk.Listbox(janela, height=6)
lista_materias.pack()

# gerar plano
tk.Button(janela, text="Gerar plano semanal", command=gerar_plano).pack(pady=5)


plano_texto = tk.Text(janela, height=10, width=60)
plano_texto.pack()

janela.mainloop()
