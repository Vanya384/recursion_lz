def Pascal_triangle(level):
    arr_2=[1]
    if len(arr)<2:
        arr.append(1)
    else:    
        for i in range(len(arr)-1):
            arr_2.append(arr[i]+arr[i+1])
        arr_2.append(1)
        arr=arr_2
        arr_2=[1]
        print(arr)
        Pascal_triangle(level-len(arr),arr)


def main():
    Pascal_triangle(3)

main()
