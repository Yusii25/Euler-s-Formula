from manim import *

class Parabola(Scene):
    def construct(self):
        # Create an Axes object
        ax = Axes(
            x_range=[-6, 6, 1], # The range of x values
            y_range=[-7, 7, 1], # The range of y values
            x_length=13, # The length of the x-axis
            y_length=13, # The length of the y-axis
            axis_config={"include_numbers": True},
        )
        # Create a function to plot
        def func(x):
            return np.exp(x)

        # Plot the function using the plot method
        graph = ax.plot(func, color=BLUE,).scale(1).shift(DOWN*3)
        ax.scale(1).shift(DOWN*3)
        equation = MathTex(r"(y = e^{x})", tex_to_color_map={"x": RED}).shift(RIGHT*4).shift(DOWN*2).scale(1)
        

        # Add the axes and the graph to the scene
        self.play(Create(ax),runtime=5)
        self.play(Create(graph),runtime=5)
        self.play(Write(equation),runtime=5)
        self.wait(5)