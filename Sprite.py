from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
class GraphicStructure(object):
    r= 0.
    g= 0.
    b= 0.
    a= 1.
    pos = [0.,0.]
    size = [0.,0.]
    def __init__( self , r , g , b , a , position , size , *args , **kwargs ):
        super(GraphicStructure, self).__init__(*args, **kwargs)
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.pos = position
        self.size = size


class Sprite(Widget):
    """description of class"""
    graph_object_list=None
    def __init__(self, **kwargs):
        super(Sprite, self).__init__(**kwargs)
    def add_graphic(self,graph_object):
        self.graph_object_list=graph_object
    def __set_canvas_and_position(self, canvas, position):
        if canvas is None:
            canvas = self.canvas
        if position is not None:
            position = [position[0]+self.pos[0] , position[1]+self.pos[1]]
        else:
            position = self.pos
        return canvas, position

    def __draw_children(self, canvas, position):
        for child in self.children:
            child.draw( canvas , position )

    def draw(self , canvas = None , position = None):
        canvas, position = self.__set_canvas_and_position(canvas, position)
        self._draw(self.graph_object_list , canvas , position)
        self.__draw_children(canvas, position)
    def _draw(self , graph_object , canvas , position):
        
        with canvas:
            if self.parent is None: 
                canvas.clear()
            Color( graph_object.r , graph_object.g , graph_object.b , graph_object.a )
            pos = [position[0] + graph_object.pos[0] ,position[1] + graph_object.pos[1]]
            print pos
            #Rectangle( pos= [self.pos[0] + graph_object.pos[0] , self.pos[1] + graph_object.pos[1]] , size= graph_object.size )
            Rectangle( pos= pos , size= graph_object.size )
            #Rectangle( pos= graph_object.pos , size= graph_object.size )
