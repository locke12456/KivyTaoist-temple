'''
Widget animation
================

This is an example of an animation creation, and how you can apply it to a
widget.
'''
from kivy.core.audio import SoundLoader
import Stage
from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    wid = Stage.Stage()
    index = 1
    size =[]
    def animate(self, instance):
       sound = SoundLoader.load('../../res/bgm/bgm_converted.ogg')
       if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

    def my_callback(self, instr):
        self.wid.draw()
        #print(index)
    def build(self):
        # create a button, and  attach animate() method as a on_press handler
        button = Button(size_hint=(None, None), text='plop', on_press=self.animate)
        self.wid.bind(on_update=lambda x: self.on_event(None))
        self.wid.draw()
        #wid.cb.ask_update()
        #Clock.schedule_interval(self.my_callback, 0.25)
        return self.wid
    def on_event(self, obj):
        print("Typical event from", obj)

if __name__ == '__main__':
    TestApp().run()
