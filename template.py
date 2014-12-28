'''
Widget animation
================

This is an example of an animation creation, and how you can apply it to a
widget.
'''

import kivy
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.atlas import Atlas
from kivy.graphics.instructions import Callback
from kivy.clock import Clock
import Stage
kivy.require('1.0.7')

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.core.image import Image
from kivy.graphics.instructions import Canvas

from functools import partial
from kivy.graphics import Color, Rectangle
# method 1 (preferred)
from kivy.base import EventLoop
EventLoop.ensure_window()

# method 2
from kivy.core.window import Window

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
