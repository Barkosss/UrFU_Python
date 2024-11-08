MaxN = 101

k = color = usedColor = []
for i in range(101):
    k.append([0] * 101)

for i in range(101):
    color.append([0] * 101)

for i in range(101):
    usedColor.append([0] * 3)
n = 0

def fill_array(arr, size=MaxN, value=0):
    for i in range(1, size):
        for j in range(1, size):
            arr[i][j]=value

def fill_array1(arr, size=3, value=0):
    for i in range(1, size):
        for j in range(1, size):
            arr[i][j]=value

def choose_color(i):
    if usedColor[i][1] >= usedColor[i][2]:
        return 2
    else:
        return 1

def color_graph(i, j, t):
    while color[i][j] == 0:
        color[i][j] = t
        usedColor[i][t]+=1
        u = k[i][j]
        for v in range(1, k[u][0] + 1):
            if k[u][v] == i:
                break

        color[u][v] = 3-t
        usedColor[u][3 - t] += 1
        for v in range(1, k[u][0] + 1):
            if color[u][v] == 0:
                break
        i = u
        j = v


def solv():
    fill_array(color)
    fill_array1(usedColor)

    for i in range(1, n + 1):
        for j in range(1, k[i][0]+1):
            if color[i][j] == 0:
                t = choose_color(i)
                color_graph(i, j, t)

def in_():
    global n
    f = open('input.txt', 'r')
    n = int(f.readline())
    for i in range(0, int(n)):
        r = f.readline().split()
        row=list()
        for j in range(len(r)):
            row.append(int(r[j]))
        k[i+1][0] = row[0]

        for j in range(len(row)):
            if j == 0:
                continue
            k[i+1][j] = row[j]

def out():
    ans = ''
    for i in range(1, n + 1):
        for j in range(1, k[i][0] + 1):
            if(color[i][j]==1):
                ans += "Y "
            elif(color[i][j] == 2):
                ans += "G "
        ans += '\n'
    print(ans)

def main():
    in_()
    solv()
    out()


if __name__ == "__main__":
    main()