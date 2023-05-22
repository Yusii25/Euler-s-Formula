from manim import *

class ScalarTimesVector(Scene):
    def construct(self):
        a_times_v = MathTex(r"a", "\\cdot", "b")

        a_times_v.shift(UP*2)

        self.play(Write(a_times_v))
        self.wait(5)
