class StringsPrinter:
    def __init__(self, string_list:list) -> None:
        self.__list = string_list

    def __iter__(self):
        for x in self.__list:
            if type(x) != str:
                continue
            if FilterStr(x):
                if x.strip() == "":
                    continue
                yield x.capitalize()

def FilterStr(string:str):
    for x in [int, None, float]:
        if SecureCheckType(string, x):
            return False
    return True
    
def SecureCheckType(value:any, type:type):
    try:
        if type(value):
            return True
    except Exception:
        return False
    return False
