import pygame
from Design import Design
from Sprites.BackGrounds import BackGroundParallaxSprite
import Config
from Sprites.Platform import Platform, PlatformGenerator
import random
from Group import Group
from Sprites.FpsShow import FpsShow


class MainGameDesign(Design):

    @classmethod
    def init_textures(cls):
        cls.set_groups({
        })
        ELEMENTS = {
            "backGround": BackGroundParallaxSprite(Config.BackGroundTextures.BACKGROUND_JUNGLE_LAYERS,
                                                   speed_begin=40,
                                                   speed_difference=0.8),
            "fps": FpsShow((100, 100), (0, 0))
        }
        cls.set_elements(ELEMENTS)
