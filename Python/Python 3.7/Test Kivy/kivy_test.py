import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
VideoPlayer:
    source: 'test_video.mp4'
''')

class TestApp(App):
    def build(self):
        return root

if __name__ == '__main__':
    TestApp().run()