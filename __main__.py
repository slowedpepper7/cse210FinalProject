import os
import random

from actor import Actor
from artifact import Artifact
from cast import Cast

from director import Director

from keyboard_service import KeyboardService
from video_service import VideoService

from color import Color
from point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Robot Finds Kitten"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 60

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(15, 555)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    # create the artifacts
    # with open(DATA_PATH) as file:
    #     data = file.read()
    #     messages = data.splitlines()

    for n in range(10):
        text = "O"
        # message = messages[n]

        x = n
        y = 35
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    
    for n in range(36):
        text = "O"
        # message = messages[n]

        x = 9
        y = n
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("artifacts", artifact)

    for n in range(36):
        text = "O"
        # message = messages[n]

        x = 25
        y = n
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    for n in range(36):
        text = "O"
        # message = messages[n]

        x = 40
        y = n + 5
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    
    for n in range(36):
        text = "O"
        # message = messages[n]

        x = 40 + n
        y = 5
        if x > 45:
            x = x - 5
            y = 10
        if x > 45:
            x = x - 5
            y = 15
        if x > 45:
            x = x - 5
            y = 20
        if x > 45:
            x = x - 5
            y = 25
        if x > 45:
            x = x - 5
            y = 30
        if x > 45:
            x = x - 5
            y = 35
        if x > 45:
            x = x - 5
            y = 50
        if x > 45:
            x = x - 5
            y = 55
        
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    
        for n in range(36):
            text = "O"
            # message = messages[n]

            x = 50
            y = n
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)

            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            # artifact.set_message(message)
            cast.add_actor("artifacts", artifact)
    for n in range(40):
        text = "O"
        # message = messages[n]

        x = random.randint(15, 24)
        y = n + 6
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(50, 255)
        g = random.randint(50, 255)
        b = random.randint(50, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    
    for n in range(15):
        text = "O"
        # message = messages[n]

        x = n
        y = 38
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("artifacts", artifact)

    for n in range(33):
        text = "O"
        # message = messages[n]

        x = 14
        y = n + 5
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    
#Coding for the obstacles that move back and forth
    for n in range(8):
        text = "O"
        # message = messages[n]

        x = 10
        y = 5 + (n * 4)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("obstacles", artifact)
    
    for n in range(8):
        text = "O"
        # message = messages[n]

        x = 26
        y = 5 + (n * 4)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("obstacles", artifact)

    for n in range(8):
        text = "O"
        # message = messages[n]

        x = 29
        y = 7 + (n * 4)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("obstacles", artifact)
    
    for n in range(8):
        text = "O"
        # message = messages[n]

        x = 32
        y = 10 + (n * 4)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("obstacles", artifact)

    for n in range(8):
        text = "O"
        # message = messages[n]

        x = 35
        y = 7 + (n * 4)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("obstacles", artifact)

    for n in range(31):
        text = "O"
        # message = messages[n]

        x = 46
        y = n + 5
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("obstacles", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
