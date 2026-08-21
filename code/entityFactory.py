#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH
from code.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                # Utiliza os arquivos existentes na sua pasta asset
                for i in [0, 2, 3, 4, 5, 6, 7]:
                    # Primeira cópia (visível de início)
                    list_bg.append(Background(f'level1Bg{i}', (0, 0)))
                    # Segunda cópia (emendada à direita para rolagem contínua)
                    list_bg.append(Background(f'level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

        return None