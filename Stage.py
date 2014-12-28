from kivy.uix.widget import Widget
import Input
from RoleZero import RoleZero
class Stage(Widget):
    _input = Input.Input()
    _player = RoleZero()
    """description of class"""
    def __init__(self, *args, **kwargs):
        super(Stage, self).__init__(*args, **kwargs)
        self.add_widget(self._player)
    def draw(self):
        self._player.walk(self.pos)