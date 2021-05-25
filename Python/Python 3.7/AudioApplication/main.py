from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from Database import DataBase

db = DataBase("data.txt")

class WindowManager(ScreenManager):
    data_audio = db.data

    current_name = ""
    audio_volume = 0

    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        Clock.schedule_once(self.to_main_window, 2)
        print(self.data_audio)

        self.rv = self.main_rv
        self.sound_playing = []
        self.rv.data = [{'idx': x, 'text': x, 'PATH':self.data_audio[x][0]}
                        for x in self.data_audio]

        self.slider_layout = GridLayout()
        self.slider_layout.cols = 1

        self.volume_label = Label()
        self.volume_label.text = "Volume"
        self.slider_layout.add_widget(self.volume_label)

        self.volume_slider = Slider()
        self.volume_slider.min = 0.0
        self.volume_slider.max = 1.0
        self.volume_slider.bind(value=self.on_volume_change)
        self.slider_layout.add_widget(self.volume_slider)

        self.volume_value = Label()
        self.volume_value.text = "0"
        self.slider_layout.add_widget(self.volume_value)

        self.audio_layout.add_widget(self.slider_layout)

    def to_main_window(self, *args):
        self.current = 'main_window'
        self.transition.direction = "up"

    def to_info_window(self, text, PATH):
        self.current_name = text
        self.sound_playing.append(SoundLoader().load(PATH))
        self.audio_volume = self.sound_playing[0].volume
        self.volume_value.text = str(self.sound_playing[0].volume)
        self.volume_slider.value = self.sound_playing[0].volume
        self.check_audio.text = text
        self.current = "info_window"

    def to_add_data_window(self):
        self.current = "add_data_window"

    def play_audio(self):
        if len(self.sound_playing) >= 2 and (self.sound_playing[0].state == "play" or self.sound_playing[0].state == "stop"):
            self.sound_playing[0].stop()
            self.sound_playing.pop(0)
            self.sound_playing[0].play()
        else:
            self.sound_playing[0].play()

    def stop_audio(self):
        self.sound_playing[0].stop()

    def loop_audio(self):
        self.sound_playing[0].loop = True

    def not_loop_audio(self):
        self.sound_playing[0].loop = False

    def on_volume_change(self, instance, value):
        self.sound_playing[0].volume = value
        self.volume_value.text = str(round(value, 2))

    def add_audio(self, name, path):
        db.add_data(name, path)
        self.reset_add_data_window()
        self.to_main_window()

    def reset_add_data_window(self):
        self.add_name.text = ""
        self.add_path.text = ""

class SplashWindow(Screen):
    pass

class MainWindow(Screen):
    pass

class InfoWindow(Screen):
    pass

class AddDataWindow(Screen):
    pass

class MainApp(App):
    Window.size = 300, 450
    def build(self):
        return WindowManager()

if __name__ == "__main__":
    MainApp().run()