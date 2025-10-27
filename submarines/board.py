
def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    ships = []
    for i in range(size):
        ships.append([])
        for j in range(size):
            ships[i].append(fill)
    return ships

def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    shots = []
    for i in range(size):
        shots.append([])
        for j in range(size):
            shots[i].append(fill)
    return shots

def in_bounds(size: int, x: int, y:int) -> bool:
    if x <= size and y <= size:
        return True
    return False

def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]) -> int:
    count = 0
    for i in range(len(ships)):
        for j in range(len(ships)):
            if ships[i][j] == 1 and shots[i][j] == False:
                count += 1
    return count


def render_public(ships: list[list[int]], shots: list[list[bool]]) -> str:
    pass



