"""
    Implementar uma função que receba uma lista de listas de comprimentos
    quaisquer e retorne uma lista de uma dimensão.
"""

def retornaLista(l):
    a = []
    for i in l:
        if isinstance(i,list):
            retornaLista(i)
	else:
            a.append(i)
