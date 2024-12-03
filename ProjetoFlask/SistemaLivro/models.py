'''Este arquivo é responsável pela estrutura de fila da biblioteca'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class FilaLigada:
    def __init__(self):
        self.head = None
        self.tail = None

    def enfileirar(self, data):
        novo_no = Node(data)
        if not self.tail:
            self.head = novo_no
        else:
            self.tail.next = novo_no
        self.tail = novo_no

    def desenfileirar(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return data

    def is_empty(self):
        return self.head is None


