# pedro paulo de oliveira rocha - Entregavel Python POO
import pandas as pd
import time
import os
def PrintLine():
    print("_____________________________________________________________")

#definicao da classe dos objetos Auvs
class Auvs:
    #construtor com todos os atributos/caracteristicas (privados) dos objetos
    def __init__(self, numeroThursters, sensores, anoConstrucao, nome, peso):
        self.__numeroThursters = numeroThursters
        self.__sensores = sensores
        self.__anoConstrucao = anoConstrucao
        self.__nome = nome
        self.__peso = peso

    #metodos para que outras classes acessem os atributos privados
    def GetPeso(self):
        return self.__peso
    
    def GetNome(self):
        return self.__nome
    
    def GetAnoConstrucao(self):
        return self.__anoConstrucao
    
    def GetNumeroThursters(self):
        return self.__numeroThursters
    
    def GetSensores(self):
        return self.__sensores

#classe que pode descrever os objetos da classe Auvs
class Descritor:
    #o construtor recebe uma quantidade variavel de parametros, flexibilizando o codigo
    def __init__ (self, *args, **kwargs):
        self.array = args #vetor de objetos que a classe Descritor vai descrever

        #atributo privado utilizado para guardar os dados dos objetos recebidos,
        # para exibicao de tabelas com o pandas ##
        self.__data = {
            "Nome": [],
            "Sensores": [],
            "Numero de Thurstes": [],
            "Ano de Construcao": [],
            "Peso": [],
        }

        #inicializando __data pedindo aos objetos recebidos seus dados
        for objeto in self.array:
            self.__data["Ano de Construcao"].append(objeto.GetAnoConstrucao())
            self.__data["Numero de Thurstes"].append(objeto.GetNumeroThursters())
            self.__data["Sensores"].append(objeto.GetSensores())
            self.__data["Peso"].append(objeto.GetPeso())
            self.__data["Nome"].append(objeto.GetNome())

    def ExibirTabelaAUVS(self):
        # Exibe uma pabela com todos os dados dos objetos recebidos
        data = self.__data
        tabela = pd.DataFrame(data)
        PrintLine()
        print("\n",tabela,"\n")
        PrintLine()
        time.sleep(4)
        return 0

    def ExibirIndividualmenteAUVS(self):
        #Exibe dados de um objeto individualmente

        print("\nEscolha um dos AUVs listados abaixo:")
        print(self.__data["Nome"])
        
        nome = input("Nome escolhido: ")#Pedindo ao usuario um nome

        
        if nome in self.__data["Nome"]:
            indice = self.__data["Nome"].index(nome)
            
            data = {
            "Nome selecionnado":[self.__data["Nome"][indice]],
            "Sensores":[self.__data["Sensores"][indice]],
            "Numero de Thurstes": [self.__data["Numero de Thurstes"][indice]],
            "Ano de Construcao": [self.__data["Ano de Construcao"][indice]],
            "Peso": [self.__data["Peso"][indice]],
            }

            tabela = pd.DataFrame(data)
            print ("\n",tabela,"\n")
        
        else:
            #se o nome pedido nao for um objeto conhecido, mensagem de erro
            print(f"\nErro! O AUV {nome} nao existe!\n")

        PrintLine()
    
        time.sleep(4)
        return 0
    
    def RankDeIdade(self):
        #Exibe os objetos ordenados por idade/tempo de producao
        anoConstrucaoOrdenado = self.__data["Ano de Construcao"].copy() #variavel copia, que sera ordenada para organizacao dos dados
        anoConstrucaoOrdenado.sort(reverse = True) #lista odenada das idadades
    
        data = {
                "Nome":[],
                "Ano de Construcao": [],
                "Idade (anos)":[],
                } 
        
        for indiceAno in range(0,  len(anoConstrucaoOrdenado)):
            #condicional para tratar casos de empate
            if (indiceAno != (len(anoConstrucaoOrdenado)-1)) and\
                (anoConstrucaoOrdenado[indiceAno] == anoConstrucaoOrdenado[indiceAno+1]):
                continue

            for indice in range(0, len(self.__data["Ano de Construcao"])):
                if anoConstrucaoOrdenado[indiceAno] == self.__data["Ano de Construcao"][indice]:
                    data["Ano de Construcao"].append(self.__data["Ano de Construcao"][indice])
                    data["Nome"].append(self.__data["Nome"][indice])
                    data["Idade (anos)"].append(2023 - self.__data["Ano de Construcao"][indice])


        print("\nRank de idade dos AUVs (do mais novo para o mais antigo) \n")
        tabela = pd.DataFrame(data)
        print(tabela,"\n")
        PrintLine() 
                
        time.sleep(4)
        return 0
    
    def RankDistribuicaoPeso(self):
        
        #rankea os Auvs de acordo com a quantidade de peso que cada propulsor precisa "carregar"
        data = {
                "Nome":[],
                "Distribuicao de Peso": [],
                "Ano de Construcao": [],
                }
        
        for indice in range(0,len(self.__data["Nome"])):
            data["Distribuicao de Peso"].append(self.__data["Peso"][indice]/self.__data["Numero de Thurstes"][indice])
        #atribuindo as razoes peso/propulsor

        
        data["Distribuicao de Peso"].sort()
        
        for indiceDistribuicaoPeso in range(0, len(data["Distribuicao de Peso"])):
            #tratamento para casos de empate
            if indiceDistribuicaoPeso != (len(data["Distribuicao de Peso"])-1) and \
                (data["Distribuicao de Peso"][indiceDistribuicaoPeso] == data["Distribuicao de Peso"][indiceDistribuicaoPeso+1]):
                continue

            for indice in range(0, len(self.__data["Nome"])):
                if (self.__data["Peso"][indice]/self.__data["Numero de Thurstes"][indice]) ==\
                    data["Distribuicao de Peso"][indiceDistribuicaoPeso]:
                    
                    data["Nome"].append(self.__data["Nome"][indice])
                    data["Ano de Construcao"].append(self.__data["Ano de Construcao"][indice])
        
        tabela = pd.DataFrame(data)
        print("\nRank da distribuicao de peso por propulsores dos AUVs (da maior distribuicao para menor)\n")  
        print(tabela,"\n")   
        PrintLine()
                
        time.sleep(4)
        return 0
    
def Main ():
    os.system("clear")
    AUV1 = Auvs(6, ["Pressure sensor", "Camera", "Hydrophone"], 2020, "BrHUE", 40)
    AUV2 = Auvs(8, ["External pressure sensor", "Internal pressure sensor", "Camera", "Hydrophone"], 2022, "Lua", 30)
    AUV3 = Auvs(3, ["Camera"], 2016, "Vovozao", 20)
    AUV4 = Auvs(8, ["Lydar", "Acelerometre", "Camera"], 2023, "Titan", 30)
    descricao = Descritor (AUV1, AUV2, AUV3, AUV4)
    descricao.ExibirTabelaAUVS()
    descricao.ExibirIndividualmenteAUVS()
    descricao.RankDeIdade()
    descricao.RankDistribuicaoPeso()
    return 0

Main()