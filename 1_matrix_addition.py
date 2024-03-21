x = [
    [1,2,3],
    [9,5,2],
    [8,4,7]
]

y = [
    [1,5,2],
    [3,4,1],
    [6,2,3]
]

result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

for r in result:
    print(r)