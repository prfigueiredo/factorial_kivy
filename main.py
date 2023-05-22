from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = (20, 20)

        # spacer widget
        spacer0 = Widget(size_hint=(0.03, 0.03))
        self.add_widget(spacer0)

        # image widget
        image = Image(source='image/calc.png')
        image.size_hint = (None, None)
        image.size = (200, 200)
        image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.add_widget(image)

        # spacer widget
        spacer1 = Widget(size_hint=(0.01, 0.01))
        self.add_widget(spacer1)

        # text field (input) widget
        self.text_input = TextInput(multiline=False, input_type='number')
        self.text_input.size_hint = (None, None)
        self.text_input.size = (350, 50)
        self.text_input.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.add_widget(self.text_input)

        # spacer widget
        spacer2 = Widget(size_hint=(0.01, 0.01))
        self.add_widget(spacer2)

        # button widget
        self.button = Button(text='Calculate', size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5})
        self.button.bind(on_press=self.calculate_factorial)
        self.add_widget(self.button)

    # Factorial function
    def calculate_factorial(self, instance):
        try:
            num = int(self.text_input.text)
            result = 1
            for i in range(1, num + 1):
                result *= i
            
            # Label with results
            label_result = Label(text=f'The factorial of {num} is: {result}',
                                    size_hint=(None, None),
                                    size=(400, 50),
                                    pos_hint={'center_x': 0.5})

            self.add_widget(label_result)
        except ValueError:
            print("Type a valid number, please:")

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
