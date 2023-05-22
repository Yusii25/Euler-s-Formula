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
        
        def func2(x):
            return x+1+x**2/2+x**3/6+x**4/24

        # Plot the function using the plot method
        graph = ax.plot(func, color=BLUE,).scale(1).shift(DOWN*3)
        graph2 = ax.plot(func2, color=RED,).scale(1).shift(DOWN*3)
        ax.scale(1).shift(DOWN*3)
        equation = MathTex(r"y = 1 + x +\frac{1}{2!}(x)^{2} +\frac{1}{3!}(x)^{3}+\frac{1}{4!}(x)^{4}", tex_to_color_map={"x": RED}).shift(RIGHT*4).shift(DOWN*1).scale(.5)

        

        # Add the axes and the graph to the scene
        self.add(ax)
        self.add(graph)
        self.play(Create(graph2),runtime=5)
        self.play(Write(equation),runtime=5)
        self.wait(5)