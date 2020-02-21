from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Stephen", room['outside'])
choice = input("Press M to start or Q to quit.").lower()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(f'Welcome {player.name}')

while choice != "":
    print("\n", player)

    if choice == "q":
        print("You quit the game!")
        break

    elif choice == "m":
        move = input("where would you like to go?\n Press N to go North, S to go South, E to go East, W to go West, and Q to Quit: ").lower()

        if move == "q":
            print("You quit the game!")
            break

        elif move == "n":
            if player.current_room == room['outside']:
                player.current_room = room['outside'].n_to
            elif player.current_room == room['foyer']:
                player.current_room = room['foyer'].n_to
            elif player.current_room == room['narrow']:
                player.current_room = room['narrow'].n_to
            else:
                print("That way is Forbidden, you cannot go there!")
                continue

        elif move == "s":
            if player.current_room == room['overlook']:
                player.current_room = room['overlook'].s_to
            elif player.current_room == room['foyer']:
                player.current_room = room['foyer'].s_to
            elif player.current_room == room['treasure']:
                player.current_room = room['treasure'].s_to
            else:
                print("That way is Forbidden, you cannot go there!")
                continue

        elif move == "e":
            if player.current_room == room['foyer']:
                player.current_room = room['foyer'].e_to
            else:
                print("That way is Forbidden, you cannot go there!")
                continue

        elif move == "w":
            if player.current_room == room['narrow']:
                player.current_room = room['narrow'].w_to
            else:
                print("That way is Forbidden, you cannot go there!")
                continue

    else:
        print(f"Sorry but the chosen Option: {choice} does not exist.")
