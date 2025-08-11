import tkinter as tk
from tkinter import messagebox


def enviar():
    dados = {
        "Nome": entry_nome.get(),
        "Idade": entry_idade.get(),
        "E-mail": entry_email.get(),
        "Gênero": genero.get(),
        "Interesses": [int_var_python.get(), int_var_javascript.get(), int_var_java.get()],
        "Comentário": comentario.get("1.0", tk.END).strip(),
        "Aceita os termos": var_termos.get()
    }

    if not dados["Nome"] or not dados["E-mail"]:
        messagebox.showwarning("Atenção", "Nome e E-mail são obrigatórios!")
        return

    if not dados["Aceita os termos"]:
        messagebox.showwarning("Atenção", "Você deve aceitar os termos.")
        return

    interesses = []
    if dados["Interesses"][0]: interesses.append("Python")
    if dados["Interesses"][1]: interesses.append("JavaScript")
    if dados["Interesses"][2]: interesses.append("Java")

    resumo = f"""
    --- Dados Recebidos ---
    Nome: {dados["Nome"]}
    Idade: {dados["Idade"]}
    E-mail: {dados["E-mail"]}
    Gênero: {dados["Gênero"]}
    Interesses: {', '.join(interesses)}
    Comentário: {dados["Comentário"]}
    """
    messagebox.showinfo("Formulário enviado!", resumo)


janela = tk.Tk()
janela.title("Formulário Completo")


tk.Label(janela, text="Nome:").grid(row=0, column=0, sticky="w")
entry_nome = tk.Entry(janela, width=40)
entry_nome.grid(row=0, column=1)


tk.Label(janela, text="Idade:").grid(row=1, column=0, sticky="w")
entry_idade = tk.Entry(janela, width=10)
entry_idade.grid(row=1, column=1, sticky="w")


tk.Label(janela, text="E-mail:").grid(row=2, column=0, sticky="w")
entry_email = tk.Entry(janela, width=40)
entry_email.grid(row=2, column=1)


tk.Label(janela, text="Gênero:").grid(row=3, column=0, sticky="w")
genero = tk.StringVar()
tk.Radiobutton(janela, text="Masculino", variable=genero, value="Masculino").grid(row=3, column=1, sticky="w")
tk.Radiobutton(janela, text="Feminino", variable=genero, value="Feminino").grid(row=4, column=1, sticky="w")
tk.Radiobutton(janela, text="Outro", variable=genero, value="Outro").grid(row=5, column=1, sticky="w")


tk.Label(janela, text="Interesses:").grid(row=6, column=0, sticky="w")
int_var_python = tk.BooleanVar()
int_var_javascript = tk.BooleanVar()
int_var_java = tk.BooleanVar()
tk.Checkbutton(janela, text="Python", variable=int_var_python).grid(row=6, column=1, sticky="w")
tk.Checkbutton(janela, text="JavaScript", variable=int_var_javascript).grid(row=7, column=1, sticky="w")
tk.Checkbutton(janela, text="Java", variable=int_var_java).grid(row=8, column=1, sticky="w")

tk.Label(janela, text="Comentário:").grid(row=9, column=0, sticky="nw")
comentario = tk.Text(janela, height=5, width=40)
comentario.grid(row=9, column=1)


var_termos = tk.BooleanVar()
tk.Checkbutton(janela, text="Aceito os termos de uso", variable=var_termos).grid(row=10, columnspan=2, pady=10)


tk.Button(janela, text="Enviar", command=enviar).grid(row=11, columnspan=2, pady=10)
janela.mainloop()