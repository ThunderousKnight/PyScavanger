import pygame
from pygame.surface import Surface
from colors import *
from random import randint


def spawn_random_scrap(amount, bounds):
    scrap_piles = []

    while len(scrap_piles) < amount:
        should_add = True
        scrap = pygame.Rect(randint(0, 800), randint(0, 600), 25, 25)

        if not bounds.collidepoint(scrap.x, scrap.y):
            should_add = False
        else:
            for existing_scrap in scrap_piles:
                if pygame.Rect((existing_scrap[0], existing_scrap[1]), (25, 25)).colliderect(scrap):
                    should_add = False

        if should_add:
            scrap_piles.append((scrap.x, scrap.y, randint(0, 1)))

    return scrap_piles


world_i = 0
scrap_i = 1

room_0_0 = {
    "walls": [
        [
            (0, 0), (0, 200), (50, 200), (50, 125), (125, 50), (675, 50), (750, 125), (750, 475), (675, 550),
            (125, 550), (50, 475), (50, 400), (0, 400), (0, 600), (800, 600), (800, 0)
        ]
    ],
    "scrap_pile_coords": spawn_random_scrap(amount=20, bounds=pygame.Rect((75, 75), (650, 450))),
    "scrap": []
}

room_0_1 = {
    "walls": [
        [(0, 0), (800, 0), (800, 200), (400, 200), (400, 400), (800, 400), (800, 600), (0, 600)]
    ],
    "ellipses": [(25, 25, 750, 550)],
    "scrap_pile_coords": [
        (350, 250, randint(0, 1)),
        (450, 250, randint(0, 1)),
        (350, 350, randint(0, 1)),
        (450, 350, randint(0, 1))
    ],
    "scrap": []
}

room_0_2 = {
    "walls": [
        [
            (0, 0), (0, 200), (50, 200), (50, 50), (400, 50), (400, 200), (450, 200), (450, 50), (750, 50), (750, 600),
            (800, 600), (800, 0)
        ],
        [
            (0, 400), (50, 400), (50, 550), (400, 550), (400, 300), (450, 300), (450, 550), (650, 550), (650, 600),
            (0, 600)
        ]
    ],
    "scrap_pile_coords": [(150, 475, randint(0, 1)), (300, 475, randint(0, 1))],
    "scrap": []
}

room_1_0 = {
    "walls": [
        [(0, 0), (0, 40), (100, 40), (100, 490), (150, 490), (150, 150), (750, 150), (750, 200), (800, 200), (800, 0)],
        [(0, 100), (50, 100), (50, 550), (300, 550), (300, 600), (0, 600)],
        [
            (550, 450), (600, 450), (600, 550), (750, 550), (750, 490), (650, 490), (650, 450), (750, 450), (750, 400),
            (800, 400), (800, 600), (500, 600), (500, 550), (550, 550)
        ]
    ],
    "scrap_pile_coords": [(725, 525, randint(0, 1)), (225, 300, randint(0, 1))],
    "scrap": []
}

room_1_1 = {
    "walls": [
        [(0, 0), (0, 200), (50, 200), (50, 50), (750, 50), (750, 550), (500, 550), (500, 600), (800, 600), (800, 0)],
        [(0, 400), (50, 400), (50, 550), (250, 550), (250, 200), (300, 200), (300, 600), (0, 600)]
    ],
    "scrap_pile_coords": [(150, 475, randint(0, 1)), (625, 450, randint(0, 1))],
    "scrap": []
}

room_1_2 = {
    "walls": [
        [(0, 0), (650, 0), (650, 50), (50, 50), (50, 550), (650, 550), (650, 600), (0, 600)],
        [
            (800, 0), (800, 600), (750, 600), (750, 450), (250, 450), (250, 350), (500, 350), (500, 400), (750, 400),
            (750, 200), (500, 200), (500, 250), (250, 250), (250, 150), (750, 150), (750, 0)
        ]
    ],
    "scrap_pile_coords": [(625, 300, randint(0, 1)), (375, 500, randint(0, 1))],
    "scrap": []
}

room_2_0 = {
    "walls": [
        [
            (0, 0), (0, 600), (400, 600), (400, 550), (300, 550), (300, 400), (250, 400), (250, 550), (50, 550),
            (50, 50), (250, 50), (250, 200), (300, 200), (300, 0)
        ],
        [
            (800, 0), (800, 600), (400, 600), (400, 550), (500, 550), (500, 400), (550, 400), (550, 550), (750, 550),
            (750, 50), (550, 50), (550, 200), (500, 200), (500, 0)
        ]
    ],
    "scrap_pile_coords": [
        (150, 125, randint(0, 1)),
        (150, 475, randint(0, 1)),
        (650, 475, randint(0, 1)),
        (650, 125, randint(0, 1))
    ],
    "scrap": []
}

