# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room, item={}):
        self.name = name
        self.current_room = current_room
        self.item = item

    def __str__(self):
        current = f'You are Currently in the: {self.current_room}'
        return current
