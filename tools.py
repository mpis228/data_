"""Шифрувальня система Атбаш"""
_atbas = {
        'а': 'я', 'б': 'ю', 'в': 'э', 'г': 'ь', 'д': 'ы', 'е': 'ъ', 'ё': 'щ', 'ж': 'ш', 'з': 'ч', 'и': 'ц', 'й': 'х',
        'к': 'ф', 'л': 'у', 'м': 'т', 'н': 'с', 'о': 'р', 'п': 'п', 'р': 'о', 'с': 'н', 'т': 'м', 'у': 'л', 'ф': 'к',
        'х': 'й', 'ц': 'и', 'ч': 'з', 'ш': 'ж', 'щ': 'ё', 'ъ': 'е', 'ы': 'д', 'ь': 'г', 'э': 'в', 'ю': 'б', 'я': 'а'
     }


z = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
     'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
_cezar = {z[i]: i for i in range(len(z))}
_cezar_revers = {i: z[i] for i in range(len(z))}


polib = [
    ['а', 'б', 'в', 'г', 'д', 'е'],
    ['ё', 'ж', 'з', 'и', 'й', 'к'],
    ['л', 'м', 'н', 'о', 'п', 'р'],
    ['с', 'т', 'у', 'ф', 'х', 'ц'],
    ['ч', 'ш', 'щ', 'ъ', 'ы', 'ь'],
    ['э', 'ю', 'я', '-', '-', ' ']
]


class Adbash:
    @staticmethod
    def cod(request: str):
        resolt = []
        for i in range(len(request)):
            if request[i] in _atbas:
                resolt.append(_atbas[request[i]])
            else:
                resolt.append(request[i])
        return ''.join(resolt)

    @staticmethod
    def decod(request: str):
        resolt = []
        for i in request:
            if i in _atbas.values():
                for key, value in _atbas.items():
                    if value == i:
                        resolt += key
            else:
                resolt += i
        return ''.join(resolt)


"""остался один основ баг который я не трогал это то что когда символы которых нет в списке вести то выбьет ошибку
    так что нужно будет это исправить но это потом и не так уже и сложно """


class Cezar:

    def __init__(self, rod=3):
        self.ROD = rod

    def cod(self):
        text = input()
        answer = []

        for i in text:
            answer.append(_cezar_revers[(_cezar[i] + self.ROD) % 32])
        return ''.join(answer)

    def decod(self):
        text = input()
        answer = []

        for i in text:
            answer.append(_cezar_revers[(33 + _cezar[i] - self.ROD) % 33])
        return ''.join(answer)


class Polibia:
    matrix = [[0 for j in range(6)] for i in range(6)]

    @staticmethod
    def check_char(char):
        flag = 0
        for i in range(6):
            if char not in polib[i]:
                flag += 1

        if flag == 6:
            print(f'{char} - {flag}')
            return True
        else:
            return False

    def cod(self):
        text = input()
        answer = []

        for char in text:
            if self.check_char(char):
                answer.append(char)
                continue
            for i in range(6):
                for j in range(6):
                    if polib[i][j] == char.lower():
                        answer.append(str(i + 1) + str(j + 1))
                        break
        return ''.join(answer)

    @staticmethod
    def decod():
        text = input().split()
        answer = []
        for arg in text:
            answer.append(polib[int(arg[0]) - 1][int(arg[1]) - 1])

        return ''.join(answer)

    
if __name__ == "__main__":
    a = Polibia()
    print(a.decod())
