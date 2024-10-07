from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import socket
import servidors as sev


def inicio():
    tela = Tk()
    tela.title("criar")
    tela.resizable(False, False)


    def botao():
        
        host = socket.gethostname()
        ip = socket.gethostbyname(host)

        texto = Label(tela, text="Endereço: ")
        texto.grid(row=0, column=0, padx=5, pady=2)
        texto = Label(tela, text="porta: ")
        texto.grid(row=1, column=0, padx=10, pady=2)

        ende = Label(tela, text = ip)
        ende.grid(row=0, column=1, padx=5, pady=2)
        port = Text(tela, height=1, width=15)
        port.grid(row=1, column=1, padx=5, pady=2)

        def mes():
            porta = port.get("1.0", "end-1c")
            if (porta == ""):
                messagebox.showwarning("Atenção", "Porta não encontrada")
            else:
                sev.servidor(porta)
                port.config(state=DISABLED)

        entrar = ttk.Button(text="Entrar",command=mes)
        entrar.grid(row=2, column=0, columnspan=2, padx=5 ,pady=2)


    botao()
    tela.mainloop()
inicio()