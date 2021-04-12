from bem import *
from candidato import *

"""
Universidade Federal de Pernambuco
IF 969 - Algoritmos e estruturas de dados
Aluno: Pedro Henrique Roseno Bastos Silva
Sistemas de informação
"""

class Nodo:
  def __init__(self, valor=None, anterior=None, proximo=None):
    self.proximo = proximo
    self.anterior = anterior
    self.valor = valor

class ListaEncadeada:
  """
  Classe que guarda a posição do primeiro nodo.
  """

  def __init__(self, cabeca=None):
    self.cabeca = None
    self.tamanho = 0
  
  def append(self, item):
    """
    Adiciona um novo item no fim da lista, fila ou pilha
    """
    if self.cabeca:
      ponteiro = self.cabeca
      while(ponteiro.proximo is not None):
        ponteiro = ponteiro.proximo
      ponteiro.proximo = Nodo(item, ponteiro)
      self.tamanho += 1
    else:
      self.cabeca = Nodo(item)
      self.tamanho += 1


  def __str__ (self):
    """
    Retorna a string com todos os itens separados por vírgula
    """
    temp = ""
    ponteiro = self.cabeca
    while(ponteiro is not None):
      if ponteiro:
        temp += str(ponteiro.valor) + ", "
        ponteiro = ponteiro.proximo
    return temp
  
  def __repr__(self):
    string = self.__str__()
    return "ListaEncadeada({})".format(string)

  def _getnode(self, indice):
    """
    Ao dar um índice, move o ponteiro para a posição do nodo.
    """	
    ponteiro = self.cabeca
    for elemento in range(indice):
      if ponteiro is not None:
        ponteiro = ponteiro.proximo
      else:
        raise IndexError("índice não se encontra na lista")
    return ponteiro

  def __getitem__(self, indice):
    """
    Retorna um valor dado um determinado índice
    """
    ponteiro = self._getnode(indice)
    if ponteiro is not None:
      return ponteiro.valor
    else:
      raise IndexError("índice não se encontra na lista")
  
  def __setitem__(self, indice, elemento):
    """
    Altera um valor, dado um determinado índice.
    """
    ponteiro = self._getnode
    if ponteiro is not None:
      ponteiro.valor = elemento
    else:
      raise indexError("índice não se encontra na lista")

  def search(self, valor):
    """
    Dado um valor, o procura na lista.
    """
    ponteiro = self.cabeca
    for elemento in range(self.tamanho):
      if ponteiro is not None:
        if (ponteiro.valor == valor):
          return elemento
        ponteiro = ponteiro.proximo
      else:
        raise ValueError("Valor não se encontra na lista")
    if ponteiro is not None:
      return ponteiro.valor
    else:
      raise ValueError("Valor não se encontra na lista")

  def pop(self, indice):
    """
    Remove um elemento da lista dado um índice
    """
    ponteiro = self.cabeca
    for elemento in range(indice + 1):
      if ponteiro is not None:
        if elemento == indice:
          ponteiro.anterior.proximo = ponteiro.proximo
          ponteiro.proximo.anterior = ponteiro.anterior
          self.tamanho -= 1
          return ponteiro.valor
        else:
          ponteiro = ponteiro.proximo
      else:
        raise IndexError("índice não se encontra na lista")
    
  def inserirOrdenado(self, candidato, atributo):
    if atributo == "nome":
        if self.cabeca == None:
            self.cabeca = Nodo(candidato)
            self.tamanho += 1
        else:
            ponteiro = self.cabeca
            contador = 0
            while contador < self.tamanho:
                if ponteiro:
                    verificacao = candidato.OrdemAlfabetica(candidato, ponteiro.valor)
                    if verificacao == True:
                        self.inserir(contador, candidato)
                    ponteiro = ponteiro.proximo
                contador += 1

  
  def inserir(self, indice, valor):
    """
    Insere um valor na posição desejada.
    """
    if indice == 0:
      nodo = Nodo(valor)
      nodo.proximo = self.cabeca
      nodo.anterior = None
      self.cabeca = nodo
      self.tamanho += 1
    else:
      ponteiro = self._getnode(indice-1)
      nodo = Nodo(valor)
      nodo.proximo = ponteiro.proximo
      nodo.anterior = ponteiro
      ponteiro.proximo = nodo
      self.tamanho += 1 
  
  def concatenar(self, lista):
    """
    Une uma lista à outra
    """
    ponteiro = self._getnode(self.tamanho-1)
    ponteiro.proximo = lista.cabeca
    self.tamanho += lista.tamanho


class Pilha(ListaEncadeada):
  """
  Classe Pilha que altera o método pop da lista anterior.
  """
  
  def __init__(self):
    self.cabeca = None
    self.tamanho = 0

  def pop(self):
    ponteiro = self.cabeca
    if self.cabeca.proximo is None:
      print(self.cabeca.valor)
      self.cabeca = None
      self.tamanho -= 1
    elif self.cabeca is None:
      raise IndexError("Pilha vazia")
    else:
      while(ponteiro is not None):
        ponteiro = ponteiro.proximo
      if ponteiro is not None:
        ponteiro.anterior.proximo = None
        self.tamanho -= 1
      else:
        raise IndexError("pilha vazia")
  
  def append(self, item):
    if self.cabeca:
      ponteiro = self.cabeca
      while(ponteiro.proximo is not None):
        ponteiro = ponteiro.proximo
      ponteiro.proximo = Nodo(item, ponteiro)
      self.tamanho += 1
    else:
      self.cabeca = Nodo(item)
      self.tamanho += 1

  def inserir(self, indice, valor):
    return None

class Fila(ListaEncadeada):
  """
  Classe fila que altera o método pop da lista anterior.
  """

  def __init__(self):
    self.cabeca = None
    self.tamanho = 0

  def append(self, item):
    if self.cabeca:
      ponteiro = self.cabeca
      while(ponteiro.proximo is not None):
        ponteiro = ponteiro.proximo
      ponteiro.proximo = Nodo(item, ponteiro)
      self.tamanho += 1
    else:
      self.cabeca = Nodo(item)
      self.tamanho += 1
 
  def pop(self):
    ponteiro = self.cabeca
    if self.cabeca.proximo is None:
      print(self.cabeca.valor)
      self.cabeca = None
    elif self.cabeca is None:
      raise IndexError("filaa vazia")
    else:
      print(self.cabeca.valor)
      self.cabeca = self.cabeca.proximo
  
  def inserir(self, indice, valor):
    return None
  
  def _iter_(self):
    return Ponteiro(self)

class Ponteiro:
  def __init__(self, lista):
    self.posicao = lista.cabeca

  def __next__(self):
    ponteiro = self.posicao
    if ponteiro:
      self.posicao = ponteiro.proximo
      return ponteiro.valor
    else:
      raise StopIteration("StopIt")
  
  def _iter_(self):
    return self

if __name__ == "__main__":
    a = ListaEncadeada()
    print(a)