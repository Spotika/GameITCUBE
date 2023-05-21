import pygame
from App import App
from Designs.MainGameDesign import MainGameDesign
from EventHandler import EventHandler
from Sprites.Platform import PlatformGenerator
from Sprites.Money import MoneyGenerator
from Sprites.MobGenerator import MobGenerator
from Abilities.ShurikenAttack import ShurikenAttack


class MainGameApp(App, MainGameDesign):
    """Сама игра"""

    ability1 = None
    ability2 = None
    ability3 = None

    @classmethod
    def loop(cls, *args, **kwargs):
        cls.init_textures()
        cls.init_sprites_and_groups()

        # создание генератора платформ
        cls.platformGenerator = PlatformGenerator(cls.allSprites)

        # привязка класса к игроку
        cls.get_element("player").set_app(cls)
        cls.get_element("player").add_to_collision_env_functions(
            cls.get_element("HUD").collision_function
        )

        player = cls.get_element("player")

        # создание генератора монет
        cls.moneyGenerator = MoneyGenerator(cls.allSprites, cls.platformGenerator, player)

        # создание генератора мобов
        cls.mobGenerator = MobGenerator(cls.allSprites, player)

        # подключение трекеров
        cls.get_element("HUD").get_design("healthTracker").add_state(player.get_health)
        cls.get_element("HUD").get_design("manaTracker").add_state(player.get_mana)
        cls.get_element("HUD").get_design("strengthTracker").add_state(player.get_strength)
        cls.get_element("HUD").get_design("dexterityTracker").add_state(player.get_dexterity)
        cls.get_element("HUD").get_design("intelligenceTracker").add_state(player.get_intelligence)
        cls.get_element("HUD").get_design("moneyTracker").add_state(player.get_money)
        cls.get_element("HUD").get_design("levelTracker").add_state(player.get_level)
        cls.get_element("HUD").get_design("experienceTracker").add_state(
            lambda: f"{player.experience}/{player.experience_for_next}")

        cls.ability1 = cls.get_element("HUD").get_design("ability1")
        cls.ability2 = cls.get_element("HUD").get_design("ability2")
        cls.ability3 = cls.get_element("HUD").get_design("ability3")

        cls.ability1.add_ability(ShurikenAttack, player)

        while cls.running:
            EventHandler.tick()

            EventHandler.update(cls)

            cls.platformGenerator.update()

            cls.moneyGenerator.update()

            cls.mobGenerator.update()

            cls.check_events()

            cls.render()

        cls.end(*args, **kwargs)

    @classmethod
    def check_events(cls):
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cls.redirect("MainMenuApp")
                    cls.end()

                match event.key:

                    case pygame.K_z:
                        cls.ability1.call()

                    case pygame.K_x:
                        cls.ability2.call()

                    case pygame.K_c:
                        cls.ability3.call()
