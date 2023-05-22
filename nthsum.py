from manim import *

class NthSum(Scene):
    def construct(self):
        eq = MathTex(r"f(x) =\sum_{n=0}^{n} C_{n}(x-a)^{n}").shift(UP*3).scale(1.4)
        brace = Brace(eq[0], direction=DOWN)
        name = Text("Here,").shift(LEFT*4).shift(UP*.5).scale(.6)
        eq2 = MathTex(r"C_{n} = nth Constant").shift(LEFT*4).shift(DOWN*.1).scale(.6)
        name2 = Text("a = approximation at a certain point 'a'").shift(LEFT*2).shift(DOWN*.6).scale(.4)
        name3 = Text("n = nth power").shift(LEFT*3).shift(DOWN*1).scale(.4)
        text = brace.get_text("This is Generalised Form of the Summation").shift(DOWN*3).scale(1.4)
        text.set_color_by_gradient(PINK, YELLOW)
        
        
        
        
        self.play(Write(eq))
        self.play(Write(brace))
        self.play(Write(name))
        self.play(Write(eq2))
        self.play(Write(name2))
        self.play(Write(name3))
        self.play(Write(text))
        self.wait(3)