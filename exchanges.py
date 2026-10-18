def find_partitions(number, max_value):#переменную max_value используем для того,чтобы не было повторных сумм
                                           #(условно:3=2+1=1+2,т.е. задается отношение порядка)
    if max_value==0:
        max_value = number
    if number == 0:
        return [[]]  #используем [[]],а не [] ,потому что в питоне между ними есть разница:
                        #в первом случае внутри находится пустой блок,когда в случае 2 абсолютно ничего
    section=[]   #место,куда будут записываться все полученные на данный момент разбиения на суммы
    minimum=min(number,max_value)
    for i in range(minimum,0,-1): #min-показывает откуда идет начало;
                                  #0-показывает где заканчиваем;
                                      #-1 -знак "-" показывает,что мы идем назад(в сторону 0)
        for subsection in find_partitions(number - i, i):
            section.append([i] + subsection)   
    return section                    


def main():
    print(find_partitions(5,0))


main()
