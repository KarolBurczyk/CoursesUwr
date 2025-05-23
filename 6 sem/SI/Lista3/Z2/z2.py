from queue import Queue
import collections
import random
from enum import Enum

MAX_UNCERTAINTY = 2
MAX_NUM_ACTIONS = 150

# klasa enumerowalna Movement do poruszania się
class Movement(Enum):
    U = 0, -1
    D = 0, 1
    L = -1, 0
    R = 1, 0
    
    # metoda dodająca wybrany ruch do pozycji
    def add_to(self, position):
        x, y = position
        dx, dy = self.value
        return x + dx, y + dy

class Commando:
    # konstruktor klasy Commando
    def __init__(self, initial_state, walls, destinations):
        self.initial_state = initial_state
        self.walls = walls
        self.destinations = destinations
    
    # generuje nowe stany gry po wykonaniu możliwych ruchów
    def gen_new_states(self, state):
        new_states = []
        for movement in Movement:
            new_state = tuple(sorted(self.move(movement, state)))
            new_states.append((new_state, movement.name))
        return new_states

    # sprawda czy gra została wygrana
    def is_a_win(self, state):
        for pos in state:
            if pos not in self.destinations:
                return False
        return True
    
    # funkcja redukująca niepewność przez wykonanie losowych ruchów
    def reduce_uncertainty(self):
        state = set(self.initial_state)
        movements = []

        movement = collections.namedtuple('temp', 'value')((0, 0))
        while len(state) > MAX_UNCERTAINTY:
            movement = random.choice([m for m in Movement if m.add_to(movement.value) != (0, 0)])
            state = self.move(movement, state)
            movements.append(movement.name)

        return tuple(sorted(state)), ''.join(movements)
    
    # wykonuje ruch dla każdego z elementów stanu gry
    def move(self, movement, state):
        new_state = set()
        for pos in state:
            new_pos = movement.add_to(pos)
            new_state.add(new_pos if new_pos not in self.walls else pos)
        return new_state

# odczyt danych i utworzenie obiektu Commando
def read_data():
    with open('zad_input.txt') as inp:
        board = inp.readlines()
        
    objects = collections.defaultdict(set)
    for y, row in enumerate(board):
        for x, tile in enumerate(row):
            objects[tile].add((x, y))
    
    state = objects['S'] | objects['B']
    return Commando(
        tuple(sorted(state)),
        objects['#'],
        objects['G'] | objects['B'],
    )

if __name__ == '__main__':
    game = read_data()
    
    found_solution = False
    
    while not found_solution:
        try:
            root, random_movements = game.reduce_uncertainty()

            to_visit = Queue()
            visited = {root}

            to_visit.put((root, ''))

            while not to_visit.empty():
                sub_root, solution = to_visit.get()
                if game.is_a_win(sub_root):
                    found_solution = True
                    break
                if len(solution) > MAX_NUM_ACTIONS - len(random_movements):
                    raise Exception

                for child, action in game.gen_new_states(sub_root):
                    if child in visited:
                        continue
                    to_visit.put((child, solution + action))
                    visited.add(child)
                    
        except Exception:
            continue
        else:
            break
    
    solution_str = random_movements + solution
    print(random_movements, solution, len(solution_str))

    with open('zad_output.txt', 'w+') as out:
        out.write(solution_str)
