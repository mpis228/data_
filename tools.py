
"""Шифрувальня система Атбаш"""
__atbas = {
    'а': 'я', 'б': 'ю', 'в': 'э', 'г': 'ь', 'д': 'ы', 'е': 'ъ', 'ё': 'щ', 'ж': 'ш', 'з': 'ч', 'и': 'ц', 'й': 'х',
    'к': 'ф', 'л': 'у', 'м': 'т', 'н': 'с', 'о': 'р', 'п': 'п', 'р': 'о', 'с': 'н', 'т': 'м', 'у': 'л', 'ф': 'к',
    'х': 'й', 'ц': 'и', 'ч': 'з', 'ш': 'ж', 'щ': 'ё', 'ъ': 'е', 'ы': 'д', 'ь': 'г', 'э': 'в', 'ю': 'б', 'я': 'а'
}

# cipher = [i for i in range(1072, 1104)]
# resolt = []

def atbash(request: str):
    resolt = []
    for i in range(len(request)):
        if request[i] in __atbas:
            resolt.append(__atbas[request[i]])
        else:
            resolt.append(request[i])
    return resolt

def atbash_return(request: str):
    resolt = []
    for i in request:
        if request is __atbas.values():
            for key, value in __atbas.items():
                if value == i:
                    resolt += key
        else:
            resolt += i
    return resolt

def test():
    if input("зашифруваты - 1 росшифрувати - 0 \n") == '1':
       print(atbash(input()))
    else:
        print(atbash_return(input()))


if __name__ == "__main__":
    test()

