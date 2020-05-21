#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 alanaudi <alanaudi.tw@gmail.com>
#

# {{{
# Standard import
from random import shuffle
# Third-party import

# Local import
from card import Card
# }}}

ROLES = ('Slave', 'Citizen', 'Emperor')


class Hand:
    def __init__(self, role):
        self.cards = ["Citizen"] * 4 + [ROLES[role]]
        self.cards = [Card(ROLES.index(card)) for card in self.cards]
        shuffle(self.cards)

    def remove_card(self, card):
        self.cards.remove(ROLES[card.role.iden])

    def size(self):
        return len(self.cards)

    def __str__(self):
        return ", ".join(self.cards)
