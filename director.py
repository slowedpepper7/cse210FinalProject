from artifact import Artifact
from point import Point
from color import Color
import os
import random
global v
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
v = 5
global game_over
game_over = False
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        global game_over
        if game_over != True:
            robot = cast.get_first_actor("robots")
            velocity = self._keyboard_service.get_direction()
            robot.set_velocity(velocity)        
            obstacles = cast.get_actors('obstacles')  
            artifacts = cast.get_actors('artifacts')
            first = cast.get_first_actor('obstacles')
        else:
            robot = cast.get_first_actor("robots")
            robot.set_velocity(Point(0, 0))
        global v
        # obstacle_velocity = Point(v, 0)
        # for artifact in artifacts:
        #     if first.get_position().equals(artifact.get_position()):
        #         v = v * -1
        #         print(f'{v}')
        #         obstacle_velocity = Point(v, 0)
        #         for obstacle in obstacles:
        #             obstacle.set_velocity(obstacle_velocity)
        # for obstacle in obstacles:
        #     obstacle.set_velocity(obstacle_velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        global v
        global game_over
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        obstacles = cast.get_actors("obstacles")
        first = cast.get_first_actor('obstacles')
        flags = cast.get_actors("flag")
        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        win = 1

        for obstacle in obstacles:
            obstacle.move_next(max_x, max_y)
        
        for flag in flags:
            if robot.get_position().equals(flag.get_position()):
                game_over = True
                win = 2
        
        for obstacle in obstacles:
            if robot.get_position().equals(obstacle.get_position()):
                game_over = True
        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                game_over = True  
        if game_over == False:
            for artifact in artifacts:
                    if first.get_position().equals(artifact.get_position()):
                        v = v * -1

                        obstacle_velocity = Point(v, 0)
                        for obstacle in obstacles:
                            obstacle.set_velocity(obstacle_velocity)
                    else: 
                        obstacle_velocity = Point(v, 0)
                        for obstacle in obstacles:
                            obstacle.set_velocity(obstacle_velocity)
        else:
            for obstacle in obstacles:
                obstacle.set_velocity(Point(0, 0))
           
        if game_over == True:
            robot = cast.get_first_actor("robots")
            artifacts = cast.get_actors("artifacts")
            obstacles = cast.get_actors("obstacles")
            first = cast.get_first_actor('obstacles')
            flags = cast.get_actors("flag")
            banner = cast.get_first_actor("banners")
            
            x = 20
            y = 20
            position = Point(x, y)
            if win == 1:
                    text = "GAME OVER, YOU LOSE!"
                    x = 8
                    y = 20
                    position = Point(x, y)
                    position = position.scale(CELL_SIZE)
                    r = 255
                    g = 255
                    b = 255
                    color = Color(r, g, b)
                    artifact = Artifact()
                    artifact.set_text(text)
                    artifact.set_font_size(60)
                    artifact.set_color(color)
                    artifact.set_position(position)
                    # artifact.set_message(message)
                    cast.add_actor("artifacts", artifact)
            else: 
                text = "CONGRADULATIONS YOU WIN!"
                x = 8
                y = 20
                position = Point(x, y)
                position = position.scale(CELL_SIZE)
                r = 255
                g = 15
                b = 15
                color = Color(r, g, b)
                artifact = Artifact()
                artifact.set_text(text)
                artifact.set_font_size(40)
                artifact.set_color(color)
                artifact.set_position(position)
                # artifact.set_message(message)
                cast.add_actor("artifacts", artifact)
            
        
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    def game_over(self):
        return self.game_over
