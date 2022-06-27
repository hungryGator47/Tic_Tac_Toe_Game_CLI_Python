position = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

original_positions = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

X = 'X'
O = 'O'

possible_input = ( '1', '2', '3', '4', '5', '6', '7', '8', '9' )
taken_positions = []


def update_grid(chosen_position, symbol):
    position.update({chosen_position: symbol})


def print_grid():
    print(f" {position['1']} | {position['2']} | {position['3']}")
    print(f"---|---|---                                         ")
    print(f" {position['4']} | {position['5']} | {position['6']}")
    print(f"---|---|---                                         ")
    print(f" {position['7']} | {position['8']} | {position['9']}")


def all_positions_have_changed(position, original_positions):
    number_of_original_positions = len(position)
    number_of_values_changed = 0

    # Find number of values changed
    for key in position:
        if position[key] != original_positions[key]:
            number_of_values_changed += 1

    # Check and return weather all positions have changed
    if (number_of_values_changed == number_of_original_positions):
        return True
    else:
        return False
