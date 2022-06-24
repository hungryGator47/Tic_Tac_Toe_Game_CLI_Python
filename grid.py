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


def update_grid(chosen_position, symbol):
    position.update({chosen_position: symbol})


def print_grid():
    print(f" {position['1']} | {position['2']} | {position['3']}")
    print(f"---|---|---                                         ")
    print(f" {position['4']} | {position['5']} | {position['6']}")
    print(f"---|---|---                                         ")
    print(f" {position['7']} | {position['8']} | {position['9']}")


X = 'X'
O = 'O'

possible_input = ( '1', '2', '3', '4', '5', '6', '7', '8', '9' )
taken_positions = []

