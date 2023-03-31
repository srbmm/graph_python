from Graph import Graph
MATRIX_NUMBER = 4
inp = """0 0 1 1 0
0 0 0 1 0
0 1 0 0 0
0 1 1 0 0
1 0 1 1 0
0 1 0 0 0
0 0 0 1 1
0 1 0 1 1"""


def str_to_row_and_col(inp):
    inp = inp.split('\n')
    matrix = list(map(lambda x: x.split(), inp))
    return matrix[0:4], matrix[4:]

my_graph = Graph()
row, col = str_to_row_and_col(inp)

for i in range(MATRIX_NUMBER):
    for j in range(MATRIX_NUMBER):
        temp_i = i + 1
        temp_j = j + 1
        #
        if row[i][j] != '1' and i+1 <= MATRIX_NUMBER:
            my_graph.connect_to_getter(f"{sorted([temp_i,temp_j])}", f"{sorted([temp_i + 1,temp_j])}", 1)
        if row[i][j] != '1' and j + 1 <= MATRIX_NUMBER:
            my_graph.connect_to_getter(f"{sorted([temp_i,temp_j])}", f"{sorted([temp_i,temp_j + 1])}", 3)


def my_ucs(graph, start, goal):
    start.sort()
    goal.sort()
    return graph.ucs(str(start), str(goal))


print(my_ucs(my_graph, [1, 1], [4, 4]))
