from template import LinkedList 
from solution import LinkedList as sol

if __name__ == "__main__":
    test = [1, 1, 3, 4, 6, 7, 7, 8, 9, 10, 10, 11, 12, 14, 14]
    linked_list = LinkedList()
    for x in test[::-1]:
        linked_list.insert(x)
    
    print(linked_list)
    new_linked_list = linked_list.different_values()
    print(new_linked_list)
    answer = new_linked_list
    print("¿Son listas diferentes?: "+str(not (new_linked_list is linked_list)))
    print("======================================| SOLUCIÓN |==========================================")
    linked_list_sol = sol()
    for x in test[::-1]:
        linked_list_sol.insert(x)
    
    print(linked_list_sol)
    new_linked_list_sol = linked_list_sol.different_values()
    print(new_linked_list_sol)
    print("¿Son listas diferentes?: "+str(not (new_linked_list_sol is linked_list_sol)))
    print("¿La respuesta es correcta?: "+("Si" if new_linked_list_sol == answer else "No"))
