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
from card import Role, Card
# }}}

ROLES = ('Slave', 'Citizen', 'Emperor')

class Hand:
    def __init__(self, role):
        self.hand = ["Citizen"] * 4 + [ROLES[role]]
        shuffle(self.hand)

    def remove_card(self, card):
        self.hand.remove(ROLES[card.role.iden])

    def size(self):
        return len(self.hand)

    def __str__(self):
        return ", ".join(self.hand)
