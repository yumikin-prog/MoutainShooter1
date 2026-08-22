#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.enemy import Enemy
from code.player import Player


class EntityMediator:

    @staticmethod
    def verify_collision(entity_list: list):
        for i in range(len(entity_list)):
            ent1 = entity_list[i]
            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]

                if ent1.rect.colliderect(ent2.rect):

                    # Colisão direta entre Player e Inimigo
                    if isinstance(ent1, Player) and isinstance(ent2, Enemy):
                        ent1.health = 0
                        ent2.health = 0
                    elif isinstance(ent2, Player) and isinstance(ent1, Enemy):
                        ent1.health = 0
                        ent2.health = 0

                    # Tiro do Player no Inimigo
                    elif 'Player' in ent1.name and 'Shot' in ent1.name and isinstance(ent2, Enemy):
                        ent1.health = 0
                        ent2.health -= 1
                    elif 'Player' in ent2.name and 'Shot' in ent2.name and isinstance(ent1, Enemy):
                        ent2.health = 0
                        ent1.health -= 1

                    # Tiro do Inimigo no Player
                    elif 'Enemy' in ent1.name and 'Shot' in ent1.name and isinstance(ent2, Player):
                        ent1.health = 0
                        ent2.health -= 1
                    elif 'Enemy' in ent2.name and 'Shot' in ent2.name and isinstance(ent1, Player):
                        ent2.health = 0
                        ent1.health -= 1

                    # PvP no modo Competitivo
                    elif 'Player' in ent1.name and 'Shot' in ent1.name and isinstance(ent2, Player):
                        if ent1.name != f'{ent2.name}Shot':
                            ent1.health = 0
                            ent2.health -= 1

    @staticmethod
    def verify_health(entity_list: list):
        for ent in list(entity_list):
            if ent.health <= 0 or ent.rect.right < -100 or ent.rect.left > 700:
                entity_list.remove(ent)