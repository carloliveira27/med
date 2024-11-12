import tkinter as tk

def calcularRiscoIdade(idade,ehHomem):
        idade = int(idade/5)
        risco = 0
        if (ehHomem == True):
            if(idade > 6):
                risco +=1
            if(idade > 7):
                risco+=2
            if(idade >9):
                risco+=1
            if(idade > 10):
                risco+=1
            if(idade > 13):
                risco+=1
            risco += idade - 6
            if(idade > 14):
                risco = 15
        else:
            if(idade > 6):
                risco +=1
            if(idade > 7):
                risco+=1
            if(idade >9):
                risco+=1
            risco += idade - 6
            if(idade > 14):
                risco = 12
        return risco

def calcularRiscoHdl(hdl):
    if(hdl>=60):
        return -2
    if(hdl>=50):
        return -1
    if(hdl>=45 ):
        return 0
    if(hdl>=35 ):
        return 1
    if(hdl<35):
        return 2
        
def calcularRiscoColesterol(colesterol,ehHomem):
    if(ehHomem):
        risco = 0
        if(colesterol < 160):
            return 0
        if(colesterol >= 280):
            return 4
        risco = int(colesterol/40) - 3
        return risco
    else:
        risco = 0
        if(colesterol < 160):
            return 0
        if(colesterol >= 280):
            return 4
        risco = int(colesterol/40) - 3
        if(colesterol > 199):
            risco+=1
        return risco
    
def calcularRiscoPressao(pressao,ehTratada,ehHomem):
    risco = 0
    if(ehHomem):
        if(pressao < 120):
            return (-2 + ehTratada*2)
        if(pressao >= 160):
            return (5 + ehTratada*2)
        risco = int(pressao/10) - 12
        risco += ehTratada*2
        if(pressao > 149):
            risco+=1
        return risco
    else:
        if(pressao < 120):
            return (-3 + ehTratada*2)
        if(pressao >= 160):
            return (3 + ehTratada*2)
        risco = int(pressao/10) - 12
        risco += ehTratada*2
        return risco

def calcularRiscoFumo(ehFumante,ehHomem):
    return (3*ehFumante + ehFumante*ehHomem)

def calcularRiscoDiabetes(ehDiabetico,ehHomem):
    return (4*ehDiabetico - ehDiabetico*(ehHomem))

def calcularRisco(idade,hdl,colesterol,pressao,ehTratada,ehFumante,ehDiabetico,ehHomem):
    risco = calcularRiscoColesterol(colesterol,ehHomem) + calcularRiscoDiabetes(ehDiabetico,ehHomem) + calcularRiscoFumo(ehFumante,ehHomem) + calcularRiscoHdl(hdl) + calcularRiscoIdade(idade,ehHomem) + calcularRiscoPressao(pressao,ehTratada,ehHomem)
    return risco

def calcularRiscoPercentual(pontos):
    if pontos <= -3:
        return 1.0
    elif pontos == -2:
        return 1.1
    elif pontos == -1:
        return 1.4
    elif pontos == 0:
        return 1.6
    elif pontos == 1:
        return 1.9
    elif pontos == 2:
        return 2.3
    elif pontos == 3:
        return 2.8
    elif pontos == 4:
        return 3.3
    elif pontos == 5:
        return 3.9
    elif pontos == 6:
        return 4.7
    elif pontos == 7:
        return 5.6
    elif pontos == 8:
        return 6.7
    elif pontos == 9:
        return 7.9
    elif pontos == 10:
        return 9.4
    elif pontos == 11:
        return 11.2
    elif pontos == 12:
        return 13.2
    elif pontos == 13:
        return 15.6
    elif pontos == 14:
        return 18.4
    elif pontos == 15:
        return 21.6
    elif pontos == 16:
        return 25.3
    elif pontos == 17:
        return 29.4
    else:  # pontos >= 18
        return 30.0

