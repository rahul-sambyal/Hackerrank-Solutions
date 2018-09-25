s = input()
out = []
j, c = input().split()
for i in range(len(s)):
    if i == int(j):
        out.append(c)
    else:
        out.append(s[i])
for i in range(len(out)):
    print(out[i],end="")
