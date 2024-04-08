class StringsPrinter:
    def __init__(self, string_list:list) -> None:
        self.__list = string_list

    def __iter__(self):
        for element in self.__list:
            if type(element) == str and isrealstring(element):
                yield element.capitalize()
    

def isrealstring(element):
    try:
        if int(element):
            return False
    except Exception:
        pass

    try:
        if float(element):
            return False
    except Exception:
        pass

    try:
        if element == "None":
            return False
    except Exception:
        pass

    try:
        if element == "":
            return False
    except Exception:
        pass
    return True
