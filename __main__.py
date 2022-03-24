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
CAPTION = "Robot Vs Rocks"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 70


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
    y = int(MAX_Y - 15)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    


    #Actor.get_velocity(10)
    #cast.set_position(position)

    # create the artifacts
    #with open(DATA_PATH) as file:
    #    data = file.read()
    #    messages = data.splitlines()

    for n in range(DEFAULT_ARTIFACTS):
        starsim = "*"
        text = random.randint(0,1)
        if text == 0:
            text = 'O'
        else:
            text = '*'
        

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(255, 255, b)
        
        star = Artifact()
        star.set_text(starsim)
        star.set_font_size(FONT_SIZE)
        star.set_color(color)
        star.set_position(position)
        star.set_message("points:")
        cast.add_actor("artifacts", star)


    for n in range(DEFAULT_ARTIFACTS):
        rocksim = "[]"
        #text = chr(random.randint(33, 126))
        #message = messages[n]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 100)
        g = random.randint(0, 100)
        b = random.randint(50, 200)
        color = Color(b, b, b)
        
        rock = Artifact()
        rock.set_text(rocksim)
        rock.set_font_size(FONT_SIZE)
        rock.set_color(color)
        rock.set_position(position)
        rock.set_message("points:")
        cast.add_actor("artifacts", rock)

        #Actor.get_velocity(10)
        #rock.set_position(Point(x, y))
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(text)
        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
