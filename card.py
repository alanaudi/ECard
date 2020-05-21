#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 alanaudi <alanaudi.tw@gmail.com>
#

# {{{
# Standard import

# Third-party import

# Local import

# }}}

ROLES = ('Slave', 'Citizen', 'Emperor')
SKINS = {"Citizen": [".------. ", "|C.--. | ", "| (\\/) | ", "| :\\/: | ", "| '--'C| ", "`------' "],
         "Emperor": [".------. ", "|E.--. | ", "| :(): | ", "| ()() | ", "| '--'E| ", "`------' "],
         "Slave": [".------. ", "|S.--. | ", "| :/\\: | ", "| :\\/: | ", "| '--'S| ", "`------' "]}


class Role:
    """ Role identification
    0: Emperor (E) | 1: Citizen (C)  | 2: Slave  (S)
       .------.    |    .------.     |    .------.
       |S.--. |    |    |C.--. |     |    |S.--. |
       | :/\: |    |    | (\/) |     |    | :/\: |
       | :\/: |    |    | :\/: |     |    | :\/: |
       | '--'S|    |    | '--'C|     |    | '--'S|
       `------'    |    `------'     |    `------'

    Rule: 0 > 1 > 2 > 0
    """

    def __init__(self, iden):
        self.iden = iden
        self.string = ''
        self.skin = SKINS[ROLES[iden]]
        if iden <= 2:
            self.string = ROLES[iden]
        else:
            print("Error: Invalid card identifier.")

    def __eq__(self, other):
        return self.iden - other.iden == 0

    def __gt__(self, other):
        return self.iden - other.iden in (1, -2)

    def __lt__(self, other):
        return self.iden - other.iden in (-1, 2)

    def __str__(self):
        return self.string


class Card:
    def __init__(self, role):
        self.role = Role(role)
        self.skin = self.role.skin

    def __eq__(self, other):
        return self.role == other.role

    def __gt__(self, other):
        return self.role > other.role

    def __lt__(self, other):
        return self.role < other.role
