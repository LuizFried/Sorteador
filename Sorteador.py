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
            for i in range(0, rep):
                lista.append(i)
        except (KeyboardInterrupt, ValueError):
            messagebox.showerror('ERRO', 'FALHA AO REGISTRAR NÚMEROS')

        numb = randint(1, len(lista))

        resp.configure(text=f'{numb}')
        lista.clear()

    else:
        messagebox.showerror('ERRO', 'DIGITE UMA VALOR VÁLIDO')


texto = ctk.CTkLabel(janela, text='Quantidade de números', text_color='RED')
texto.pack(padx=10, pady=10)

numb_rep = ctk.CTkEntry(janela, width=50)
numb_rep.pack(padx=10, pady=10)

button = ctk.CTkButton(janela, text='Sortear', command=lambda: sortear(numb_rep.get()), hover_color='green',
                       fg_color='black')
button.pack(padx=10, pady=10)

resp = ctk.CTkLabel(janela, text=' ', text_color='red', width=50, font=('arial', 35))
resp.pack(padx=10, pady=10)


janela.mainloop()