class Application:
    def __init__(self,master = None):
        master.geometry("800x600")
        self.widget1 = tk.Frame(master)
        self.widget1.pack()
        self.msg = tk.Label(self.widget1,text="Calculadora de risco")
        self.msg.pack()

        self.master = master
        
        self.ehHomem = True
        self.ehFumante = False
        self.ehDiabetico = False
        self.ehTratado = True

        self.msgGenero = tk.Label(master)
        self.msgGenero["text"] = "Homem"
        self.msgGenero.pack()

        self.butaoGenero = tk.Button(master)
        self.butaoGenero["text"] = "Mudar Genero"
        self.butaoGenero.bind("<Button-1>",self.mudarGenero)
        self.butaoGenero.pack()

        self.msgFumo = tk.Label(master)
        self.msgFumo["text"] = "Não fuma"
        self.msgFumo.pack()

        self.butaoFumo = tk.Button(master)
        self.butaoFumo["text"] = "Mudar situação de fumo"
        self.butaoFumo.bind("<Button-1>",self.mudarFumo)
        self.butaoFumo.pack()

        self.msgDiabetes = tk.Label(master)
        self.msgDiabetes["text"] = "Não tem diabetes"
        self.msgDiabetes.pack()

        self.butaoDiabetes = tk.Button(master)
        self.butaoDiabetes["text"] = "Mudar situação de diabetes"
        self.butaoDiabetes.bind("<Button-1>",self.mudarDiabetes)
        self.butaoDiabetes.pack()

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
        self.msg = tk.Label(self.widget3,text="Digite sua taxa de HDL-C")
        self.msg.pack()

        self.terceiroContainer = tk.Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.hdl = tk.Entry(self.terceiroContainer)
        self.hdl["width"] = 30
        self.hdl.pack()
    
        self.widget4 = tk.Frame(master)
        self.widget4.pack()
        self.msg = tk.Label(self.widget4,text="Digite sua taxa de colesterol")
        self.msg.pack()

        self.quartoContainer = tk.Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.colesterol = tk.Entry(self.quartoContainer)
        self.colesterol["width"] = 30
        self.colesterol.pack()

        self.widget5 = tk.Frame(master)
        self.widget5.pack()
        self.msg = tk.Label(self.widget5,text="Digite sua pressão artérial sistólica")
        self.msg.pack()

        self.quintoContainer = tk.Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.pressao = tk.Entry(self.quintoContainer)
        self.pressao["width"] = 30
        self.pressao.pack()

        self.msgPressao = tk.Label(master)
        self.msgPressao["text"] = "Tratado"
        self.msgPressao.pack()

        self.butaoPressao = tk.Button(master)
        self.butaoPressao["text"] = "Mudar situação de tratamento"
        self.butaoPressao.bind("<Button-1>",self.mudarPressao)
        self.butaoPressao.pack()

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

    def mudarFumo(self,event):
        if self.msgFumo["text"] == "Não fuma":
            self.msgFumo["text"] = "Fuma"
            self.ehFumante = True
        else:
            self.msgFumo["text"] = "Não Fuma"
            self.ehFumante = False

    def mudarDiabetes(self,event):
        if self.msgDiabetes["text"] == "Não tem diabetes":
            self.msgDiabetes["text"] = "Tem diabetes"
            self.ehDiabetico = True
        else:
            self.msgDiabetes["text"] = "Não tem diabetes"
            self.ehDiabetico = False

    def mudarPressao(self,event):
        if self.msgPressao["text"] == "Tratado":
            self.msgPressao["text"] = "Não Tratado"
            self.ehTratado = False
        else:
            self.msgPressao["text"] = "Tratado"
            self.ehTratado = True

    def calcular(self, event):

        try:
            idade = int(self.idade.get())
            if idade < 35:
                self.msgtaxa["text"] = "Digite uma idade válida (35 ou mais)"
                return
        except ValueError:
            self.msgtaxa["text"] = "Digite uma idade válida"
            return
        
        try:
            hdl = int(self.hdl.get())
        except ValueError:
            self.msgtaxa["text"] = "Digite uma taxa de hdl válida"
            return
        
        try:
            colesterol = int(self.colesterol.get())
        except ValueError:
            self.msgtaxa["text"] = "Digite uma taxa de colesterol válida"
            return
        
        try:
            pressao = int(self.pressao.get())
        except ValueError:
            self.msgtaxa["text"] = "Digite uma taxa de pressao válida"
            return
        

        taxa = calcularRisco(idade,hdl,colesterol,pressao,self.ehTratado,self.ehFumante,self.ehDiabetico,self.ehHomem)
        porcento = calcularRiscoPercentual(taxa)
        self.msgtaxa["text"] = f"Risco Percentual: {porcento:.2f}"
        if(porcento < 5):
            self.msgGrupo["text"] = "Risco Baixo"
        elif((porcento < 20 and self.ehHomem) or (porcento < 10 and self.ehHomem == False)):
            self.msgGrupo["text"] = "Risco Intermediário"
        else:
            self.msgGrupo["text"] = "Risco Alto"


root = tk.Tk()
Application(root)
root.mainloop()
