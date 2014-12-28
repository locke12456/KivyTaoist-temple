from Role import Role
from Status import Status
from kivy.core.image import Image
from kivy.graphics.texture import Texture
class RoleZero(Role):
    size = [128,128]
    """description of class"""
    def __init__(self , *args, **kwargs):
        super(RoleZero, self).__init__(*args, **kwargs)
        self.Create("charter_malin.atlas")
        self._status = Status(self , self._atlas )
    def stand(self ,pos):
        _ani = self._status.stand()
        _ani.canvas = self.canvas
        _ani.pos = pos
        _ani.size = self.size
        _ani.anim_reset(True)
        _ani.anim_delay = 5.0/30.0

    def walk(self , pos):
        _ani = self._status.walk()
        _ani.canvas = self.canvas
        _ani.pos = pos
        _ani.size = self.size
        _ani.anim_delay = 5.0/30.0
        _ani.anim_reset(True)


