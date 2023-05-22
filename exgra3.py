from manim import *
import numpy as np

class Graph3(Scene):
    def construct(self):
        equation = MathTex(r"(y = 1 + x)", tex_to_color_map={"x": RED}).shift(RIGHT*4).shift(UP*2).scale(1)
        axes = Axes(
            x_range=[-20, 20, 1],
            y_range=[0, 5, .5],
            x_length=20,
            y_length=5,
            axis_config={
                "color": WHITE,
                "stroke_width": 1,
                "include_tip": True,
            },
            x_axis_config={
                "numbers_with_elongated_ticks": np.arange(-20, 20, 1),
            },
            y_axis_config={
                "numbers_with_elongated_ticks": np.arange(0, 5, 1),
            },
        )
        graph = FunctionGraph(lambda x: 1 + x, x_range=[-20, 20], color=BLUE)
        graph3 = FunctionGraph(lambda x: np.exp(x), x_range=[-20, 20], color=YELLOW)
        self.add(axes)
        self.add(graph3)
        self.play(Create(graph),runtime=5)
        self.play(Write(equation),runtime=5)
        self.wait(5)

if __name__ == "__main__":
    graph = Graph()
    graph.run()
