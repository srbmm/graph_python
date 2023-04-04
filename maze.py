from Graph import Graph
import matplotlib.pyplot as plt

#inp ex1
inp = """0 0 1 1 0
0 0 0 1 0
0 1 0 0 0
0 1 1 0 0
1 0 1 1 0
0 1 0 0 0
0 0 0 1 1
0 1 0 1 1"""

# inp = ""
# for i in range(8):
#     inp += input(f"line-{i + 1}:")
#     if i != 7:
#         inp += "\n"

plt.axis([1, 6, 6, 1])

plt.plot([1, 1], [1, 6], color='blue', linewidth=10)
plt.plot([1, 6], [1, 1], color='blue', linewidth=10)
plt.plot([6, 6], [1, 6], color='blue', linewidth=10)
plt.plot([1, 6], [6, 6], color='blue', linewidth=10)


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
        if row[i][j] == "1":
            pass
            plt.plot([temp_j, temp_j+1],[temp_i+1, temp_i+1], color="blue", linewidth=5)
        else:
            if i < 5:
                my_graph.connect_to_getter(f"{temp_i},{temp_j}", f"{temp_i+1},{temp_j}", 3)

for i in range(5):
    for j in range(4):
        temp_i = i + 1
        temp_j = j + 1
        if col[j][i] == "1":
            plt.plot([temp_j+1, temp_j+1], [temp_i, temp_i+1], color="blue", linewidth=5)
        else:
            if i < 5:
                my_graph.connect_to_getter(f"{temp_i},{temp_j}", f"{temp_i},{temp_j+1}", 1)


res = my_graph.ucs('1,1', '5,5')
for i in range(len(res[1]) - 1):
    temp_i, temp_j = res[1][i].split(",")
    temp_i = int(temp_i)
    temp_j = int(temp_j)
    next_i, next_j = res[1][i+1].split(",")
    next_i = int(next_i)
    next_j = int(next_j)
    print([temp_j+0.5, next_j+0.5], [temp_i+0.5, next_i+0.5])
    plt.plot([temp_j+0.5, next_j+0.5], [temp_i+0.5, next_i+0.5], "-o", linewidth=2)

plt.show()
print(res)
