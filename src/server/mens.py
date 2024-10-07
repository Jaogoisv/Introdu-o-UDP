from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from socket import *

def janela(ende,port):
    mensa = Tk()
    mensa.title("Chat")
    mensa.resizable(False, False)


    def titulo():
        texto = Label(mensa, text="Endereço: ")
        texto.grid(row=0, column=0, padx=5, pady=1)
        texto = Label(mensa, text="Porta: ")
        texto.grid(row=1, column=0, padx=5, pady=1)
        texto = Label(mensa, text=ende)
        texto.grid(row=0, column=1, padx=5, pady=1)
        texto = Label(mensa, text=port)
        texto.grid(row=1, column=1, padx=5, pady=1)

    def mensagem():
        
        his = Text(mensa, height=15, width=40)
        his.config(state=DISABLED)
        his.grid(row=2, column = 0, columnspan=4, padx=2, pady=2)
        barra = Scrollbar(mensa, command=his.yview)
        barra.grid(row=2,column=3)
        his.config(yscrollcommand=barra.set)

        texto = Label(mensa, text = "Mensagem:")
        texto.grid(row=3, column=0, padx=5, pady=2)
        mes = Text(mensa, height=4, width=30)
        mes.grid(row=4, column=0, columnspan=3, padx=5, pady=2)

        def envia(mes, his):
            dado = mes.get("1.0", "end-1c")
            mes.delete("1.0",END)
            
            if (dado == ""):
                messagebox.showwarning("Atenção", "mensagem sem caractere")
            else:
                his.tag_configure("verde", foreground="green")
                his.tag_configure("azul", foreground="blue")
                his.tag_configure("preot", foreground="black")


                inicio = "Você digitou:"
                quebra = "----------------------------------------"

                his.config(state=NORMAL)
                his.insert(END,f"\n{quebra}","verde")
                his.insert(END,f"\n{inicio}","verde")
                his.insert(END,f"\n{dado}","black")
                his.insert(END,f"\n{quebra}","verde")
                his.config(state=DISABLED)


                status.config(state=NORMAL)
                status.delete("1.0",END)
                status.insert(END,"mensagem enviada", "verde")
                status.config(state=DISABLED)

                def conectar(ende, port, dado):
                    sever_name = ende
                    sever_port = int(port)

                    clientsocket = socket(AF_INET, SOCK_DGRAM)
                    message = dado

                    message = str(message).encode('utf-8')
                    print (type(message))
                    clientsocket.sendto(message,(sever_name,sever_port))

                    modified_message, severAddress = clientsocket.recvfrom(2048)
                    modified_message = modified_message.decode('utf-8')

                    recebe (modified_message)

                conectar(ende, port, dado)

        def recebe(rece):
            his.tag_configure("verde", foreground="green")
            his.tag_configure("azul", foreground="blue")
            his.tag_configure("preot", foreground="black")

            inicio = "texto que voltou:"
            quebra = "----------------------------------------"

            his.config(state=NORMAL)
            his.insert(END,f"\n{quebra}","azul")
            his.insert(END,f"\n{inicio}","azul")
            his.insert(END,f"\n{rece}","black")
            his.insert(END,f"\n{quebra}","azul")
            his.config(state=DISABLED)

        enviar = Button(mensa, text="enviar", height=4, width= 9, command= lambda : envia(mes,his))
        enviar.grid(row=4, column=3, padx=2, pady=2)


        texto = Label(mensa, text="Status")
        texto.grid(row=5, column=0, padx=2, pady=2)

        status = Text(mensa, height=1,width=20)
        status.tag_configure("vermelho", foreground="red")
        status.tag_configure("verde", foreground="green")
        status.tag_configure("azul", foreground="blue")
        status.grid(row=5,column=1,columnspan=2,padx=5,pady=2)
        status.insert(END,"Aguardando...","azul")
        status.config(state=DISABLED)

    titulo()
    mensagem()
    mensa.mainloop()

