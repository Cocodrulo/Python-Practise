class LinkedList:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

    def __init__(self):
        self.__first = None
        self.__last = None
        self.__len = 0

    def __len__(self):
        return self.__len

    def __str__(self):
        linkedlist = "["+str(self.__first.value)+"]"
        current_node = self.__first.next_node
        while current_node is not None:
            linkedlist += " -> ["+ str(current_node.value)+"]"
            current_node = current_node.next_node
        return linkedlist

    def insert(self, value):
        if value is None:
            raise ValueError("El valor no puede ser nulo!!")

        if self.__first is not None:
            new_node = self.Node(value, next_node=self.__first)
            self.__first = new_node
        else:
            self.__first = self.Node(value)
            self.__last = self.__first
        self.__len +=1 

    def different_values(self):
        pass