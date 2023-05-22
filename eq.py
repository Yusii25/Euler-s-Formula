from manim import *

class Intro(Scene):
    def construct(self):

        name = Text("Proof Of Euler's Theorem", t2c={"Euler's": MAROON}).shift(UP*2).scale(1.8)
        equation = MathTex(r"(e^{ix} = \cos x + i \sin x)", tex_to_color_map={"x": RED}).shift(UP*.7).scale(1.5)
        name2 = Tex("-Made By Yusii").shift(DOWN*1).shift(RIGHT*2.5).scale(1.2)
        
        self.play(Write(name), runtime=3)
        self.play(Write(equation), runtime=3)
        self.play(Write(name2), runtime=3)
        self.wait(3)
