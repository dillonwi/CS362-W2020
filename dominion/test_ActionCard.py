from unittest import TestCase
import Dominion


class TestAction_card(TestCase):
    def test_use(self):
        # Initialize a Market action card
        card = Dominion.Action_card("Market", 5, 1, 1, 1, 1)
        self.assertEqual(card.name, "Market")
        self.assertEqual(card.cost, 5)
        self.assertEqual(card.actions, 1)
        self.assertEqual(card.cards, 1)
        self.assertEqual(card.buys, 1)
        self.assertEqual(card.coins, 1)

        # Initialize a player and trash
        player = Dominion.Player('John')
        trash = []

        # Ensure that the player has 5 cards in hand and nothing in the played pile
        self.assertEqual(5, len(player.hand))
        self.assertEqual(0, len(player.played))

        # Append the card to the player's hand, then ensure that their hand has increased by 1
        player.hand.append(card)
        self.assertEqual(6, len(player.hand))

        # Use the card and see if the player's hand decreases by 1, and the played pile increases by 1.
        card.use(player, trash)
        self.assertEqual(5, len(player.hand))
        self.assertEqual(1, len(player.played))

        return 0

class TestAction_card(TestCase):
    def test_augment(self):
        player = Dominion.Player('John')
        card = Dominion.Action_card("Market", 5, 1, 1, 1, 1)

        #Add action, buys, and purse attributes to the player. They usually get these from playing turns, but for the sake of
        #simplification and testing, I have decided to give them these attributes manually.
        player.actions = 2
        player.buys = 3
        player.purse = 4

        #Check that the player has 5 cards in their hand. After Augment is run, the player will have another card in their hand.
        self.assertEqual(5, len(player.hand))

        #Run the augment function for the player. We are going to use the Market card to augment the player in this case.
        card.augment(player)

        #After this, the actions should be 3, buys should be 4, and purse should be 5. Also, there should be another card in the player's hand.
        self.assertEqual(3, player.actions)
        self.assertEqual(4, player.buys)
        self.assertEqual(5, player.purse)
        self.assertEqual(6, len(player.hand))

        #initialize more action cards to be augmented to the player.
        card2 = Dominion.Woodcutter()
        card3 = Dominion.Festival()

        #Run the augment function on both of these cards
        card2.augment(player)
        card3.augment(player)

        #After doing so, the player's action count should be 5 (3 plus 0 from the Woodcutter and 2 from the Festival)
        self.assertEqual(5, player.actions)

        #The player's buys count should be 6 (4 plus 1 from the Woodcutter and 1 from the Festival)
        self.assertEqual(6, player.buys)

        #The player's purse count should be 9 (5 plus 2 from the Woodcutter and 2 from the Festival)
        self.assertEqual(9, player.purse)

        pass
