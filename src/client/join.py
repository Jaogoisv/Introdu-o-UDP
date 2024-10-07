from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mes import janela as mensagemm

def inicio():
    tela = Tk()
    tela.title("entrar")
    tela.resizable(False, False)


    def botao():

        texto = Label(tela, text="Endereço: ")
        texto.grid(row=0, column=0, padx=5, pady=2)
        texto = Label(tela, text="porta: ")
        texto.grid(row=1, column=0, padx=10, pady=2)

        ende = Text(tela, height=1, width=15)
        ende.grid(row=0, column=1, padx=5, pady=2)
        port = Text(tela, height=1, width=15)
        port.grid(row=1, column=1, padx=5, pady=2)

        def mes():
            endereco = ende.get("1.0", "end-1c")
            porta = port.get("1.0", "end-1c")
            if (endereco == ""):
                messagebox.showwarning("Atenção", "Endereço  não econtrado")
            elif (porta == ""):
                messagebox.showwarning("Atenção", "Porta não encontrada")
            else:
                tela.destroy()
                mensagemm(endereco,porta)

        entrar = ttk.Button(text="Entrar",command=mes)
        entrar.grid(row=2, column=0, columnspan=2, padx=5 ,pady=2)


    botao()
    tela.mainloop()
inicio()