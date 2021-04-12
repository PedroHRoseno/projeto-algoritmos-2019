"""
Universidade Federal de Pernambuco
IF 969 - Algoritmos e estruturas de dados
Aluno: Pedro Henrique Roseno Bastos Silva
Projeto de Algoritmos I
"""




from bem import *
from lista import *
from candidato import *


class Controle:
    """
    Classe que controla todas as funções das outras classes
    """
   
    def __init__(self):
        self.listaDeCandidatos = ListaEncadeada()

    def lerArquivo(self, caminho, tipo):
        if tipo == "candidato":
            with open(caminho, "rt", encoding="latin-1") as arquivo:
                listaGrande = []
                flag = False
                for elemento in arquivo:
                    if flag:
                        palavras = elemento.split(";")
                        self.setarCandidato(palavras)
                    flag = True
                
            return self.listaDeCandidatos
        else:
            with open(caminho, "rt", encoding="latin-1") as arquivo:
                listaGrande = []
                flag = False
                for elemento in arquivo:
                    if flag:
                        palavras = elemento.split(";")
                        self.setarBem(palavras)
                    flag = True
                
            return self.listaDeCandidatos

        
    def setarCandidato(self, lista):
        candidato = Candidato()
        candidato.setAno(lista[2].replace('"', "")) 
        candidato.setSiglaUF(lista[10].replace('"', ""))
        candidato.setCodigo(lista[13].replace('"', ""))
        candidato.setDescricao(lista[14].replace('"', ""))
        candidato.setNome(lista[17].replace('"', ""))
        candidato.setId(lista[15].replace('"', ""))
        candidato.setNumero(lista[16].replace('"', ""))
        candidato.setCPF(lista[20].replace('"', ""))
        candidato.setNomeUrna(lista[18]).replace('"', "")
        candidato.setNumeroP(lista[27].replace('"', ""))
        candidato.setNomeP(lista[29].replace('"', ""))
        candidato.setSigla(lista[28].replace('"', ""))
        candidato.setCodigoO(lista[49].replace('"', ""))
        candidato.setDescricaoO(lista[50].replace('"', ""))
        candidato.setData(lista[38].replace('"', ""))
        candidato.setSexo(lista[41].replace('"', ""))
        candidato.setGrau(lista[42].replace('"', ""))
        candidato.setEstado(lista[44].replace('"', ""))
        candidato.setUF(lista[35].replace('"', ""))
        candidato.setMunicipio(lista[36].replace('"', ""))
        candidato.setSituacao(lista[23].replace('"', ""))
        candidato.setCandidatura(lista[25].replace('"', ""))
        candidato.setBens(ListaEncadeada())
        candidato.setTotalBens(0)
        self.listaDeCandidatos.append(candidato)
    
    def setarBem(self, lista):
        bem = Bem()
        bem.setCodigo(lista[13].replace('"', ""))
        bem.setDescricao(lista[14].replace('"', ""))
        bem.setDescricaoDetalhada(lista[15].replace('"', ""))
        bem.setValor(lista[16].replace('"', ""))
        self.setarCandidatoBem(lista[11].replace('"', ""), bem)
    
    def setarCandidatoBem(self, idCandidato, bem):
        ponteiro = self.listaDeCandidatos.cabeca
        while ponteiro is not None:
            if ponteiro.valor._Candidato__id == idCandidato:
                ponteiro.valor._Candidato__lista_bens.append(bem)
                ponteiro.valor.setarTotalBens()
            ponteiro = ponteiro.proximo

    
    def filtraCandidatoPartido(self, partido):
        lista = ListaEncadeada()
        for elemento in self.listaDeCandidatos:
            if elemento._Candidato__sigla == partido:
                lista.append(elemento)
        return lista

    def filtraCandidatoUF(self, uf):
        lista = ListaEncadeada()
        for elemento in self.listaDeCandidatos:
            if elemento._Candidato__siglaUF == uf:
                lista.append(elemento)
        return lista
    
    def filtraCandidatoMunicipio(self, municipio):
        lista = ListaEncadeada()
        for elemento in self.listaDeCandidatos:
            if elemento._Candidato__municipio == municipio:
                lista.append(elemento)
        return lista
    
    def filtraCandidatoCargo(self, cargo):
        lista = ListaEncadeada()
        for elemento in self.listaDeCandidatos:
            if elemento._Candidato__descricao == cargo:
                lista.append(elemento)
        return lista
    
    def filtraCandidatoBens(self, total):
        lista = ListaEncadeada()
        for elemento in self.listaDeCandidatos:
            elemento.setarTotalBens()
            if elemento._Candidato__totalBens >= total :
                lista.append(elemento)
        return lista

    def filtraCandidatoSituacao(self, situacao):
        lista = ListaEncadeada()
        for elemento in self.listaDeCandidatos:
            if elemento._Candidato__situacao >= situacao :
                lista.append(elemento)
        return lista
    
    def filtraCandidatoOcupacao(self, ocupacao):
        lista = ListaEncadeada()
        for elemento in self.listaDeCandidatos:
            if elemento._Candidato__descricao_ocupacao >= ocupacao :
                lista.append(elemento)
        return lista

    def filtraCandidatoAno(self, ano):
        lista = ListaEncadeada()
        for elemento in self.listaDeCandidatos:
            if elemento._Candidato__data >= ano :
                lista.append(elemento)
        return lista

    
    def mediaPorCargo(self, cargo):
        lista = self.filtraCandidatoCargo(cargo)
        total = 0
        for elemento in lista:
            total += elemento._Candidato__totalBens
        media = total / lista.tamanho
        return media

    def mediaPorUF(self, uf):
        lista = self.filtraCandidatoUF(uf)
        total = 0
        for elemento in lista:
            total += elemento._Candidato__totalBens
        media = total / lista.tamanho
        return media

    def mediaPorPartido(self, partido):
        lista = self.filtraCandidatoPartido(partido)
        total = 0
        for elemento in lista:
            total += elemento._Candidato__totalBens
        media = total / lista.tamanho
        return media

    def mediaPorOcupacao(self, Ocupacao):
        lista = self.filtraCandidatoOcupacao(ocupacao)
        total = 0
        for elemento in lista:
            total += elemento._Candidato__totalBens
        media = total / lista.tamanho
        return media

    def mediaPorAno(self, ano):
        lista = self.filtraCandidatoAno(ano)
        total = 0
        for elemento in lista:
            total += elemento._Candidato__totalBens
        media = total / lista.tamanho
        return media

    def remover(self, situacao):
        contador = 0
        for elemento in self.listaDeCandidatos:
            if elemento._Candidato__situacao_candidatura == situacao:
                self.listaDeCandidatos.pop(contador)
            contador +=1
        
if __name__ == "__main__":
    a = Controle()
    b = a.lerArquivo("consulta_cand_2014_PE.csv", "candidato")
    f = a.lerArquivo("bem_candidato_2014_PE.csv", "bem")
    print(a.listaDeCandidatos.tamanho)
    a.remover("DEFERIDO")
    print(a.listaDeCandidatos.tamanho)
    
         