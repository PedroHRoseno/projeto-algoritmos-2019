from lista import *
from candidato import *

class Bem:
    def __init__(self):
        self.__codigo_tipo = 0
        self.__descricao_bem = "" 
        self.__descricao_detalhada = "" 
        self.__valor = 0
    
    def setCodigo(self, valor):
        self.__codigo_tipo = valor
        return self.__codigo_tipo
    
    def setDescricao(self, valor):
        self.descricao_bem = valor
        return self.__descricao_bem

    def setDescricaoDetalhada(self, valor):
        self.__descricao_detalhada = valor
        return self.__descricao_detalhada

    def setValor(self, valor):
        self.__valor = valor
        return self.__valor

    def getCodigo(self):
        return self.__codigo_tipo
    
    def getDescricao(self):
        return self.descricao_bem

    def getDescricaoDetalhada(self):
        return self.descricao_detalhada

    def getValor(self):
        return self.valor
    
    def __str__(self):
        return "{} ---- {} ------ R$ {} Descrição: {} ".format(self.__codigo_tipo, self.__descricao_bem, self.__valor,  self.__descricao_detalhada)

    def __repr__(self):
        return "{} ---- {} ------ R$ {} Descrição: {} \n".format(self.__codigo_tipo, self.__descricao_bem, self.__valor,  self.__descricao_detalhada)
    
    def compara(self, bem1, bem2):
        if bem1.__valor > bem2__valor:
            return True
        elif bem1.__valor < bem2__valor:
            return False
        elif bem1.__valor == bem2__valor:
            if bem1.__codigo_tipo > bem2.__codigo_tipo:
                return True
            elif bem1.__codigo_tipo < bem2.__codigo_tipo:
                return False
            elif bem1.__codigo_tipo == bem2.__codigo_tipo:
                if len(bem1.__descricao_detalhada) > len(bem2.__descricao_detalhada):
                    True
                elif len(bem1.__descricao_detalhada) < len(bem2.__descricao_detalhada):
                    False
                else:
                    return None
        
            




    
    
        