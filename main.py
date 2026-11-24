import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

MAX_NUMBER = 99999


class GuessGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=15, **kwargs)

        self.title = Label(
            text="Number Guessing Game",
            font_size="26sp",
            size_hint_y=None,
            height=60,
        )
        self.info = Label(
            text=f"I have selected a number between 1 and {MAX_NUMBER}.\nTry to guess it.",
            font_size="18sp",
            halign="center",
        )
        self.info.bind(size=lambda w, s: setattr(w, "text_size", s))

        self.input = TextInput(
            hint_text="Enter your guess",
            input_filter="int",
            multiline=False,
            font_size="22sp",
            size_hint_y=None,
            height=60,
        )
        self.input.bind(on_text_validate=self.check_guess)

        self.guess_btn = Button(
            text="Guess", font_size="20sp", size_hint_y=None, height=60
        )
        self.guess_btn.bind(on_release=self.check_guess)

        self.new_btn = Button(
            text="New Game", font_size="18sp", size_hint_y=None, height=50
        )
        self.new_btn.bind(on_release=self.new_game)

        self.result = Label(text="", font_size="20sp", halign="center")
        self.result.bind(size=lambda w, s: setattr(w, "text_size", s))

        for widget in (
            self.title,
            self.info,
            self.input,
            self.guess_btn,
            self.result,
            self.new_btn,
        ):
            self.add_widget(widget)

        self.new_game()

    def new_game(self, *args):
        self.number = random.randint(1, MAX_NUMBER)
        self.tries = 0
        self.game_over = False
        self.result.text = ""
        self.input.text = ""
        self.input.disabled = False
        self.guess_btn.disabled = False
        self.input.focus = True

    def check_guess(self, *args):
        if self.game_over:
            return
        text = self.input.text.strip()
        if not text:
            self.result.text = "Please enter a number."
            return

        guess = int(text)
        self.tries += 1

        if guess < self.number:
            self.result.text = f"{guess} is too low! Try again.\nAttempts: {self.tries}"
        elif guess > self.number:
            self.result.text = f"{guess} is too high! Try again.\nAttempts: {self.tries}"
        else:
            self.result.text = f"Correct! You guessed it in {self.tries} attempts."
            self.game_over = True
            self.input.disabled = True
            self.guess_btn.disabled = True

        self.input.text = ""
        if not self.game_over:
            self.input.focus = True


class GuessApp(App):
    def build(self):
        self.title = "Number Guessing Game"
        return GuessGame()


if __name__ == "__main__":
    GuessApp().run()
