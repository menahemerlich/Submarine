
def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(fill)
    return matrix

def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(fill)
    return matrix


