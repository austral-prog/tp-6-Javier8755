def remove_elements(list_to_remove_elements):
    lista = list_to_remove_elements

    if len(lista) < 2:
        return []
    elif len(lista) >= 2 and len(lista) < 5:
        return lista[1:]
    elif len(lista) == 5 or len(lista) == 6:
        return lista[1:4]
    else:
        return lista[1:4] + lista[5:]



def add_elements(list_to_add_elements):
    
    lista = list_to_add_elements

    lista.insert(0,"Pink") 

    lista.append("Yellow")

    return lista


def is_empty(list_to_check):
    lista = list_to_check

    if len(lista) == 0:
        return "Lista Vacía"


def check_lists(list_to_compare1, list_to_compare2):
    
    lista1 = list_to_compare1
    lista2 = list_to_compare2

    if len(lista1) < 3 or len(lista2) < 3:
        return False 
    elif lista1[2] == lista2[2]:
        return True
    else:
        return False

def list_of_lists(list_of_lists_to_modify):
    lista = list_of_lists_to_modify
    modified_list = [lista[0][0:2], lista[1][1:4], lista[2][-2:]]
    return modified_list 

