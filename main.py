from kivy.core.audio import SoundLoader
from kivy.app import App

import Stage

class TestApp(App):
    wid = Stage.Stage()
    index = 1
    size =[]
    def my_callback(self, instr):
        self.wid.draw()
        #print(index)
    def build(self):
        #self.wid.bind(on_update=lambda x: self.on_event(None))
        self.wid.draw()
        return self.wid
    def on_event(self, obj):
        print("Typical event from", obj)

if __name__ == '__main__':
    TestApp().run()