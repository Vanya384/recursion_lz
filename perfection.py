def perfection(number):
    if number<2:
        print("Ошибка,число неудовлетворяет нужному диапозону значений")
    arr=[]
    for i in range(1,number):
        if(number%i==0):
            arr.append(i)
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    if number==sum:
        print(f"{number} - совершенное число")
        return 1
    else:
        print(f"{number} - несовершенное число")
        return 0


def main():
    number=int(input("Введите число"))
    perfection(number)


main()
    