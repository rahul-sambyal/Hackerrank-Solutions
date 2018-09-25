if __name__ == '__main__':
    physics = []
    sorted_list = []
    final_list = []
    lowest = []
    marks = []
    result = []
    n = 0
    for _ in range(int(input())):
        students = []
        name = input()
        score = float(input())
        students.append(name)
        students.append(score)
        physics.append(students)
        second = 0

    sorted_list = (sorted(physics, key= lambda x: float(x[1])))
    for i in range(0, len(sorted_list)):
        if sorted_list[i][1] == sorted_list[0][1]:
            continue
        second = sorted_list[i][1]
        break
    for i in range(0, len(sorted_list)):
        if sorted_list[i][1] == second:
                final_list.append(sorted_list[i])

    for i in range(len(final_list)):
        result.append(final_list[i][0])
    result.sort()
    for i in range(len(result)):
        print(result[i])
