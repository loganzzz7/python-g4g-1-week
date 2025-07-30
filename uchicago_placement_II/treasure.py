class Treasure:
    def __init__(self, treasure_type: str, amount: int):
        self.treasure_type = treasure_type.lower()
        self.amount = amount

    def get_treasure_value(self):
        if self.treasure_type == "diamond":
            return self.amount * 5
        elif self.treasure_type == "gold":
            return self.amount * 3
        elif self.treasure_type == "silver":
            return self.amount
        else:
            return 0

class Player:
    def __init__(self, name: str):
        self.name = name
        self.pieces = []
        self.treasures = []
        
    def add_piece(self, piece):
        self.pieces.append(piece)
    
    def get_treasure(self, treasure):
        self.treasures.append(treasure)
    
    def drop_lowest_val(self):
        if not self.treasures:
            return None
        
        lowest = self.treasures[0]
        
        for treasure in self.treasures[1:]:
            if treasure.get_treasure_value() < lowest.get_treasure_value():
                lowest = treasure
        self.treasures.remove(lowest)
        return lowest

    def get_player_score(self):
        # ran out of time