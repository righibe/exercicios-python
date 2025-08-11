import tkinter as tk
from tkinter import messagebox

def enviar():
    dados = {
        "Nome de Cria": entry_nome.get(),
        "Quebrada": entry_quebrada.get(),
        "Idade": entry_idade.get(),
        "Grau de Fã": grau_fa.get(),
        "Fez pix pro Tigrin": var_pix.get(),
        "Tem bundão de academia": var_bundao.get(),
        "Topa ir pro baile": var_baile.get(),
        "Comentário": comentario.get("1.0", tk.END).strip()
    }

    if not dados["Nome de Cria"]:
        messagebox.showwarning("Atenção", "Nome de Cria é obrigatório!")
        return

    resumo = f"""
    --- Dados do Formulário do Oruam ---
    Nome de Cria: {dados["Nome de Cria"]}
    Quebrada: {dados["Quebrada"]}
    Idade: {dados["Idade"]}
    Grau de Fã: {dados["Grau de Fã"]}
    Fez pix pro Tigrin: {"Sim" if dados["Fez pix pro Tigrin"] else "Não"}
    Tem bundão de academia: {"Sim" if dados["Tem bundão de academia"] else "Não"}
    Topa ir pro baile: {"Sim" if dados["Topa ir pro baile"] else "Não"}
    Comentário: {dados["Comentário"]}
    """

    messagebox.showinfo("Formulário Enviado!", resumo)
    print('''Ô, garota, eu quero você só pra mim (pra mim)
Botou a bunda com o dinheiro do Tigrin (no complexo)
Vem pro Rio que tu sabe que sou cria (no complexo)
Vem mostrando esse bundão de academia (no complexo)''')

janela = tk.Tk()
janela.title("Formulário Hiper Mega Complexo do Oruam")

tk.Label(janela, text="Nome de Cria:").grid(row=0, column=0, sticky="w")
entry_nome = tk.Entry(janela, width=40)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="Quebrada:").grid(row=1, column=0, sticky="w")
entry_quebrada = tk.Entry(janela, width=40)
entry_quebrada.grid(row=1, column=1)

tk.Label(janela, text="Idade:").grid(row=2, column=0, sticky="w")
entry_idade = tk.Entry(janela, width=10)
entry_idade.grid(row=2, column=1, sticky="w")

tk.Label(janela, text="Grau de Fã (0-10):").grid(row=3, column=0, sticky="w")
grau_fa = tk.StringVar()
grau_fa.set("10")
tk.Spinbox(janela, from_=0, to=10, textvariable=grau_fa, width=5).grid(row=3, column=1, sticky="w")

var_pix = tk.BooleanVar()
tk.Checkbutton(janela, text="Já fez pix pro Tigrin 💸", variable=var_pix).grid(row=4, columnspan=2, sticky="w")

var_bundao = tk.BooleanVar()
tk.Checkbutton(janela, text="Tem bundão de academia 🍑", variable=var_bundao).grid(row=5, columnspan=2, sticky="w")

var_baile = tk.BooleanVar()
tk.Checkbutton(janela, text="Topa ir pro baile no complexo 🎶", variable=var_baile).grid(row=6, columnspan=2, sticky="w")

tk.Label(janela, text="Comentário:").grid(row=7, column=0, sticky="nw")
comentario = tk.Text(janela, height=4, width=40)
comentario.grid(row=7, column=1)

tk.Button(janela, text="Enviar", command=enviar).grid(row=8, columnspan=2, pady=10)

janela.mainloop()
