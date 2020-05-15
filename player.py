#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 alanaudi <alanaudi.tw@gmail.com>
#

# {{{
# Standard import

# Third-party import

# Local import
from hand import Hand
# }}}

num_of_roles = 3
ROLES = ('Slave', 'Citizen', 'Emperor')

class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = ROLES.index(role)
        self.hand = Hand(self.role)
        self.score = 0

