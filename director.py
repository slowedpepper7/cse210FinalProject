from game.casting.artifact import Artifact
from game.shared.point import Point
global v
v = 5
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
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        
        obstacles = cast.get_actors('obstacles')  
        artifacts = cast.get_actors('artifacts')
        first = cast.get_first_actor('obstacles')
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
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        obstacles = cast.get_actors("obstacles")
        first = cast.get_first_actor('obstacles')
        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        for obstacle in obstacles:
            obstacle.move_next(max_x, max_y)
        
        for obstacle in obstacles:
            if robot.get_position().equals(obstacle.get_position()):
                print('Touching!')
        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                print('touching')   
        
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
        
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
