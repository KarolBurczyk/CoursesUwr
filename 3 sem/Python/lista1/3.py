def tabliczka(x1, x2, y1, y2, d):
    i = 0
    width = (int)((x2 - x1) / d + 2)
    height = (int)((y2 - y1) / d + 2)
    tab = [[0] * width for i in range(height)]
    spaces = [0 for i in range(width)]
    for x in range(height):
        for y in range(width):
            if x == 0:
                if y == 0:
                    pass
                else:
                    tab[x][y] = x1 + (y - 1) * d
            elif y == 0:
                tab[x][y] = y1 + (x - 1) * d
                if len(str(tab[x][y])) > spaces[y]:
                    spaces[y] = len(str(tab[x][y]))
            else:  
                tab[x][y] = tab[0][y] * tab[x][0]
                if len(str(tab[x][y])) > spaces[y]:
                    spaces[y] = len(str(tab[x][y]))

    for x in range(height):
        for y in range(width):
            if x == 0:
                if y == 0:
                    print(spaces[y] * " ", end=" ")
                else:
                    print((spaces[y] - len(str(tab[x][y]))) * " ", tab[x][y], end="")
            elif y == 0:
                print((spaces[y] - len(str(tab[x][y]))) * " ", tab[x][y], end="")
            else:  
                print((spaces[y] - len(str(tab[x][y]))) * " ", tab[x][y], end="")
        print("\n")
    
    

                
        
        




tabliczka(-1000.0, 1000.0, -1000.0, 1000.0, 100.0)