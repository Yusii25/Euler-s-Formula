from manim import *

class ExpNthSum(Scene):
    def construct(self):
        
        name = Text("Substituting the Value of 'n' in the Increasing order, We get").shift(UP*2).scale(.8)
        name.set_color_by_gradient(PINK, YELLOW)
        equation = MathTex(r"f(x) = C_{0}1 + C_{1}(x-a)^{1} + C_{2}(x-a)^{2} + C_{3}(x-a)^{3} + C_{4}(x-a)^{4} +...........C_{n}(x-a)^{n}......(3)", tex_to_color_map={"x": RED}).scale(.5).shift(LEFT*1).shift(UP*1)
        name2 = Text("Now Somehow we have to remove Constant 'C' from the equation").shift(UP*.1).scale(.5)
        name2.set_color_by_gradient(RED, YELLOW)
        name3 = Text("How do we get rid of a constant??by differentiating :)").shift(DOWN*.4).scale(.5)
        name3.set_color_by_gradient(GREEN, YELLOW)
        name4 = Text("So By Differentiating (3),").shift(LEFT*4).scale(.7).shift(DOWN*1)
        equation2 = MathTex(r"f^{1}(x) = C_{1} + 2C_{2}(x-a)^{1} + 3C_{3}(x-a)^{2} + 4C_{4}(x-a)^{3} +.............(4)", tex_to_color_map={"x": RED}).scale(.7).shift(LEFT*1).shift(DOWN*1.5)
        equation3 = MathTex(r"f^{2}(x) = 0 + 2!C_{2} + 3!C_{3}(x-a)^{1} + 4.3C_{4}(x-a)^{2} +.............(5)", tex_to_color_map={"x": RED}).scale(.7).shift(LEFT*1.5).shift(DOWN*2)
        equation4 = MathTex(r"f^{3}(x) = 0 + 3!C_{3} + 4!C_{4}(x-a)^{1} + .............(6)", tex_to_color_map={"x": RED}).scale(.7).shift(LEFT*2.2).shift(DOWN*2.5)
        name5 = Text(".................................").shift(DOWN*3).scale(.5)
        
        
        
        self.play(Write(name), runtime=3)
        self.play(Write(equation), runtime=5)
        self.play(Write(name2), runtime=3)
        self.play(Write(name3), runtime=3)
        self.play(Write(name4), runtime=3)
        self.play(Write(equation2), runtime=5)
        self.play(Write(equation3), runtime=5)
        self.play(Write(equation4), runtime=5)
        self.play(Write(name5), runtime=5)
        self.wait(5)
