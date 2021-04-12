from bem import *
from lista import *

class Candidato:
    def __init__(self):
        self.__anoE = 0
        self.__siglaUF = ""
        self.__codigo = 0
        self.__descricao = ""
        self.__nome_candidato = ""
        self.__id = 0
        self.__numero_urna = 0
        self.__cpf = 0
        self.__nome_urna = ""
        self.__numero_partido = 0
        self.__nome_partido = ""
        self.__sigla = ""
        self.__codigo_ocupacao = ""
        self.__descricao_ocupacao = ""
        self.__data = 0
        self.__sexo = ""
        self.__grau = ""
        self.__estado = ""
        self.__uf = ""
        self.__municipio = ""
        self.__situacao = ""
        self.__situacao_candidatura = ""
        self.__lista_bens = None
        self.__totalBens = 0
    
    def setarTotalBens(self):
        self.__totalBens = 0
        for elemento in self.__lista_bens:
            self.__totalBens += float(elemento._Bem__valor.replace(",", "."))
    
    def incluirBem(self, item):
        __lista_bens.inserirOrdenado(item, "bem")
        self.totalBens += item.__valor

    def __str__(self):
        return " {} -- {} -- {} \n {} ({}) - {} ({}) \n Resumo dos bens: \n  - Total declarado: R$ {} \n  - Total por tipo: {}".format(self.__nome_urna, self.__numero_urna, self.__sigla, self.__descricao_ocupacao, self.__siglaUF, self.__municipio, self.__uf, self.__totalBens, self.__lista_bens)
    
    def __repr__(self):
        pass
    
# ---------- COMPARAÇÕES --------------#

    def OrdemAlfabetica(self, cd1, cd2):
        a = cd1.__nome_candidato
        b = cd2.__nome_candidato
        if len(a) > len(b):
            for elemento in range(0, len(a)  - len(b)):
                b += " "
        cont = 0
        for elemento in a:
            if elemento > b[cont]:
                return True
            elif elemento < b[cont]:
                return False
        
        cpf1 = cd1.__cpf
        cpf2 = cd2.__cpf
        if cpf1 > cpf2:
            return True
        else:
            return False
    
    def totalBens(self, cd1, cd2):

        a = int(cd1.__totalBens)
        b = int(cd2.__totalBens)
        if a > b:
            return True
        elif a < b:
            return False
        else:
            porNome = OrdemAlfabetica(cd1.__nome_candidato, cd2.__nome_candidato)
            return porNome

    def partido(self, cd1, cd2):
        a = cd1.__numero_partido
        b = cd2.__numero_partido
        if a > b:
            return True
        elif a < b:
            return False
        else:
            porNome = OrdemAlfabetica(cd1.__nome_candidato, cd2.__nome_candidato)
            return porNome

    def data(self, cd1, cd2):
        #24/07/2000
        data1 = (cd1.__data[5:] + cd1.__data[3:5] + cd1.__data[0:2])
        data2 = (cd2.__data[5:] + cd2.__data[3:5] + cd2.__data[0:2])
        #Ano
        if data1 > data2:
            return True
        elif data1 < data2:
            return False
        else:
            porNome = OrdemAlfabetica(cd1.__nome_candidato, cd2.__nome_candidato)
            return porNome          

#------------------ SET ABAIXO ----------------#

    def setAno(self, valor):
        self.__anoE = valor
        return self.__anoE
    
    def setSiglaUF(self, valor):
        self.__siglaUF = valor
        return self.__siglaUF
    
    def setCodigo(self, valor):
        self.__codigo = valor
        return self.__sigla

    def setDescricao(self, valor):
        self.__descricao = valor
        return self.__descricao

    def setNome(self, valor):
        self.__nome_candidato = valor
        return self.__nome_candidato

    def setId(self, valor):
        self.__id = valor
        return self.__id

    def setNumero(self, valor):
        self.__numero_urna = valor
        return self.__numero_urna

    def setCPF(self, valor):
        self.__cpf = valor
        return self.__cpf

    def setNomeUrna(self, valor):
        self.__nome_urna = valor
        return self.__nome_urna
        
    def setNumeroP(self, valor):
        self.__numero_partido = valor
        return self.__numero_partido

    def setNomeP(self, valor):
        self.__nome_partido = valor
        return self.__nome_partido

    def setSigla(self, valor):
        self.__sigla = valor
        return self.__sigla

    def setCodigoO(self, valor):
        self.__codigo_ocupacao = valor
        return self.__codigo_ocupacao

    def setDescricaoO(self, valor):
        self.__descricao_ocupacao = valor
        return self.__descricao_ocupacao

    def setData(self, valor):
        self.__data = valor
        return self.__data

    def setSexo(self, valor):
        self.__sexo = valor
        return self.__sexo

    def setGrau(self, valor):
        self.__grau = valor
        return self.__grau

    def setEstado(self, valor):
        self.__estado = valor
        return self.__estado

    def setUF(self, valor):
        self.__uf = valor
        return self.__uf

    def setMunicipio(self, valor):
        self.__municipio = valor
        return self.__municipio

    def setSituacao(self, valor):
        self.__situacao = valor
        return self.__situacao

    def setCandidatura(self, valor):
        self.__situacao_candidatura = valor
        return self.__situacao_candidatura

    def setBens(self, valor):
        self.__lista_bens = valor
        return self.__lista_bens
    
    def setTotalBens(self, valor):
        self.__totalBens = valor
        return self.__totalBens


#----------------------------- GET ABAIXO ------------------------#        

    def getAno(self):

        return self.__anoE
    
    def getSiglaUF(self):

        return self.__siglaUF
    
    def getCodigo(self):

        return self.__sigla

    def getDescricao(self):

        return self.__descricao

    def getNome(self):

        return self.__nome_candidato

    def getId(self):

        return self.__id

    def getNumero(self):

        return self.__numero_urna

    def getCPF(self):

        return self.__cpf

    def getNomeUrna(self):

        return self.__nome_urna
        
    def getNumeroP(self):

        return self.__numero_partido

    def getNomeP(self):

        return self.__nome_partido

    def getSigla(self):

        return self.__sigla

    def getCodigoO(self):

        return self.__codigo_ocupacao

    def getDescricaoO(self):

        return self.__descricao_ocupacao

    def getData(self):

        return self.__data

    def getSexo(self):

        return self.__sexo

    def getGrau(self):

        return self.__grau

    def getEstado(self):

        return self.__estado

    def getUF(self):

        return self.__uf

    def getMunicipio(self):

        return self.__municipio

    def getSituacao(self):

        return self.__situacao

    def getCandidatura(self):

        return self.__situacao_candidatura

    def getBens(self):

        return self.__lista_bens

