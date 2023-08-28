from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex


class CalculatorApp(App):

    def build(self):
        self.operators = ['+', '-', '/', '*', '%']
        self.last_button_pressed = None
        self.last_was_operator = None

        self.result = TextInput(halign='right', readonly=True, font_size=32)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result)

        buttons = [
            ['AC', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '=']
        ]

        for row in buttons:
            h_layout = BoxLayout()
          
            for button_text in row:
                btn = Button(
                    text=button_text,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    background_color=get_color_from_hex('#191e1f'),
                    color=get_color_from_hex('#f57a07'),
                    font_size=32,
                    bold=True,

                )
                btn.bind(on_release=self.on_button_press)
                h_layout.add_widget(btn)
            layout.add_widget(h_layout)


        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'AC':
            self.clear(instance)
        elif button_text == '⌫':
            self.on_backspace(instance)
        elif button_text == '=':
            self.on_solution(instance)
        elif button_text == '%':
            self.percent(instance)
        else:
            new_text = current + button_text
            self.result.text = new_text

        self.last_button_pressed = instance
        self.last_was_operator = button_text in self.operators

    def clear(self, instance):
        self.result.text = ''

    def percent(self,instance):
        try:
            value=eval(self.result.text)
            percentage=value/100
            self.result.text=str(percentage)
        except:
            self.result.text='Error'


    def on_backspace(self, instance):
        current = self.result.text
        if current:
            new_text = current[:-1]
            self.result.text = new_text

    def on_solution(self, instance):
        try:
            solution = str(eval(self.result.text))
            self.result.text = solution
        except:
            self.result.text = 'Error'

if __name__ == '__main__':
    app = CalculatorApp()
    app.run()