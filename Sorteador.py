import customtkinter as ctk
import tkinter
from tkinter import messagebox
from random import randint

janela = ctk.CTk()
janela.title('SORTEADOR')
janela.geometry('700x400')
janela.resizable(True, True)

lista = list()
def sortear(x):
    if x.isnumeric():
        rep = int(x)

    try:
        for i in range (0, rep):
            lista.append(i)
    except (KeyboardInterrupt, ValueError):
        messagebox.showerror('ERRO', 'FALHA AO REGISTRAR NÚMEROS')

    numb = randint(0,len(lista))

    sorteado = ctk.CTkLabel(resp, width=15,text=f'{numb}',
                   font=('Arial', 30, 'bold'))

    sorteado.pack(padx=3, pady=5)


texto = ctk.CTkLabel(janela, text='Quantidade de números', text_color='RED')
texto.pack()
numb_rep = ctk.CTkEntry(janela, width=50)
numb_rep.pack()
button = ctk.CTkButton(janela, text='Sortear', command=lambda: sortear(numb_rep.get()), hover_color='green',fg_color='black')
button.pack(padx=10,pady=10)
resp =ctk.CTkFrame(janela)
resp.pack()














janela.mainloop()