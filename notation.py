def convert_to_base(number,base):
    if base < 2 or base > 16:
        print("Ошибка,система счисления не удовлетворяет заданному диапозону")
        return -1
    if number<0:
        print("Ошибка,число должно быть неотрицательным")
        return -1
    symbols="0123456789ABCDEF"
    if number<base:
        return symbols[number]   #если число меньше системы счисления,то оно будет под своим номером в массиве символов системы счисления
    
    
    return convert_to_base(number//base,base) + symbols[number%base]  #целая часть от деления исходного числа на систему счисления переходит далее в рекурсию,
                                                                      #в то время как остаток от деления идет в массив symbols,находит себя там и  запоминается


def main():
    number=int(input("Введите число"))
    base=int(input("Введите систему счисления"))
    print(convert_to_base(number,base))

main()
