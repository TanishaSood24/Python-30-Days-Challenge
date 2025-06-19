from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup

class TempConverter(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(cols=2, padding=20, spacing=10)

        self.set_background_color()

        # Title label
        self.add_widget(Label(text='Temperature Converter', font_size=22, bold=True, color=(0, 0, 0, 1)))
        self.add_widget(Label(text='', size_hint_y=None))  # Empty cell for alignment

        # Input
        self.add_widget(Label(text='Enter Temperature:', color=(0.1, 0.1, 0.1, 1), font_size=18))
        self.temp_input = TextInput(multiline=False, background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))
        self.add_widget(self.temp_input)

        # From unit dropdown
        self.add_widget(Label(text='From Unit:', font_size=18, color=(0.1, 0.1, 0.1, 1)))
        self.from_unit = Spinner(text='Celsius', values=['Celsius', 'Fahrenheit', 'Kelvin'], background_color=(0.6, 0.8, 1, 1))
        self.add_widget(self.from_unit)

        # To unit dropdown
        self.add_widget(Label(text='To Unit:', font_size=18, color=(0.1, 0.1, 0.1, 1)))
        self.to_unit = Spinner(text='Fahrenheit', values=['Celsius', 'Fahrenheit', 'Kelvin'], background_color=(0.6, 0.8, 1, 1))
        self.add_widget(self.to_unit)

        # Convert button
        self.convert_button = Button(text='Convert', background_color=(0.2, 0.6, 1, 1), color=(1, 1, 1, 1), font_size=16)
        self.convert_button.bind(on_press=self.convert_temp)
        self.add_widget(self.convert_button)

        # Result label
        self.result_label = Label(text='Result:', font_size=18, color=(0.2, 0.2, 0.2, 1))
        self.add_widget(self.result_label)

    def set_background_color(self):
        from kivy.core.window import Window
        Window.clearcolor = (0.95, 0.95, 1, 1)  # light blue background

    def convert_temp(self, instance):
        try:
            value = float(self.temp_input.text)
            from_unit = self.from_unit.text
            to_unit = self.to_unit.text

            if from_unit == to_unit:
                result = value
            elif from_unit == 'Celsius':
                result = (value * 9/5 + 32) if to_unit == 'Fahrenheit' else (value + 273.15)
            elif from_unit == 'Fahrenheit':
                result = (value - 32) * 5/9 if to_unit == 'Celsius' else (value - 32) * 5/9 + 273.15
            elif from_unit == 'Kelvin':
                result = value - 273.15 if to_unit == 'Celsius' else (value - 273.15) * 9/5 + 32

            self.result_label.text = f'Result: {round(result, 2)} {to_unit}'
        except:
            popup = Popup(title='Error', content=Label(text='Please enter a valid number!'), size_hint=(0.6, 0.4))
            popup.open()

class TempConverterApp(App):
    def build(self):
        return TempConverter()

if __name__ == '__main__':
    TempConverterApp().run()


#& "C:\Users\DELL\AppData\Local\Programs\Python\Python313\python.exe" "D:\DOWNLOAD\PYTHON\Python30DaysChallenge\Day-23.py"
#in powershell