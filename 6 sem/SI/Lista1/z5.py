# Niestety tego zadania nie udało mi się dosiągnąć do końca. Zmiana piksela jest realizowana w następujący sposób:
# wybieram losowy wiersz, który nie jest poprawnie uzupełniony, następnie biorę wszystkie kolumny, które nie są poprawnie uzupełnione i
# wybieram losową i-tą z nich. Jeżeli jest w niej za mało znaków '#' to zmieniam i-tą komórkę w wierszu na '#'(jeżeli jeszcze nie jest '#', w przeciwnym wypadku losuję następną).
# Analogicznie sprawa wygląda dla kolumn. Nie wpadł mi do głowy pomysł jak to zrobić lepiej lub efektywniej.

import random

def save_img(img, name):
    with open(name, 'w') as file:
        for row in img:
            file.write("".join(row) + '\n')

def generate_img(x, y):
    return [['.' for _ in range(y)] for _ in range(x)]

# funkcja zwraca listę niepoprawnych jeszcze wierszy oraz kolumn 
def incompleted_lines(image, rows, cols):
    incomplete_rows, incomplete_cols = [], []
    for i, row in enumerate(image):
        if not check_line(row, rows[i]):
            incomplete_rows.append(i)
    for j in range(len(cols)):
        col = [image[i][j] for i in range(len(image))]
        if not check_line(col, cols[j]):
            incomplete_cols.append(j)
    return incomplete_rows, incomplete_cols

# funkcja zwraca 
def count_hash_blocks(s):
    blocks = []
    count = 0
    
    for char in s:
        if char == '#':
            count += 1
        elif count > 0:
            blocks.append(count)
            count = 0
    
    if count > 0:
        blocks.append(count)
    
    return blocks

def evaluate_line(line, req):
    line_blocks = count_hash_blocks(line)

    if line_blocks == req:
        return 100

    if not req:
        return 100 - (sum(line) * 10)

    if not line_blocks:
        return -req[0] * 5

    expected_size = req[0] if req else 0

    if len(line_blocks) > 1:
        return -20 * len(line_blocks)

    actual_size = line_blocks[0]
    size_diff = abs(actual_size - expected_size)

    if size_diff == 0:
        return 80
    else:
        return 50 - (size_diff * 10)

def evaluate(image, cols, rows):
    sum = 0
    for i in range(len(image)):
        sum += evaluate_line(image[i], rows[i])
    for j in range(len(image[0])):
        sum += evaluate_line([row[j] for row in image], cols[j])
    return sum

# check_line zwraca informację czy linia jest już poprawnie uzupełniona
 
def check_line(line, requirements):
    return count_hash_blocks(line) == requirements
    
def change_pixel(image, i, j): # funkcja zmienia piksel na przeciwny 
    if image[i][j] == '#':
        image[i][j] = '.'
        return image
    else:
        image[i][j] = '#'
        return image 

def change_pixel_row(image, i, cols, rows):
    maks, maks_id = 0, random.randint(0, len(cols)-1)
    for j in range(len(cols)):
        tmp = evaluate(change_pixel(image, i, j), cols, rows) # sprawdzamy po kolei każdy piksel w wierszu 
        if tmp > maks:
            maks, maks_id = tmp, j
    
    return change_pixel(image, i, maks_id) # wybieramy ten, którego zmiana da największy wynik

def change_pixel_col(image, j, cols, rows):
    maks, maks_id = 0, random.randint(0, len(rows)-1)
    for i in range(len(rows)):
        tmp = evaluate(change_pixel(image, i, j), cols, rows) # sprawdzamy po kolei każdy piksel w kolumnie 
        if tmp > maks:
            maks, maks_id = tmp, i
    
    return change_pixel(image, maks_id, j) # wybieramy ten, którego zmiana da największy wynik

def solve(image_width, image_height, rows, cols):
    image = generate_img(image_width, image_height)
    
    max_iter = 10000
    iterations = 0
    while iterations < max_iter:
        iterations += 1
        ic_rows, ic_cols = incompleted_lines(image, rows, cols)
        if not ic_cols and not ic_rows:
            break
        elif not ic_cols:
            choose_row_column = 'row'
        elif not ic_rows:
            choose_row_column = 'column'
        else:
            choose_row_column = random.choice(['row', 'column']) # dowolnie kolumna lub wiersz
            
        if choose_row_column == 'row':
            i = random.choice(ic_rows) # wybieramy dowolny wiersz z niepoprawnych jeszcze
            image = change_pixel_row(image, i, cols, rows)
        else:
            j = random.choice(ic_cols) # analogicznie robimy z kolumnami 
            image = change_pixel_col(image, j, cols, rows)
    
    save_img(image, 'zad5_output.txt')

def main():
    with open('zad5_input.txt', 'r') as file:
        size_x, size_y = map(int, file.readline().split())
        rows = [list(map(int, file.readline().split())) for _ in range(size_x)] # w rows są wytyczny dla kolejnych wierszy
        cols = [list(map(int, file.readline().split())) for _ in range(size_y)] # w cols sąwytyczne dla kolejnych kolumn

    solve(size_x, size_y, rows, cols)

if __name__ == "__main__":
    main()
