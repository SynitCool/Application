from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

class WindowManager(ScreenManager):
    pass

class PlayWindow(Screen):
    turn = "X"
    def flip_player(self):
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"

        self.vertical_winner()
        self.diagonal_winner()
        self.columns_winner()
        self.draw()

    def vertical_winner(self):
        if (self.button_0.text == "X" and self.button_3.text == "X" and self.button_6.text == "X") or (self.button_0.text == "O" and self.button_3.text == "O" and self.button_6.text == "O"):
            self.parent.current = "winner_window"
            self.parent.transition.direction = "left"

            self.turn = "X"

            self.button_0.text = "None"
            self.button_0.disabled = False
            self.button_0.background_color = (1,1,1,1)


            self.button_1.text = "None"
            self.button_1.disabled = False
            self.button_1.background_color = (1,1,1,1)

            self.button_2.text = "None"
            self.button_2.disabled = False
            self.button_2.background_color = (1,1,1,1)

            self.button_3.text = "None"
            self.button_3.disabled = False
            self.button_3.background_color = (1,1,1,1)

            self.button_4.text = "None"
            self.button_4.disabled = False
            self.button_4.background_color = (1,1,1,1)

            self.button_5.text = "None"
            self.button_5.disabled = False
            self.button_5.background_color = (1, 1, 1, 1)

            self.button_6.text = "None"
            self.button_6.disabled = False
            self.button_6.background_color = (1, 1, 1, 1)

            self.button_7.text = "None"
            self.button_7.disabled = False
            self.button_7.background_color = (1, 1, 1, 1)

            self.button_8.text = "None"
            self.button_8.disabled = False
            self.button_8.background_color = (1, 1, 1, 1)
        if (self.button_1.text == "X" and self.button_4.text == "X" and self.button_7.text == "X") or (self.button_1.text == "O" and self.button_4.text == "O" and self.button_7.text == "O"):
            self.parent.current = "winner_window"
            self.parent.transition.direction = "left"

            self.turn = "X"

            self.button_0.text = "None"
            self.button_0.disabled = False
            self.button_0.background_color = (1, 1, 1, 1)

            self.button_1.text = "None"
            self.button_1.disabled = False
            self.button_1.background_color = (1, 1, 1, 1)

            self.button_2.text = "None"
            self.button_2.disabled = False
            self.button_2.background_color = (1, 1, 1, 1)

            self.button_3.text = "None"
            self.button_3.disabled = False
            self.button_3.background_color = (1, 1, 1, 1)

            self.button_4.text = "None"
            self.button_4.disabled = False
            self.button_4.background_color = (1, 1, 1, 1)

            self.button_5.text = "None"
            self.button_5.disabled = False
            self.button_5.background_color = (1, 1, 1, 1)

            self.button_6.text = "None"
            self.button_6.disabled = False
            self.button_6.background_color = (1, 1, 1, 1)

            self.button_7.text = "None"
            self.button_7.disabled = False
            self.button_7.background_color = (1, 1, 1, 1)

            self.button_8.text = "None"
            self.button_8.disabled = False
            self.button_8.background_color = (1, 1, 1, 1)
        elif (self.button_2.text == "X" and self.button_5.text == "X" and self.button_8.text == "X") or (self.button_2.text == "O" and self.button_5.text == "O" and self.button_8.text == "O"):
            self.parent.current = "winner_window"
            self.parent.transition.direction = "left"

            self.turn = "X"

            self.button_0.text = "None"
            self.button_0.disabled = False
            self.button_0.background_color = (1, 1, 1, 1)

            self.button_1.text = "None"
            self.button_1.disabled = False
            self.button_1.background_color = (1, 1, 1, 1)

            self.button_2.text = "None"
            self.button_2.disabled = False
            self.button_2.background_color = (1, 1, 1, 1)

            self.button_3.text = "None"
            self.button_3.disabled = False
            self.button_3.background_color = (1, 1, 1, 1)

            self.button_4.text = "None"
            self.button_4.disabled = False
            self.button_4.background_color = (1, 1, 1, 1)

            self.button_5.text = "None"
            self.button_5.disabled = False
            self.button_5.background_color = (1, 1, 1, 1)

            self.button_6.text = "None"
            self.button_6.disabled = False
            self.button_6.background_color = (1, 1, 1, 1)

            self.button_7.text = "None"
            self.button_7.disabled = False
            self.button_7.background_color = (1, 1, 1, 1)

            self.button_8.text = "None"
            self.button_8.disabled = False
            self.button_8.background_color = (1, 1, 1, 1)

    def diagonal_winner(self):
        if (self.button_0.text == "X" and self.button_1.text == "X" and self.button_2.text == "X") or (self.button_0.text == "O" and self.button_1.text == "O" and self.button_2.text == "O"):
            self.parent.current = "winner_window"
            self.parent.transition.direction = "left"

            self.turn = "X"

            self.button_0.text = "None"
            self.button_0.disabled = False
            self.button_0.background_color = (1, 1, 1, 1)

            self.button_1.text = "None"
            self.button_1.disabled = False
            self.button_1.background_color = (1, 1, 1, 1)

            self.button_2.text = "None"
            self.button_2.disabled = False
            self.button_2.background_color = (1, 1, 1, 1)

            self.button_3.text = "None"
            self.button_3.disabled = False
            self.button_3.background_color = (1, 1, 1, 1)

            self.button_4.text = "None"
            self.button_4.disabled = False
            self.button_4.background_color = (1, 1, 1, 1)

            self.button_5.text = "None"
            self.button_5.disabled = False
            self.button_5.background_color = (1, 1, 1, 1)

            self.button_6.text = "None"
            self.button_6.disabled = False
            self.button_6.background_color = (1, 1, 1, 1)

            self.button_7.text = "None"
            self.button_7.disabled = False
            self.button_7.background_color = (1, 1, 1, 1)

            self.button_8.text = "None"
            self.button_8.disabled = False
            self.button_8.background_color = (1, 1, 1, 1)
        elif (self.button_3.text == "X" and self.button_4.text == "X" and self.button_5.text == "X") or (self.button_3.text == "O" and self.button_4.text == "O" and self.button_5.text == "O"):
            self.parent.current = "winner_window"
            self.parent.transition.direction = "left"

            self.turn = "X"

            self.button_0.text = "None"
            self.button_0.disabled = False
            self.button_0.background_color = (1, 1, 1, 1)

            self.button_1.text = "None"
            self.button_1.disabled = False
            self.button_1.background_color = (1, 1, 1, 1)

            self.button_2.text = "None"
            self.button_2.disabled = False
            self.button_2.background_color = (1, 1, 1, 1)

            self.button_3.text = "None"
            self.button_3.disabled = False
            self.button_3.background_color = (1, 1, 1, 1)

            self.button_4.text = "None"
            self.button_4.disabled = False
            self.button_4.background_color = (1, 1, 1, 1)

            self.button_5.text = "None"
            self.button_5.disabled = False
            self.button_5.background_color = (1, 1, 1, 1)

            self.button_6.text = "None"
            self.button_6.disabled = False
            self.button_6.background_color = (1, 1, 1, 1)

            self.button_7.text = "None"
            self.button_7.disabled = False
            self.button_7.background_color = (1, 1, 1, 1)

            self.button_8.text = "None"
            self.button_8.disabled = False
            self.button_8.background_color = (1, 1, 1, 1)
        elif (self.button_6.text == "X" and self.button_7.text == "X" and self.button_8.text == "X") or (self.button_6.text == "O" and self.button_7.text == "O" and self.button_8.text == "O"):
            self.parent.current = "winner_window"
            self.parent.transition.direction = "left"

            self.turn = "X"

            self.button_0.text = "None"
            self.button_0.disabled = False
            self.button_0.background_color = (1, 1, 1, 1)

            self.button_1.text = "None"
            self.button_1.disabled = False
            self.button_1.background_color = (1, 1, 1, 1)

            self.button_2.text = "None"
            self.button_2.disabled = False
            self.button_2.background_color = (1, 1, 1, 1)

            self.button_3.text = "None"
            self.button_3.disabled = False
            self.button_3.background_color = (1, 1, 1, 1)

            self.button_4.text = "None"
            self.button_4.disabled = False
            self.button_4.background_color = (1, 1, 1, 1)

            self.button_5.text = "None"
            self.button_5.disabled = False
            self.button_5.background_color = (1, 1, 1, 1)

            self.button_6.text = "None"
            self.button_6.disabled = False
            self.button_6.background_color = (1, 1, 1, 1)

            self.button_7.text = "None"
            self.button_7.disabled = False
            self.button_7.background_color = (1, 1, 1, 1)

            self.button_8.text = "None"
            self.button_8.disabled = False
            self.button_8.background_color = (1, 1, 1, 1)

    def columns_winner(self):
        if (self.button_0.text == "X" and self.button_4.text == "X" and self.button_8.text == "X") or (self.button_0.text == "O" and self.button_4.text == "O" and self.button_8.text == "O"):
            self.parent.current = "winner_window"
            self.parent.transition.direction = "left"

            self.turn = "X"

            self.button_0.text = "None"
            self.button_0.disabled = False
            self.button_0.background_color = (1, 1, 1, 1)

            self.button_1.text = "None"
            self.button_1.disabled = False
            self.button_1.background_color = (1, 1, 1, 1)

            self.button_2.text = "None"
            self.button_2.disabled = False
            self.button_2.background_color = (1, 1, 1, 1)

            self.button_3.text = "None"
            self.button_3.disabled = False
            self.button_3.background_color = (1, 1, 1, 1)

            self.button_4.text = "None"
            self.button_4.disabled = False
            self.button_4.background_color = (1, 1, 1, 1)

            self.button_5.text = "None"
            self.button_5.disabled = False
            self.button_5.background_color = (1, 1, 1, 1)

            self.button_6.text = "None"
            self.button_6.disabled = False
            self.button_6.background_color = (1, 1, 1, 1)

            self.button_7.text = "None"
            self.button_7.disabled = False
            self.button_7.background_color = (1, 1, 1, 1)

            self.button_8.text = "None"
            self.button_8.disabled = False
            self.button_8.background_color = (1, 1, 1, 1)
        elif (self.button_2.text == "X" and self.button_4.text == "X" and self.button_6.text == "X") or (self.button_2.text == "O" and self.button_4.text == "O" and self.button_6.text == "O"):
            self.parent.current = "winner_window"
            self.parent.transition.direction = "left"

            self.turn = "X"

            self.button_0.text = "None"
            self.button_0.disabled = False
            self.button_0.background_color = (1, 1, 1, 1)

            self.button_1.text = "None"
            self.button_1.disabled = False
            self.button_1.background_color = (1, 1, 1, 1)

            self.button_2.text = "None"
            self.button_2.disabled = False
            self.button_2.background_color = (1, 1, 1, 1)

            self.button_3.text = "None"
            self.button_3.disabled = False
            self.button_3.background_color = (1, 1, 1, 1)

            self.button_4.text = "None"
            self.button_4.disabled = False
            self.button_4.background_color = (1, 1, 1, 1)

            self.button_5.text = "None"
            self.button_5.disabled = False
            self.button_5.background_color = (1, 1, 1, 1)

            self.button_6.text = "None"
            self.button_6.disabled = False
            self.button_6.background_color = (1, 1, 1, 1)

            self.button_7.text = "None"
            self.button_7.disabled = False
            self.button_7.background_color = (1, 1, 1, 1)

            self.button_8.text = "None"
            self.button_8.disabled = False
            self.button_8.background_color = (1, 1, 1, 1)

    def draw(self):
        if self.button_0.text != "None" and self.button_1.text != "None" and self.button_2.text != "None" and self.button_3.text != "None" and self.button_4.text != "None" and self.button_5.text != "None" and self.button_6.text != "None" and self.button_7.text != "None" and self.button_8.text != "None":
            self.parent.current = "winner_window"
            self.parent.transition.direction = "left"

            self.turn = "X"

            self.button_0.text = "None"
            self.button_0.disabled = False
            self.button_0.background_color = (1, 1, 1, 1)

            self.button_1.text = "None"
            self.button_1.disabled = False
            self.button_1.background_color = (1, 1, 1, 1)

            self.button_2.text = "None"
            self.button_2.disabled = False
            self.button_2.background_color = (1, 1, 1, 1)

            self.button_3.text = "None"
            self.button_3.disabled = False
            self.button_3.background_color = (1, 1, 1, 1)

            self.button_4.text = "None"
            self.button_4.disabled = False
            self.button_4.background_color = (1, 1, 1, 1)

            self.button_5.text = "None"
            self.button_5.disabled = False
            self.button_5.background_color = (1, 1, 1, 1)

            self.button_6.text = "None"
            self.button_6.disabled = False
            self.button_6.background_color = (1, 1, 1, 1)

            self.button_7.text = "None"
            self.button_7.disabled = False
            self.button_7.background_color = (1, 1, 1, 1)

            self.button_8.text = "None"
            self.button_8.disabled = False
            self.button_8.background_color = (1, 1, 1, 1)

class WinnerWindow(Screen):
    def back_to_playing(self):
        self.win_label.text = "END"
        self.parent.current = "play_window"
        self.parent.transition.direction = "right"

class TicTacToeApp(App):
    def build(self):
        Window.size = (400, 400)
        return Builder.load_file("TicTacToe_Design.kv")

if __name__ == "__main__":
    TicTacToeApp().run()