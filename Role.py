from kivy.atlas import Atlas
from kivy.uix.widget import Widget
class Role(Widget):
    """description of class"""
    def __init__(self, *args, **kwargs):
        super(Role, self).__init__(*args, **kwargs)
    def Create(self , filename):
        self._atlas = Atlas(filename)
    def Texture(self , key ):
        return self._atlas.textures[key]
    def Keys(self):
        return self._atlas.textures.keys()


