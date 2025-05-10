from pygame.sprite import Group

from dataclasses import dataclass

@dataclass
class ObjectGroups:
    updatable: Group
    drawable: Group
    asteroids: Group
    shots: Group
    menu_updatable: Group
    menu_drawable: Group