room_2_1 = {
    "walls": [
        [
            (0, 0), (300, 0), (300, 50), (50, 50), (50, 550), (750, 550), (750, 450), (150, 450), (150, 400),
            (800, 400), (800, 600), (0, 600)
        ],
        [
            (500, 0), (800, 0), (800, 200), (750, 200), (750, 50), (650, 50), (650, 200), (200, 200), (200, 300),
            (150, 300), (150, 150), (500, 150)
        ]
    ],
    "scrap_pile_coords": [(700, 100, randint(0, 1)), (700, 500, randint(0, 1)), (250, 250, randint(0, 1))],
    "scrap": []
}

room_2_2 = {
    "walls": [
        [
            (0, 0), (0, 200), (50, 200), (50, 50), (300, 50), (300, 450), (350, 450), (350, 50), (600, 50), (600, 450),
            (650, 450), (650, 0)
        ],
        [
            (800, 0), (800, 600), (0, 600), (0, 400), (150, 400), (150, 150), (200, 150), (200, 550), (450, 550),
            (450, 150), (500, 150), (500, 550), (750, 550), (750, 0)
        ]
    ],
    "scrap_pile_coords": [(325, 500, randint(0, 1)), (475, 100, randint(0, 1))],
    "scrap": []
}

rooms = [
    [room_0_0, room_0_1, room_0_2],
    [room_1_0, room_1_1, room_1_2],
    [room_2_0, room_2_1, room_2_2]
]


def update_world():
    global scrap_i
    global world_i
    world_i = world_i + 1 if world_i < 41 else 1
    scrap_i = scrap_i + 1 if world_i % 10 == 0 else scrap_i

    if scrap_i == 9:
        scrap_i = 1

    return get_world()


def collide(obj1, obj2):
    mask1 = pygame.mask.from_surface(obj1)
    mask2 = pygame.mask.from_surface(obj2)

    return mask1.overlap_mask(mask2, (0, 0)).centroid() != (0, 0)


def should_score(world_nr, player_rect):
    room = rooms[world_nr[0]][world_nr[1]]
    score = 0
    for scrap in room["scrap"]:
        if player_rect.colliderect(scrap):
            score = score + 10

            for scrap_coord in room["scrap_pile_coords"]:
                if scrap.center == (scrap_coord[0], scrap_coord[1]):
                    room["scrap_pile_coords"].pop(room["scrap_pile_coords"].index(scrap_coord))

    return score


def get_next_room(room, x, y):
    if room == (0, 0) and x <= 0:
        return 1, 0
    elif room == (1, 0) and x <= 0:
        return 0, 0
    elif x >= 800:
        return room[0], room[1] + 1
    elif x <= 0:
        return room[0], room[1] - 1
    elif y >= 600:
        return room[0] + 1, room[1]
    elif y <= 0:
        return room[0] - 1, room[1]


def move_player_to_next_room(room, x, y):
    if room == (0, 0) and x <= 0:
        return 50, 50
    elif room == (1, 0) and x <= 0:
        return 150, 275
    elif x >= 800:
        return 10, y
    elif x <= 0:
        return 790, y
    elif y >= 600:
        return x, 10
    elif y <= 0:
        return x, 590


def get_surface(room):
    surface = Surface((800, 600))
    room["scrap"] = []

    for wall in room["walls"]:
        pygame.draw.polygon(surface, dark_green, wall)

    if "ellipses" in room:
        for ellipse in room["ellipses"]:
            transparent_beige = (beige[0], beige[1], beige[2], 0)
            pygame.draw.ellipse(surface, transparent_beige, ellipse)

    for scrap_center in room["scrap_pile_coords"]:
        if scrap_center[2] is not None and scrap_center[2] == 1:
            scrap = pygame.image.load(f"resources/mutter/mutter_{scrap_i}.png")
        else:
            scrap = pygame.image.load(f"resources/screw/screw_{scrap_i}.png")

        scrap.set_colorkey(beige)
        scrap_rect = scrap.get_rect()
        scrap_rect.center = (scrap_center[0], scrap_center[1])

        room["scrap"].append(scrap_rect)
        surface.blit(scrap, scrap_rect)

    return surface


def get_world():
    return [
        [get_surface(room_0_0), get_surface(room_0_1), get_surface(room_0_2)],
        [get_surface(room_1_0), get_surface(room_1_1), get_surface(room_1_2)],
        [get_surface(room_2_0), get_surface(room_2_1), get_surface(room_2_2)],
    ]
