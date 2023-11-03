from kivy.app import App
from kivy.core.window import Window 
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from datetime import datetime
from time import time, strftime



class show(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_start()

    def update_time(self):
        self.ids.time.text = strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)





class ClockApp(App):
    sw_second = 0
    
    def update(self, nap):
        self.sw_second += nap
        
    def build(self):
        return show()
    

if __name__== '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    ClockApp().run()