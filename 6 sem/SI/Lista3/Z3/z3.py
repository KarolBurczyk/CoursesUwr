from collections import deque
import heapq

maze = []
goals = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = set()
commandos = []
distance = {}
N, M = 0, 0

def print_maze():
    for m in maze:
        print(*m)

def vec_to_pos(n):
    return ['R', 'L', 'D', 'U'][n]

def good_move(positions):
    h_s = tuple(positions)
    if h_s in visited:
        return False

    visited.add(h_s)
    return True

def make_new_pos(i, positions):
    ans = []

    for p in positions:
        new_x = p[0] + dx[i]
        new_y = p[1] + dy[i]

        if maze[new_x][new_y] != '#':
            ans.append((new_x, new_y))
        else:
            ans.append(p)

    return list(set(ans))

def mission_complete(state):
    for s in state:
        if not s in goals:
            return False
    return True

def heuristic(positions, moves):
    distances = [distance[pos] for pos in positions]
    return max(distances) + moves

def print_answer(answer):
    f = open('zad_output.txt', 'w')
    f.write(answer)
    f.close()

def BFS(pos):
    distance[pos] = 1e9
    QQ = deque()
    visited = {}
    visited[pos] = True
    QQ.append((pos, 0))

    while QQ:
        act = QQ.popleft()
        dist = act[1]
        act = act[0]

        if act in goals:
            distance[pos] = min(distance[pos], dist)

        for i in range(4):
            new_x = act[0] + dx[i]
            new_y = act[1] + dy[i]

            if not (new_x, new_y) in visited and maze[new_x][new_y] != '#':
                visited[(new_x, new_y)] = True
                QQ.append(((new_x, new_y), dist + 1))

def all_shortest_paths():
    for i in range(N):
        for j in range(M):
            pos = (i, j)
            if maze[i][j] != '#':
                BFS(pos)

def read_file():
    with open('zad_input.txt') as f:
        for line in f:
            maze.append(list(line.strip()))

    return len(maze), len(maze[0])

if __name__ == '__main__':
    N, M = read_file()
    # print('Start:')
    # print_maze()

    for i in range(N):
        for j in range(M):
            if maze[i][j] == 'G':
                goals.append((i, j))

            if maze[i][j] == 'S':
                commandos.append((i, j))

            if maze[i][j] == 'B':
                goals.append((i, j))

    all_shortest_paths()
    Q = []
    heapq.heappush(Q, (heuristic(commandos, 0), commandos, ''))
    visited.add(tuple(commandos))

    while Q:
        act_state = heapq.heappop(Q)
        positions = act_state[1]
        moves = act_state[2]

        if mission_complete(positions):
            # print('\nANSWER')
            # print(moves, len(moves))
            print_answer(moves)
            break

        for i in range(4):
            new_positions = make_new_pos(i, positions)

            if good_move(new_positions):
                heapq.heappush(Q, (heuristic(new_positions, len(moves) + 1), new_positions, moves + vec_to_pos(i)))
                # print(act_state, ' - > ', new_positions, heuristic(new_positions, len(moves) + 1))