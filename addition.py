def rec_addition(string_1,string_2,transferal):   #transferal является переносом
                                                   #(условно:мы сложиил 8+9,цифра 7 из полученного 17 остается ,а 1 явлется transferal)
    if string_1 == "" and string_2 == "" and transferal == 0:    #уже нечего считать
        return ""
    if string_1 != "":
        digit_1 = string_1[-1]     #если строка не пустая, то сдвигаем на один элемент влево
    else:
        digit_1 = 0
    if string_2 != "":
       digit_2 = string_2[-1]     #аналогично
    else:
        digit_2 = 0
    absolute = int(digit_1) + int(digit_2) + transferal    #сумма цифр и переноса дадут цифру
    actual_digit = absolute % 10   #число ,которое останется под суммой этих чисел(по разряду)
    next_transferal=absolute//10   #число ,которое пойдет в сумму следующих по разрядам цифр
    next_string_1=""   #заранее создали две пустые следующие строки,дабы в случае ,если длина нынешней не больше 0,
    next_string_2=""   #программа не выдала ошибку(потому что тогда строки следующей вообще не будет существовать)
    if len(string_1)>0:   
        next_string_1=string_1[:-1]     #создаем новую строку сдвинутую влево на 1 символ,которую впоследствие закинем в рекурсию
    if len(string_2)>0:
        next_string_2=string_2[:-1]   #аналогично
    return rec_addition(next_string_1,next_string_2,next_transferal)+ str(actual_digit)   #нужно добавить str(actual_digit),потому что без нее на последнем шаге вернется пустая строка и все сломается

def main():
    string1="1435"
    string2="13536"
    print(rec_addition(string1,string2,0))


main()



