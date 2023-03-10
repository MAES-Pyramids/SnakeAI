from util.point import Point
from util.constants import CONSTANTS
from util.directions import Direction
import pygame


class Segment(pygame.sprite.Sprite):
    def __init__(self, position: Point) -> None:
        super().__init__()

        self.image = pygame.transform.smoothscale(pygame.image.load(
            r"assets\images\segment.png").convert_alpha(), CONSTANTS.PIXEL_SIZE)
        self.rect = self.image.get_rect()
        self.position = position


class Snake:
    def __init__(self) -> None:
        self.body = [Segment(Point.get_random_point())]
        self.head = self.body[-1]
        self.direction = Direction.RIGHT

    def length(self) -> int:
        return len(self.body)

    def change_direction(self, new_direction: Direction) -> None:
        if new_direction + self.direction != Point(0, 0):
            self.direction = new_direction

    def move(self) -> None:
        new_segment = Segment(self.head.position+self.direction)
        self.head = new_segment

        self.body.append(new_segment)
        self.body = self.body[1:]

    def grow(self) -> None:
        new_segment = self.body[0]
        self.body.insert(0, new_segment)
    

    def collides_with(self, other: object) -> bool:
        return self.head.rect.colliderect(other)
