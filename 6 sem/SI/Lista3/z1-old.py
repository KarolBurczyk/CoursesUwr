from itertools import combinations

def save_img(img, name):
    with open(name, 'w') as file:
        for row in img:
            file.write("".join(row) + '\n')

def generate_img(x_size, y_size):
    return [['.' for _ in range(x_size)] for _ in range(y_size)]

def fill_full_row(image, y, pattern, size):
    if pattern == size:
        tmp = 0
    else:
        tmp = size - pattern
    for x in range(tmp, size - tmp):
        image[y][x] = '1'
    return image

def fill_full_col(image, x, pattern, size):
    if pattern == size:
        tmp = 0
    else:
        tmp = size - pattern
    for y in range(tmp, size - tmp):
        image[y][x] = '1'
    return image

def fill_row(image, y, pattern, size):
    for x in range(size):
        image[y][x] = '1'
    idx = 0
    for dst in pattern:
        idx += dst
        image[y][idx] = '0'
        idx += 1
    return image

def fill_col(image, x, pattern, size):
    for y in range(size):
        image[y][x] = '1'
    idx = 0
    for dst in pattern:
        idx += dst 
        image[idx][x] = '0'
        idx += 1
    return image

def generate_valid_arrangements(length, segments):
    segment_lengths = len(segments)
    
    valid_grids = []
    
    for spaces in combinations(range(1, length), segment_lengths - 1):
        positions = [0] + list(spaces) + [length]
        
        if any(positions[i + 1] - positions[i] <= segments[i] for i in range(segment_lengths)):
            continue
        
        row = ['.'] * length
        index = 0
        for i in range(segment_lengths):
            start = positions[i]
            for j in range(segments[i]):
                row[start + j] = '1'
            if i < segment_lengths - 1:
                row[positions[i + 1] - 1] = '.'
        valid_grids.append("".join(row))
    
    return valid_grids

def find_common_filled_cells(length, segments):
    arrangements = generate_valid_arrangements(length, segments)
    if not arrangements:
        return []
    common_cells = [i for i in range(length) if all(arr[i] == '1' for arr in arrangements)]
    return common_cells

def prog_row(image, y, pattern, size):
    cells = find_common_filled_cells(size, pattern)
    for x in cells:
        image[y][x] = '1'
    return image

def prog_col(image, x, pattern, size):
    cells = find_common_filled_cells(size, pattern)
    for y in cells:
        image[y][x] = '1'
    return image

def solve(x_size, y_size, rows, cols):
    image = generate_img(x_size, y_size)
    for y in range(y_size):
        image = prog_row(image, y, rows[y], x_size)
        # if len(rows[y]) == 1:
        #     if rows[y][0] > x_size / 2:
        #         image = fill_full_row(image, y, rows[y][0], x_size)
        #     if rows[y][0] == 0:
        #         for x in range(x_size):
        #             image[y][x] = 0
        # else:
        #     if sum(rows[y]) + len(rows[y]) - 1:
        #         image = fill_row(image, y, rows[y], x_size)

    for x in range(x_size):
        image = prog_col(image, x, cols[x], y_size)
        # if len(cols[x]) == 1: 
        #     if cols[x][0] > y_size / 2:
        #         image = fill_full_col(image, x, cols[x][0], y_size)
        #     if cols[x][0] == 0:
        #         for y in range(y_size):
        #             image[y][x] = 0
        # else:
        #     if sum(cols[x]) + len(cols[x]) - 1:
        #         image = fill_col(image, x, cols[x], y_size)


    save_img(image, 'zad1_output.txt')

def main():
    with open('zad1_input.txt', 'r') as file:
        x_size, y_size = map(int, file.readline().split())
        rows = [list(map(int, file.readline().split())) for _ in range(x_size)] # w rows są wytyczny dla kolejnych wierszy
        cols = [list(map(int, file.readline().split())) for _ in range(y_size)] # w cols sąwytyczne dla kolejnych kolumn
    solve(x_size, y_size, rows, cols)

if __name__ == "__main__":
    main()
