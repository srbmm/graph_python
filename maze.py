from Graph import Graph

#inp ex1
# inp = """0 0 1 1 0
# 0 0 0 1 0
# 0 1 0 0 0
# 0 1 1 0 0
# 1 0 1 1 0
# 0 1 0 0 0
# 0 0 0 1 1
# 0 1 0 1 1"""


#inp ex2
# inp = """0 1 0 0 0
# 0 1 1 0 0
# 0 0 0 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 0 1 0 0 0
# 1 0 1 1 0
# 0 0 1 1 0"""

inp = ""
for i in range(8):
    inp += input(f"line-{i + 1}:")
    if i != 7:
        inp += "\n"


def str_to_row_and_col(inp):
    inp = inp.split('\n')
    matrix = list(map(lambda x: x.split(), inp))
    return matrix[0:4], matrix[4:]

my_graph = Graph()
row, col = str_to_row_and_col(inp)

for i in range(4):
    for j in range(5):
        temp_i = i + 1
        temp_j = j + 1
        if row[i][j] != '1' and i + 1 < 5:
            my_graph.connect_to_getter(f"{temp_i}, {temp_j}", f"{temp_i + 1}, {temp_j}", 1)
            print(temp_i, temp_j, "--->", temp_i+1, temp_j)
        if row[i][j] != '1' and j + 1 < 5:
            my_graph.connect_to_getter(f"{temp_i}, {temp_j}", f"{temp_i}, {temp_j + 1}", 3)
            print(temp_i, temp_j, "--->", temp_i, temp_j+1)



def my_ucs(graph, start, goal):
    return graph.ucs(str(start), str(goal))


print(my_ucs(my_graph, "1, 1", "5, 5"))
