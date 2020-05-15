#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright © 2020 alanaudi <alanaudi.tw@gmail.com>
#

# Standard import
import os
import sys

# Third-party import

# Local import
from player import Player


class ECard:
    def __init__(self, line:int=5):
        self.slave = Player("伊藤開司", "Slave")
        self.emperor = Player("利根川幸雄", "Emperor")

    def play(self):
        # Initialize Game Message
        print(F'Welcome to the ECard Game, {self.slave.name}')
        print(F'I\' {self.emperor.name}')


def main():
    game = ECard(line=5)
    game.play()

if "__main__" == __name__:
    main()
