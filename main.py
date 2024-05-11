from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import os
from kivy.core.audio import SoundLoader

class Mp3PlayerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.text_input = TextInput(text='', multiline=False)
        self.text_input.bind(on_text_validate=self.on_enter)
        self.layout.add_widget(self.text_input)
        return self.layout

    def on_enter(self, instance):
        number = instance.text
        path_to_files=  os.path.join(os.getcwd(),'sounds')
        files=os.listdir(path_to_files)
        for file in files:
            if file.startswith(number) and file.endswith('.mp3'):
                sound= SoundLoader.load(os.path.join(path_to_files, file))
                if sound:
                    sound.play()

if __name__ == '__main__':
    Mp3PlayerApp().run()