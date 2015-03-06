
from kivy.app import App
from Sprite import *
class TestApp(App):
    wid = Sprite()
    index = 1
    size =[]
    def my_callback(self, instr):
        self.wid.draw()
    def build(self):
        sp2 = Sprite()
        
        sp3 = Sprite()
        r = GraphicStructure(1.,0.,0.,0.5,[0,0],[128,128])
        g = GraphicStructure(0.,1.,0.,1,[0,0],[128,128])
        b = GraphicStructure(0,0,1,0.25,[0,0],[128,128])
        self.wid.add_graphic(g)
        sp2.pos=[20,20]
        sp2.add_graphic(r)
        sp3.pos=[20,20]
        sp3.add_graphic(b)
        self.wid.add_widget(sp2,1)
        sp2.add_widget(sp3,1)
        self.wid.pos = [128,128]
        self.wid.draw()
        return self.wid
    def on_event(self, obj):
        print("Typical event from", obj)

if __name__ == '__main__':
    TestApp().run()