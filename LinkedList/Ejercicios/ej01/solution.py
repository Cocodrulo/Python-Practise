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
        # Create a new list
        new_list = LinkedList()

        # If list is blank, return blank list
        if self.__first is None:
            return new_list

        # Put current node in check list
        current_node = self.__first
        content_values = [current_node.value]

        # Create a new node in the new list containing the first value of the old list
        new_list.__first = new_list.Node(current_node.value)
        new_list.__last = new_list.__first
        new_current_node = new_list.__first

        # Iter the old list
        while current_node is not None and current_node.next_node is not None:
            if current_node.next_node.value not in content_values:
                new_current_node.next_node = new_list.Node(current_node.next_node.value)
                new_list.__last = new_current_node.next_node
                new_current_node = new_current_node.next_node
                content_values.append(current_node.next_node.value)
            
            current_node = current_node.next_node
        return new_list

if __name__ == "__main__":
    test = [1, 1, 3, 4, 6, 7, 7, 8, 9, 10, 10, 11, 12, 14, 14]
    linked_list = LinkedList()
    for x in test[::-1]:
        linked_list.insert(x)
    
    print(linked_list)
    new_linked_list = linked_list.different_values()
    print(new_linked_list)
    print("¿Son listas diferentes?: "+str(not (new_linked_list is linked_list)))