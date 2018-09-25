if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    total = 0.00
    avg = 0.00
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    var = student_marks[query_name]
    for i in range(len(var)):
        total += var[i] + 0.00
    avg = float(total / len(var))
    print("%.2f" % avg)
    
