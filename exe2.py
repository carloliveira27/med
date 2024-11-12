import tkinter as tk
    
def calcularFiltracao(creatina,idade,ehHomem,ehNegro):
    if ehHomem == True:
        k = 0.7
        a = -0.411
    else:
        k = 0.9
        a = -0.329
    taxa = 141*(min(creatina/k,1)**a)*(max(creatina/k,1)**-1.209)*(0.993**idade)
    if ehHomem == False:
        taxa *= 1.018
    if ehNegro == True:
        taxa*= 1.159
    return taxa  

class Application:
    def __init__(self,master = None):
        master.geometry("600x400")
        self.widget1 = tk.Frame(master)
        self.widget1.pack()
        self.msg = tk.Label(self.widget1,text="Primeiro widget")
        self.msg.pack()

        self.master = master
        
        self.ehHomem = True
        self.ehNegro = False

        self.msgGenero = tk.Label(master)
        self.msgGenero["text"] = "Homem"
        self.msgGenero.pack()

        self.butaoGenero = tk.Button(master)
        self.butaoGenero["text"] = "Mudar Genero"
        self.butaoGenero.bind("<Button-1>",self.mudarGenero)
        self.butaoGenero.pack()

        self.msgEtinia = tk.Label(master)
        self.msgEtinia["text"] = "Branco"
        self.msgEtinia.pack()

        self.butaoEtinia = tk.Button(master)
        self.butaoEtinia["text"] = "Mudar Etinia"
        self.butaoEtinia.bind("<Button-1>",self.mudarEtinia)
        self.butaoEtinia.pack()

        self.widget2 = tk.Frame(master)
        self.widget2.pack()
        self.msg = tk.Label(self.widget2,text="Digite sua idade")
        self.msg.pack()

        self.segundoContainer = tk.Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.idade = tk.Entry(self.segundoContainer)
        self.idade["width"] = 30
        self.idade.pack()

        self.widget3 = tk.Frame(master)
        self.widget3.pack()
        self.msg = tk.Label(self.widget3,text="Digite sua taxa de creatina")
        self.msg.pack()

        self.terceiroContainer = tk.Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.creatina = tk.Entry(self.terceiroContainer)
        self.creatina["width"] = 30
        self.creatina.pack()

        self.butao = tk.Button(master)
        self.butao["text"] = "Calcular taxa"
        self.butao.bind("<Button-1>",self.calcular)
        self.butao.pack()

        self.msgtaxa = tk.Label(master)
        self.msgtaxa["text"] = " "
        self.msgtaxa.pack()

        self.msgGrupo = tk.Label(master)
        self.msgGrupo["text"] = " "
        self.msgGrupo.pack()



    def mudarGenero(self,event):
        if self.msgGenero["text"] == "Homem":
            self.msgGenero["text"] = "Mulher"
            self.ehHomem = False
        else:
            self.msgGenero["text"] = "Homem"
            self.ehHomem = True

    def mudarEtinia(self,event):
        if self.msgEtinia["text"] == "Branco":
            self.msgEtinia["text"] = "Negro"
            self.ehNegro = True
        else:
            self.msgEtinia["text"] = "Branco"
            self.ehNegro = False

    def calcular(self, event):

        try:
            idade = int(self.idade.get())
        except ValueError:
            self.msgtaxa["text"] = "Digite uma idade válida"
            return
        

        try:
            creatina = int(self.creatina.get())
        except ValueError:
            self.msgtaxa["text"] = "Digite uma taxa de creatina válida"
            return

        taxa = calcularFiltracao(creatina, idade, self.ehHomem, self.ehNegro)
        self.msgtaxa["text"] = f"Taxa de Filtração: {taxa:.2f}"
        grupo = int(taxa / 15)
        match grupo:
            case 0:
                self.msgGrupo["text"] = "Você está no estágio G5, seu diagnóstico é de Falência Renal"
            case 1:
                self.msgGrupo["text"] = "Você está no estágio G4, seu diagnóstico é de Redução Severa"
            case 2:
                self.msgGrupo["text"] = "Você está no estágio G3b, seu diagnóstico é de Redução Discreta-Severa"
            case 3:
                self.msgGrupo["text"] = "Você está no estágio G3a, seu diagnóstico é de Redução Discreta-Moderada"
            case 4:
                self.msgGrupo["text"] = "Você está no estágio G2, seu diagnóstico é de Redução Discreta"
            case _:
                self.msgGrupo["text"] = "Você está no estágio G1, seu diagnóstico é de Normal"

root = tk.Tk()
Application(root)
root.mainloop()
