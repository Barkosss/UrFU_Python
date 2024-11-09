number_rooms = 101

color_doors = color = used_color = []
for index in range(number_rooms):
    color_doors.append([0] * number_rooms)
    color.append([0] * number_rooms)
    used_color.append([0] * 3)
matrix_size = 0

def fill_array(arr, size=number_rooms, value=0):
    for row in range(1, size):
        for column in range(1, size):
            arr[row][column] = value

def choose_color(row):
    if used_color[row][1] >= used_color[row][2]:
        return 2
    return 1

def color_graph(row, column, num_color):
    while color[row][column] == 0:
        color[row][column] = num_color
        used_color[row][num_color] += 1
        color_door = color_doors[row][column]
        save_index_color = 0
        for index_color in range(1, color_doors[color_door][0] + 1):
            if color_doors[color_door][index_color] == row:
                save_index_color = index_color
                break

        color[color_door][save_index_color] = 3 - num_color
        used_color[color_door][3 - num_color] += 1
        for index_color in range(1, color_doors[color_door][0] + 1):
            if color[color_door][index_color] == 0:
                save_index_color = index_color
                break
        row = color_door
        column = save_index_color

def solver():
    fill_array(color)
    fill_array(used_color, size=3)

    for row in range(1, matrix_size + 1):
        for column in range(1, color_doors[row][0]+1):
            if not color[row][column]:
                color_graph(row, column, choose_color(row))

def read():
    global matrix_size
    with open('input.txt', 'r') as file:
        matrix_size = int(file.readline())
        for row in range(0, int(matrix_size)):
            arr_text = file.readline().split()
            new_row=list()
            for index_room in range(len(arr_text)):
                new_row.append(int(arr_text[index_room]))
            color_doors[row + 1][0] = new_row[0]

            for column in range(1, len(new_row) - 1):
                color_doors[row + 1][column] = new_row[column]

def out():
    answer = ''
    for row in range(1, matrix_size + 1):
        for column in range(1, color_doors[i][0] + 1):
            if color[row][column] == 1:
                answer += "Y "
            elif color[row][column] == 2:
                answer += "G "
        answer += '\n'
    print(answer)

def main():
    read()
    solver()
    out()

if __name__ == "__main__":
    main()