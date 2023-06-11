"""Шифрувальня система Атбаш"""
_atbas = {
        'а': 'я', 'б': 'ю', 'в': 'э', 'г': 'ь', 'д': 'ы', 'е': 'ъ', 'ё': 'щ', 'ж': 'ш', 'з': 'ч', 'и': 'ц', 'й': 'х',
        'к': 'ф', 'л': 'у', 'м': 'т', 'н': 'с', 'о': 'р', 'п': 'п', 'р': 'о', 'с': 'н', 'т': 'м', 'у': 'л', 'ф': 'к',
        'х': 'й', 'ц': 'и', 'ч': 'з', 'ш': 'ж', 'щ': 'ё', 'ъ': 'е', 'ы': 'д', 'ь': 'г', 'э': 'в', 'ю': 'б', 'я': 'а'
     }


alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
     'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', ',', '.']
_cezar = {alphabet[i]: i for i in range(len(alphabet))}
_cezar_revers = {i: alphabet[i] for i in range(len(alphabet))}


matrix_alphabet = [
    ['а', 'б', 'в', 'г', 'д', 'е'],
    ['ё', 'ж', 'з', 'и', 'й', 'к'],
    ['л', 'м', 'н', 'о', 'п', 'р'],
    ['с', 'т', 'у', 'ф', 'х', 'ц'],
    ['ч', 'ш', 'щ', 'ъ', 'ы', 'ь'],
    ['э', 'ю', 'я', '.', ',', ' ']
]


def check_char(char):
    flag = 0
    for i in range(6):
        if char not in matrix_alphabet[i]:
            flag += 1

    if flag == 6:
        return True
    else:
        return False


class Adbash:
    @staticmethod
    def cod(text: str):
        resolt = []
        for i in range(len(text)):
            if text[i] in _atbas:
                resolt.append(_atbas[text[i]])
            else:
                resolt.append(text[i])
        return ''.join(resolt)


class Cezar:

    def __init__(self, rod=3):
        self.ROD = rod

    def cod(self, text):
        answer = []

        for i in text:
            try:
                answer.append(_cezar_revers[(_cezar[i] + self.ROD) % 32])
            except:
                answer.append(i)
        return ''.join(answer)

    def decod(self, text):
        answer = []

        for i in text:
            try:
                answer.append(_cezar_revers[(33 + _cezar[i] - self.ROD) % 33])
            except:
                answer.append(i)
        return ''.join(answer)


class Polibia:
    matrix = [[0 for j in range(6)] for i in range(6)]

    def cod(self, text):
        answer = []
        result = []

        for char in text:
            if check_char(char):
                answer.append(char)
                continue
            for i in range(6):
                for j in range(6):
                    if matrix_alphabet[i][j] == char.lower():
                        answer.append(str(i + 1) + str(j + 1))
                        break
        """костиль"""
        for num in answer:
            if num.isdigit():
                i, j = int(num[0]), int(num[1])
                print(i, j)
                if j - 4 <= 1:
                    i = (abs(i - 1) + 6) % 7
                    j = 6 - abs(j - 4)
                elif j - 4 >= 1:
                    j -= 4
                print(i, j)
                result.append(matrix_alphabet[i - 1][j - 1])
            else:
                result.append(num)
        return ' '.join(result)

    @staticmethod
    def decod(request):

        """костыль"""
        result = []
        for char in request:
            if check_char(char):
                result.append(char)
                continue
            for i in range(6):
                for j in range(6):
                    if matrix_alphabet[i][j] == char.lower():
                        result.append(str(i + 1) + str(j + 1))
                        break
        answer = []
        for num in result:
            if num.isdigit():
                i, j = int(num[0]), int(num[1])
                print(i, j)
                if j + 5 > 6:
                    i = (abs(i + 1)) % 7
                    j = abs(j + 5) % 7
                elif j + 4 <= 6:
                    j += 4
                print(i, j)
                answer.append(matrix_alphabet[i - 1][j - 1])
            else:
                answer.append(num)

        return ''.join(answer)



class Trisemus:
    def index_find(self, word, alph=matrix_alphabet):
        answer = []
        for char in word:
            if check_char(char):
                answer.append(char)
                continue
            for i in range(6):
                for j in range(6):
                    if char == alph[i][j]:
                        answer.append(str(i) + str(j))

        return answer

    @staticmethod  # переделывает алфавит под ключевое слово
    def __deconstruct(word):
        matrix = [[0 for _ in range(6)] for _ in range(6)]
        word += "".join(alphabet)
        rework_alphabet = []


        for i in word:
            if i.lower() in rework_alphabet:
                continue
            else:
                rework_alphabet.append(i.lower())


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = rework_alphabet[i * len(matrix[0]) + j]
        return matrix

    def cod(self, key, sentence):
        rework_alphabed = self.__deconstruct(key)
        index_mass = self.index_find(sentence.lower(), alph=rework_alphabed) # хранит индексы предложения
        try:
            result = [rework_alphabed[(int(i[0]) + 1) % 6][int(i[1])] for i in index_mass]
        except ValueError:
            return 'извините я вас не понимаю'
        return "".join(result)



    def decod(self, key, sentence):
        rework_alphabet = self.__deconstruct(key)
        index_mass = self.index_find(sentence, alph=rework_alphabet)
        try:
            result = [matrix_alphabet[(int(i[0]) + 5) % 6][int(i[1])] for i in index_mass]
        except ValueError:
            return "извините я вас не понимать, начальника"
        return ''.join(result)



if __name__ == "__main__":
    a = Trisemus()
    a.decod("ПРЕФЕКТУРА", "уаауштшцичднщчктшуамиьуф")

