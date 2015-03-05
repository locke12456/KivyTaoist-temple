from Role import Role
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
from kivy.graphics.instructions import VertexInstruction
class VertexCalc(VertexInstruction):
    def __init__(self, **args):
        super(VertexCalc, self).__init__(**args)
        tx = self.tex_coords
class State(Image):
    index =0
    atlas = {}
    size = []
    _image_tex_cache = [None,None,None,None,None,None,None]
    pos= []
    _filp = False
    @property 
    def Filp(self):
        return _filp
    @Filp.setter
    def Filp(self,value):
        self._filp = value

    def __init__(self,atlas,list, *args, **kwargs):
        super(State, self).__init__(atlas[list[0]],*args, **kwargs)
        self._image = self
        self.atlas = atlas
        self.textures =  [atlas[s] for s in list]
        self.anim_reset(False)
        self.on_texture = self.play
        self._anim_available = True
    def _need_filp(self):
        if self._filp is not True:
            return None
        if self._image_tex_cache[self.index] is not None:
            return self._image_tex_cache[self.index]
        r = VertexCalc(texture=self.texture)
        tex = r.tex_coords
        left = tex[0]
        right = tex[2]
        tc = [right,tex[1],left,tex[3],left,tex[5],right,tex[7]]
        self._image_tex_cache[self.index] = tc
        return tc

    def _draw(self, tc):
        if tc is not None:
            r = Rectangle(texture=self.texture, pos=self.pos, size=self.texture.size,tex_coords=tc)
        else:
            r = Rectangle(texture=self.texture, pos=self.pos, size=self.texture.size)
    def play(self):
        with self.canvas:
            self.canvas.clear()
            #self.pos[0] += 2
            self.index = self.anim_index
            tc = self._need_filp()
            self._draw(tc)
            

class Status(object):
    """description of class"""
    _status = {}
    def __init__(self, role , atlas,*args, **kwargs):
        super(Status, self).__init__(*args, **kwargs)
        self._status["stand"] =  State(atlas, self._parse( role , "stand") )
        self._status["walk"] =  State(atlas, self._parse( role , "walk") )

    def _parse(self, role , state ):
        keys = role.Keys()
        matching = [s for s in keys if state in s]
        return sorted(matching)
    @property
    def stand(self):
        return self._status["stand"]
    @property
    def walk(self):
        return self._status["walk"]
    