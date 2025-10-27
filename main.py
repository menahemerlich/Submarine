from submarines.board import create_matrix, create_bool_matrix, in_bounds, count_remaining_ships, render_public

ships = create_matrix(3)
shots = create_bool_matrix(3)
print(in_bounds(3, 4, 3))
print(count_remaining_ships(ships, shots))
print(render_public(ships, shots))