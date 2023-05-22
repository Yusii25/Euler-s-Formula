from manim import *

class XeqA(Scene):
    def construct(self):
        
        name = Text("Notice that If we put (x = a) in (3), (4),(5) and (6) we get the value of Constant").shift(UP*3).scale(.6)
        name.set_color_by_gradient(PINK, YELLOW)
        
        
        
        
        equation = MathTex(r"f(a) = C_{0}1 + C_{1}(a-a)^{1} + C_{2}(a-a)^{2} + C_{3}(a-a)^{3} + C_{4}(a-a)^{4} +...........C_{n}(a-a)^{n}......(3)", tex_to_color_map={"x": RED}).scale(.6).to_edge(LEFT).shift(UP*2.5)
        equation2 = MathTex(r"f^{1}(a) = C_{1} + 2C_{2}(a-a)^{1} + 3C_{3}(a-a)^{2} + 4C_{4}(a-a)^{3} +.............(4)", tex_to_color_map={"x": RED}).scale(.6).to_edge(LEFT).shift(UP*2)
        equation3 = MathTex(r"f^{2}(a) = 0 + 2!C_{2} + 3!C_{3}(a-a)^{1} + 4.3C_{4}(a-a)^{2} +.............(5)", tex_to_color_map={"x": RED}).scale(.6).to_edge(LEFT).shift(UP*1.5)
        equation4 = MathTex(r"f^{3}(a) = 0 + 0 + 3!C_{3} + 4!C_{4}(a-a)^{1} + .............(6)", tex_to_color_map={"x": RED}).scale(.6).to_edge(LEFT).shift(UP*1)
    
        equation5 = MathTex(r"f(a) = C_{0} + 0 + 0 + 0+...").scale(.6).to_edge(LEFT).shift(UP*2.5)
        equation6 = MathTex(r"f^{1}(a) = C_{1} + 0 + 0 + 0+...").scale(.6).to_edge(LEFT).shift(UP*2)
        equation7 = MathTex(r"f^{2}(a) = 2!C_{2} +0 + 0 + 0+...").scale(.6).to_edge(LEFT).shift(UP*1.5)
        equation8 = MathTex(r"f^{3}(a) = 3!C_{3} + 0 + 0 + 0+...").scale(.6).to_edge(LEFT).shift(UP*1)
        
        equation9 = MathTex(r"C_{0} = f(a).............(7)").scale(.6).shift(RIGHT*3).shift(UP*2.5)
        equation10 = MathTex(r"C_{1} = f^{1}(a).............(8)").scale(.6).shift(RIGHT*3).shift(UP*2)
        equation11 = MathTex(r"C_{2} = \frac{f^{2}(a)}{2!}.............(9)").scale(.6).shift(RIGHT*3).shift(UP*1.4)
        equation12 = MathTex(r"C_{3} = \frac{f^{3}(a)}{3!}.............(10)").scale(.6).shift(RIGHT*3).shift(UP*.4)
        
        
        
        equation13 = MathTex(r"C_{n} = \frac{f^{n}(a)}{n!}.............(11)").scale(.7).shift(DOWN*.1)
        name2 = Text("Putting these value in equation (3)").shift(DOWN*1.2).scale(.7)
        name2.set_color_by_gradient(RED, YELLOW)
        equation14 = MathTex(r"f(x) = C_{0}1 + C_{1}(x-a)^{1} + C_{2}(x-a)^{2} + C_{3}(x-a)^{3} + C_{4}(x-a)^{4} +...........C_{n}(x-a)^{n}......(3)", tex_to_color_map={"x": RED}).scale(.6).shift(DOWN*2)
        equation15 = MathTex(r"f(x) = f(a) + f^{1}(a)(x-a) + \frac{f^{2}(a)}{2!}(x-a)^{2} + \frac{f^{3}(a)}{3!}(x-a)^{3} + ............ \frac{f^{n}(a)}{n!}(x-a)^{n}.........(11)").scale(.6).shift(DOWN*2)
        name3 = Text("That is Essentially the Taylor Series").shift(DOWN*3).scale(.7)
        name3.set_color_by_gradient(RED, BLUE)
        name4 = Text("(Formula for Expansion of a function)").shift(DOWN*3.5).scale(.4)
        name4.set_color_by_gradient(RED, PURE_GREEN)


        self.play(Write(name), runtime=3)
        self.play(Write(equation), runtime=5)
        self.play(FadeTransform(equation, equation5), runtime=5)
        self.play(Write(equation2), runtime=5)
        self.play(FadeTransform(equation2, equation6), runtime=5)
        self.play(Write(equation3), runtime=5)
        self.play(FadeTransform(equation3, equation7), runtime=5)
        self.play(Write(equation4), runtime=5)
        self.play(FadeTransform(equation4, equation8), runtime=5)
        self.play(Write(equation9), runtime=5)
        self.play(Write(equation10), runtime=5)
        self.play(Write(equation11), runtime=5)
        self.play(Write(equation12), runtime=5)
        self.play(Write(equation13), runtime=5)
        self.play(Write(name2), runtime=5)
        self.play(Write(equation14), runtime=5)
        self.play(FadeTransform(equation14, equation15), runtime=7)
        self.play(Write(name3), runtime=5)
        self.play(Write(name4), runtime=5)

        self.wait(5)