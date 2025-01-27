import items, characters, actions, world


class MapTile:
    """The base class for a tile within the world space"""

    def __init__(self, x, y):
        """Creates a new tile.

        :param x: the x-coordinate of the tile
        :param y: the y-coordinate of the tile
        """
        self.x = x
        self.y = y

    def intro_text(self):
        """Information to be displayed when the player moves into this tile."""
        raise NotImplementedError()

    def modify_player(self, the_player):
        """Process actions that change the state of the player."""
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return """
        The mechanical ring of your alarm clock jars you into a hazy half-
        conscious state after your unconscious brain tried to clumsily 
        shoehorn the noise into your dream about cats. You pound it to shut
        it off, abusing the device as well as the side of your hand. For a 
        brief moment, you manage to think about something other than your 
        current reality. This is always the best half minute of the day. 
        You wonder how much stress could have been saved back in the day 
        had people gone for a more soothing sound to wake up to. If you had
        any other non-electronic options, you'd surely choose any one of 
        them over the ear-splitting repetition of pounding bells you've 
        been subjecting yourself to for the past two weeks. You miss your 
        Spotify Handel playlist, but you can't risk it anymore. And the 
        blissful moment of forgetfulness is over as you settle into the 
        realization that everything is exactly as it was when you went to 
        bed. You look around, but you can't see much. On the bedside table 
        is the alarm clock, your glasses, a huge pair of what look like 
        pink fluffy earmuffs, and a crumpled newspaper.
        """

    def modify_player(self, the_player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    """A room that adds something to the player's inventory"""

    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class CharacterRoom(MapTile):
    def __init__(self, x, y, character):
        self.character = character
        super().__init__(x, y)

    def modify_player(self, the_player):
        pass

    def available_actions(self):
        if self.character.is_alive():
            return [actions.Converse(character=self.character)]
        else:
            return self.adjacent_moves()


class DadJokeRoom(CharacterRoom):
    def __init__(self, x, y):
        super().__init__(x, y, characters.DadJokeGuy())

    def intro_text(self):
        return """
        Your dad is in his usual spot on the couch, watching Rush document-
        aries and crocheting a blanket. The blanket has gotten to an unman-
        ageable size, and you almost trip on it.
        """


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!


        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True
