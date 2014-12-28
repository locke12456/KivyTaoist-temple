
from kivy.core.window import Window
class Input(object):
    #_keyboard = {}
    _event_map = {}
    def _on_key_down(self, keyboard, keycode, text, modifiers):
        print keycode
        result = self._event_map.has_key(keycode[1])
        if result :
            callbak = self._event_map[keycode[1]]
            callbak(keycode)
        return True
    def _on_key_up(self,text , keycode):
        print keycode
        return True
    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    """description of class"""
    def __init__(self, *args, **kwargs):
        self._keyboard =  Window.request_keyboard( self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_up=self._on_key_up)
        self._keyboard.bind(on_key_down=self._on_key_down)
        return super(Input, self).__init__(*args, **kwargs)
    def Register( self , key , callback ):
        self._event_map[key] = callback 


