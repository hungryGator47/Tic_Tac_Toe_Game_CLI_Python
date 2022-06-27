import grid


def main():

    chosen_position = None
    player_X_choice = None
    player_O_choice = None

    ### Beginning screen ###
    print("\n--- Tic Tac Toe ---\n")
    grid.print_grid()

    while True: # main game loop

        ### Player X's chance ###
        print("\nPlayer X")
        while True:
            player_X_choice = input("> ")
            if player_X_choice not in grid.possible_input: # checks if input is valid
                print("Invalid input!")
                continue
            if player_X_choice in grid.taken_positions: # checks if position is already taken
                print("Position already taken!")
                continue
            break
        grid.taken_positions.append(player_X_choice) # this is now a taken position and cannot be taken anymore
        chosen_position = player_X_choice
        grid.update_grid(chosen_position, grid.X)
        print()
        grid.print_grid()

        ### Checking if player X won ###
        if \
            (grid.position['1'] == grid.X and grid.position['2'] == grid.X and grid.position['3'] == grid.X) \
        or  (grid.position['4'] == grid.X and grid.position['5'] == grid.X and grid.position['6'] == grid.X) \
        or  (grid.position['7'] == grid.X and grid.position['8'] == grid.X and grid.position['9'] == grid.X) \
        or  (grid.position['1'] == grid.X and grid.position['4'] == grid.X and grid.position['7'] == grid.X) \
        or  (grid.position['2'] == grid.X and grid.position['5'] == grid.X and grid.position['8'] == grid.X) \
        or  (grid.position['3'] == grid.X and grid.position['6'] == grid.X and grid.position['9'] == grid.X) \
        or  (grid.position['1'] == grid.X and grid.position['5'] == grid.X and grid.position['9'] == grid.X) \
        or  (grid.position['7'] == grid.X and grid.position['5'] == grid.X and grid.position['3'] == grid.X):
            print("\nPlayer X wins!")
            break # game over

        ### Checks if game is a draw ###
        if grid.all_positions_have_changed(grid.position, grid.original_positions):
            print("\nIt's a draw!")
            break # game over

        ### Player O's chance ###
        print("\nPlayer O")
        while True:
            player_O_choice = input("> ")
            if player_O_choice not in grid.possible_input: # checks if input is valid
                print("Invalid input!")
                continue
            if player_O_choice in grid.taken_positions: # checks if position is already taken
                print("Position already taken!")
                continue
            break
        grid.taken_positions.append(player_O_choice) # this is now a taken position and cannot be taken anymore
        chosen_position = player_O_choice
        grid.update_grid(chosen_position, grid.O)
        print()
        grid.print_grid()
        
        ### Checking if player O won ###
        if \
            (grid.position['1'] == grid.O and grid.position['2'] == grid.O and grid.position['3'] == grid.O) \
        or  (grid.position['4'] == grid.O and grid.position['5'] == grid.O and grid.position['6'] == grid.O) \
        or  (grid.position['7'] == grid.O and grid.position['8'] == grid.O and grid.position['9'] == grid.O) \
        or  (grid.position['1'] == grid.O and grid.position['4'] == grid.O and grid.position['7'] == grid.O) \
        or  (grid.position['2'] == grid.O and grid.position['5'] == grid.O and grid.position['8'] == grid.O) \
        or  (grid.position['3'] == grid.O and grid.position['6'] == grid.O and grid.position['9'] == grid.O) \
        or  (grid.position['1'] == grid.O and grid.position['5'] == grid.O and grid.position['9'] == grid.O) \
        or  (grid.position['7'] == grid.O and grid.position['5'] == grid.O and grid.position['3'] == grid.O):
            print("\nPlayer O wins!")
            break # game over


# Run program
main()
