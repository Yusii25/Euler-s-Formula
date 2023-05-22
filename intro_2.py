from manim import *
import numpy as np

class Graph(Scene):
    def construct(self):
        name = Text("To prove Euler's Theorem we gotta know about Taylor Series first...").shift(UP*3).scale(.5)
        name.set_color_by_gradient(YELLOW, WHITE)
        name2 = Text("We all know about the expansion of").shift(UP*2.5).scale(.5)
        name2.set_color_by_gradient(YELLOW, WHITE)
        equation = MathTex(r"e^{x}", tex_to_color_map={"x": RED}).next_to(name2, RIGHT).scale(.7)
        equation2 = MathTex(r"e^{x} = 1 + x +\frac{1}{2!}(x)^{2} +\frac{1}{3!}(x)^{3}+\frac{1}{4!}(x)^{4}+\frac{1}{5!}(x)^{5}+ \frac{1}{6!}x^{6}.....", tex_to_color_map={"x": RED}).shift(UP*1.8).scale(.7)
        name3 = Text("Taylor Series is nothing but summation of bunch of functions.").shift(UP*.6).scale(.6)
        name3.set_color_by_gradient(YELLOW, WHITE)
        name4 = Text("Each Term we add to the equation it gets closer to the actual equation..").shift(DOWN*.6).scale(.6)
        name4.set_color_by_gradient(YELLOW, WHITE)









        self.play(Create(name),runtime=3)
        self.play(Create(name2),runtime=3)
        self.play(Write(equation),runtime=5)
        self.play(Write(equation2),runtime=5)
        self.play(Create(name3),runtime=4)
        self.play(Create(name4),runtime=4)
        self.wait(5)