from manim import *
import numpy as np
class OpeningManimExample(Scene):
    def construct(self):
        
        name = Text("Now, Carefully notice the exapansion of ..").shift(UP*3).scale(.6)
        name.set_color_by_gradient(PURE_RED, PURE_GREEN)
        equation = MathTex(r"e^{x}").shift(UP*3).shift(RIGHT*3).scale(.4)

        self.play(Create(name),runtime=5)
        self.play(Write(equation),runtime=5)