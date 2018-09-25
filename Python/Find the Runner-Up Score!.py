if __name__ == '__main__':
    n = int(input())
    arr = (input().split(" "))
    arrint = []
    for i in range(n):
        arrint.append(int(arr[i]))
    max = max2 = -1000000
    for i in range(n):
        if max < arrint[i]:
            max = arrint[i]
    for j in range(n):
        if arrint[j] == max:
            continue
        elif max2 < arrint[j]:
            max2 = arrint[j]
print(max2)
