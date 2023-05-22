from manim import *
import numpy as np

class Graph(Scene):
    def construct(self):
        name = Text("When we define Taylor series at (a = 0) it becomes McLaurean Series").shift(UP*3).scale(.5)
        name.set_color_by_gradient(YELLOW, WHITE)
        name2 = Text("Notice we have").shift(LEFT*3).shift(UP*1).scale(.5)
        name2.set_color_by_gradient(YELLOW, WHITE)
        equation = MathTex(r"cosx , sinx", tex_to_color_map={"x": RED}).next_to(name2, RIGHT).scale(.7)
        name3 = Text("In Euler's formula").next_to(equation, RIGHT).scale(.5)
        name3.set_color_by_gradient(YELLOW, WHITE)
        name4 = Text("So we have to expand this according to McLaurean Series").shift(DOWN*.1).scale(.5)
        name4.set_color_by_gradient(YELLOW, WHITE)









        self.play(Create(name),runtime=3)
        self.play(Create(name2),runtime=3)
        self.play(Write(equation),runtime=5)
        self.play(Create(name3),runtime=4)
        self.play(Create(name4),runtime=4)
        self.wait(5)