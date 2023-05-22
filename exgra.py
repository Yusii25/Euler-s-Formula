from manim import *
import numpy as np

class Graph(Scene):
    def construct(self):
        equation = MathTex(r"(y = e^{x})", tex_to_color_map={"x": RED}).shift(RIGHT*4).shift(UP*1).scale(1)
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
        graph = FunctionGraph(lambda x: np.exp(x), x_range=[-20, 20], color=YELLOW)
        self.play(Create(axes),runtime=5)
        self.play(Create(graph),runtime=5)
        self.play(Write(equation),runtime=5)
        self.wait(5)

if __name__ == "__main__":
    graph = Graph()
    graph.run()









