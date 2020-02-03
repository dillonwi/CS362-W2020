from unittest import TestCase
import Dominion
import random
from collections import defaultdict


class Test(TestCase):
    def test_gameover(self):

        #Establish a box and supply just like you would in a realistic game.
        box = {}
        box["Woodcutter"] = [Dominion.Woodcutter()] * 10
        box["Smithy"] = [Dominion.Smithy()] * 10
        box["Laboratory"] = [Dominion.Laboratory()] * 10
        box["Village"] = [Dominion.Village()] * 10
        box["Festival"] = [Dominion.Festival()] * 10
        box["Market"] = [Dominion.Market()] * 10
        box["Chancellor"] = [Dominion.Chancellor()] * 10
        box["Workshop"] = [Dominion.Workshop()] * 10
        box["Moneylender"] = [Dominion.Moneylender()] * 10
        box["Chapel"] = [Dominion.Chapel()] * 10
        box["Cellar"] = [Dominion.Cellar()] * 10
        box["Remodel"] = [Dominion.Remodel()] * 10
        box["Adventurer"] = [Dominion.Adventurer()] * 10
        box["Feast"] = [Dominion.Feast()] * 10
        box["Mine"] = [Dominion.Mine()] * 10
        box["Library"] = [Dominion.Library()] * 10
        box["Gardens"] = [Dominion.Gardens()] * 5
        box["Moat"] = [Dominion.Moat()] * 10
        box["Council Room"] = [Dominion.Council_Room()] * 10
        box["Witch"] = [Dominion.Witch()] * 10
        box["Bureaucrat"] = [Dominion.Bureaucrat()] * 10
        box["Militia"] = [Dominion.Militia()] * 10
        box["Spy"] = [Dominion.Spy()] * 10
        box["Thief"] = [Dominion.Thief()] * 10
        box["Throne Room"] = [Dominion.Throne_Room()] * 10

        supply_order = {0: ['Curse', 'Copper'], 2: ['Estate', 'Cellar', 'Chapel', 'Moat'],
                        3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
                        4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy',
                            'Thief',
                            'Throne Room'],
                        5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
                        6: ['Gold', 'Adventurer'], 8: ['Province']}

        # Pick 10 cards from box to be in the supply.
        boxlist = [k for k in box]
        random.shuffle(boxlist)
        random10 = boxlist[:10]
        supply = defaultdict(list, [(k, box[k]) for k in random10])

        # The supply always has these cards
        supply["Copper"] = [Dominion.Copper()] * (60 - 21)
        supply["Silver"] = [Dominion.Silver()] * 40
        supply["Gold"] = [Dominion.Gold()] * 30
        supply["Estate"] = [Dominion.Estate()] * 5
        supply["Duchy"] = [Dominion.Duchy()] * 5
        supply["Province"] = [Dominion.Province()] * 5
        supply["Curse"] = [Dominion.Curse()] * 5

        #Set the variable, gameOverbool to the result of running the supply through gameover.
        gameOverbool = Dominion.gameover(supply)

        #Gameover should return false because there is at least one province card which is represented by the False here.
        self.assertEqual(False, gameOverbool)

        #Reduce the number of province cards in the supply to 0.
        supply["Province"] = [Dominion.Province()] * 0

        # Set the variable, gameOverbool to the result of running the supply through gameover.
        gameOverbool = Dominion.gameover(supply)

        # Gameover should return true. There are no more province cards in the supply, so the game SHOULD be over.
        self.assertEqual(True, gameOverbool)

        pass
