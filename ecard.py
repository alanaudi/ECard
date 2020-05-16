#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright © 2020 alanaudi <alanaudi.tw@gmail.com>
#

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
# }}}

def typing(msg):
    for char in msg:
        sleep(random.choice([0.01, 0.03, 0.05, 0.07, 0.09]))
        sys.stdout.write(char)
        sys.stdout.flush()

def show_cards(cards):
    hand = reduce(lambda x, y: [x[i] + y[i] for i in range(6)], [card.skin for card in cards])
    print('\n'.join(hand))

class ECard:
    def __init__(self, line:int=5):
        self.slave = Player("伊藤開司", "Slave")
        self.emperor = Player("利根川幸雄", "Emperor")

    def play(self):
        # Initialize Game Message
        typing(F'Welcome to the ECard Game, {self.slave.name}\n')
        typing(F'I\'m {self.emperor.name}\n')
        sleep(0.5)
        typing(F'In this game, you have the following 5 cards,\n')
        show_cards(self.slave.hand.cards)

def main():
    game = ECard(line=5)
    game.play()


if "__main__" == __name__:
    main()
