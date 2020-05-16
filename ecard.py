#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# {{{
# Standard import
import os
import sys
from time import sleep
import random
from functools import reduce
# Third-party import

# Local import
from player import Player
from color import Color
# }}}

def typing(msg):
    for char in msg:
        sleep(random.choice([0.01, 0.03, 0.05, 0.07, 0.09]))
        sys.stdout.write(char)
        sys.stdout.flush()

class ECard:
    def __init__(self, line:int=5):
        self.slave = Player("伊藤開司", "Slave")
        self.emperor = Player("利根川幸雄", "Emperor")
        self.winner = None
        self.loser = None
        self.players = []


    @staticmethod
    def show_cards(cards):
        hand = reduce(lambda x, y: [x[i]+y[i] for i in range(6)], [card.skin for card in cards])
        print('\n'.join(hand))

    def start(self, name):
        self.slave.name = name

        # Initialize Game Message
        typing(F'Welcome to the ECard Game, {Color.BLUE}{self.slave.name}{Color.ENDC}\n')
        typing(F'I\'m {self.emperor.name}\n')
        sleep(0.5)
        typing(F'In this game, you have the following 5 cards,\n')
        self.show_cards(self.slave.hand.cards)
        sleep(1)
        typing(F'And I also have 5 cards below.\n')
        self.show_cards(self.emperor.hand.cards)
        typing(F'Emperor counter citizen, citizen counter slave and slave counter emperor.\n')

    def who_first(self, side):
        self.slave.side = 'offensive' if side == 'Slave' else 'defensive'
        self.emperor.side = 'offensive' if side == 'Emperor' else 'defensive'
        self.players.append(self.slave if self.slave.side == 'offensive' else self.emperor)
        self.players.append(self.slave if self.slave.side == 'defensive' else self.emperor)
        typing(F'Now the offensive side is {(self.players[0]).name} and the defensive side is {(self.players[1]).name}\n')

    def act(self):
        print([(player.name, player.side) for player in self.players])



def main():
    name = input('What\'s your name, challenger.\n')
    game = ECard(line=5)
    game.start(name)
    first = input('Please select the role who first.\n❯ Slave\n❯ Emperor\n')
    game.who_first(first)
    # while game.winner is not None:
    game.act()
    # while game.winner is None:



if "__main__" == __name__:
    main()
