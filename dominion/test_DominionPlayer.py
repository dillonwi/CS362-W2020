from unittest import TestCase
import Dominion


class TestPlayer(TestCase):
    def test_action_balance(self):
        # establish the player (John), an action card (Market), and a non-action card (Silver)
        player = Dominion.Player('John')
        MarketCard = Dominion.Action_card("Market", 5, 1, 1, 1, 1)
        VillageCard = Dominion.Action_card("Village", 3, 2, 1, 0, 0)

        SilverCard = Dominion.Silver()

        # Check to see that the action balance function returns 0 if no action cards have been added to the player's stack.
        checkNumber = player.action_balance()
        self.assertEqual(0, checkNumber)

        # Append the Silver card to the player's stack, then ensure that the action balance still returns 0.
        player.deck.append(SilverCard)

        # Set a variable for the player's stack
        pStack = player.stack()
        self.assertEqual(11, len(pStack))
        checkNumber = player.action_balance()
        self.assertEqual(0, checkNumber)

        # Append the Market card to the stack, and ensure that the action balance STILL returns 0 (70 * 0 / 12 = 0)
        player.deck.append(MarketCard)
        pStack = player.stack()

        self.assertEqual(12, len(pStack))
        checkNumber = player.action_balance()
        self.assertEqual(0, checkNumber)

        # Append 2 Village cards to the stack and verify that it now has 14 cards in the stack.
        player.deck.append(VillageCard)
        player.deck.append(VillageCard)
        pStack = player.stack()
        self.assertEqual(14, len(pStack))

        # Set checkNumber to the returned value from action_balance. I expect it to be 10 (70 * 2 / 14 = 10)
        checkNumber = player.action_balance()
        self.assertEqual(10, checkNumber)

        pass


class TestPlayer(TestCase):
    def test_calcpoints(self):
        # establish the player (Eric), a duchy card (), and a garden card
        player = Dominion.Player('Eric')
        dCard = Dominion.Duchy()
        gCard = Dominion.Gardens()

        # run calc points, and validate that the player has 3 victory points.
        # We expect 3 Vpoints to begin because using the order of operations for Python, we do 10 // 10 * 0 + 3 in that order, giving us the answer 3.
        victoryTotal = player.calcpoints()
        self.assertEqual(victoryTotal, 3)

        # Set a variable for the player's stack A

        # Append the Duchy card to the player's stack, then ensure that the length is 11 now.
        player.deck.append(dCard)
        pStack = player.stack()
        self.assertEqual(11, len(pStack))

        # After adding the duchy card, we would expect the victory point total to be 6.
        # The math is now: 11 // 10 * 0 + 6.
        victoryTotal = player.calcpoints()
        self.assertEqual(victoryTotal, 6)

        # Append the Garden card to the player's stack and check that the length is 12 now.
        player.deck.append(gCard)
        pStack = player.stack()
        self.assertEqual(12, len(pStack))

        # After adding the garden card, we would expect the victory point total to be 7.
        # The math is now: 12 // 10 * 1 + 6.
        victoryTotal = player.calcpoints()
        self.assertEqual(victoryTotal, 7)

        pass


class TestPlayer(TestCase):
    def test_draw(self):
        player = Dominion.Player('Eric')
        # Create a Silver  and Copper Card. We will use this for the discard and deck.
        SilverCard = Dominion.Silver()
        CopperCard = Dominion.Copper()

        # Before drawing, check to see that the length of the player's hand is 5, then draw
        self.assertEqual(5, len(player.hand))
        player.draw()

        # After drawing, check to see that the length of the player's hand is 6.
        # There was no destination specified, and the deck has more than 0 cards so the card should go to the player's hand.
        # Also verify that the length of the deck is 4. One card was drawn, so it should be 4.
        self.assertEqual(6, len(player.hand))
        self.assertEqual(4, len(player.deck))

        # Append 5 Silvers and 2 Coppers to the discard pile.
        player.discard.append(SilverCard)
        player.discard.append(SilverCard)
        player.discard.append(SilverCard)
        player.discard.append(CopperCard)
        player.discard.append(CopperCard)
        player.discard.append(SilverCard)
        player.discard.append(SilverCard)

        # Keep drawing cards until the deck has one left.
        player.draw()
        player.draw()
        player.draw()

        # check to see that the length of the player's deck is 1
        self.assertEqual(1, len(player.deck))

        # draw one more time. After doing this, there should be no more cards left in the deck.
        player.draw()
        self.assertEqual(0, len(player.deck))

        # When the player goes to draw, the discard pile should be shuffled to become the new deck, and one more card will be drawn.
        # As such, the deck should have 6 cards after this (0 + 7 -1)
        player.draw()
        self.assertEqual(6, len(player.deck))

        # Test that the discard pile now no longer has anything.
        self.assertEqual(0, len(player.discard))

        # Test the effects of drawing a card with the DISCARD as the specified destination.
        # This should increase the discard count by 1, and reduce the deck count to 5.
        player.draw(player.discard)
        self.assertEqual(5, len(player.deck))
        self.assertEqual(1, len(player.discard))

        pass


class TestPlayer(TestCase):
    def test_cardsummary(self):
        #initialize a silver, copper, and duchy card and a player.
        player = Dominion.Player('Jerry')
        SilverCard = Dominion.Silver()
        CopperCard = Dominion.Copper()
        dCard = Dominion.Duchy()

        #Establish a new variable that is equal to the value returned from calling cardsummary.
        summaryVar = player.cardsummary()

        #After running the card summary, there should have been 3 victory points and 7 copper cards counted.
        #As such, we will asset that the total number of victory points is 3, and the number of copper cards is 7.
        self.assertEqual(3, summaryVar['VICTORY POINTS'])
        self.assertEqual(7, summaryVar['Copper'])

        #Next we will append the silver card and Copper Card to the player's deck. This will result in these cards being in the stack.
        player.deck.append(SilverCard)
        player.deck.append(CopperCard)

        #Run the summary again
        summaryVar = player.cardsummary()

        #Check that the values are what we expect.
        self.assertEqual(3, summaryVar['VICTORY POINTS'])
        self.assertEqual(8, summaryVar['Copper'])
        self.assertEqual(1, summaryVar['Silver'])

        #Append the Duchy card to the player's hand
        player.hand.append(dCard)

        # Run the summary again
        summaryVar = player.cardsummary()

        # Check that the values are what we expect. The duchy card will increase the victory points by 3.
        self.assertEqual(6, summaryVar['VICTORY POINTS'])
        self.assertEqual(8, summaryVar['Copper'])
        self.assertEqual(1, summaryVar['Silver'])


        pass