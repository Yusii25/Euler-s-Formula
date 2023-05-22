
from manim import *
import numpy as np
class OpeningManimExample(Scene):
    def construct(self):
        
        name = Text("If we expand 'cosx' According to Taylor's Theorem..").shift(UP*3).scale(.6)
        name.set_color_by_gradient(PURE_RED, WHITE)
        linear_transform_words = MathTex(r"cosx = f(a) + f^{1}(a)(x-a) + \frac{f^{2}(a)}{2!}(x-a)^{2} + \frac{f^{3}(a)}{3!}(x-a)^{3} + \frac{f^{4}(a)}{4!}(x-a)^{4} + \frac{f^{5}(a)}{4!}(x-a)^{5} + \frac{f^{6}(a)}{6!}(x-a)^{6} + \frac{f^{7}(a)}{7!}(x-a)^{7}+...").shift(UP*1.5)
        name2 = Text("In Mclaurin series, (a = 0), the equation will be..").shift(UP*.5).scale(.6)
        name2.set_color_by_gradient(PURE_RED, WHITE)
        linear_transform_words.scale(.4)
        
        self.play(Create(name),runtime=5)
        self.play(Write(linear_transform_words),runtime=5)
        self.play(Create(name2),runtime=5)
        self.play(FadeOut(name2),runtime=5)
        
        complex_map_words = MathTex(r"cosx = f(0) + f^{1}(0)(x-0) + \frac{f^{2}(0)}{2!}(x-0)^{2} + \frac{f^{3}(0)}{3!}(x-0)^{3} + \frac{f^{4}(0)}{4!}(x-0)^{4} + \frac{f^{5}(0)}{5!}(x-0)^{5} + \frac{f^{6}(0)}{6!}(x-0)^{6} + \frac{f^{7}(0)}{7!}(x-0)^{7}+...").shift(UP*1.5)
        complex_map_words2 = MathTex(r"cosx = f(0) + f^{1}(0)(x) + \frac{f^{2}(0)}{2!}x^{2} + \frac{f^{3}(0)}{3!}x^{3} + \frac{f^{4}(0)}{4!}x^{4} + \frac{f^{5}(0)}{5!}x^{5} + \frac{f^{6}(0)}{6!}x^{6} + \frac{f^{7}(0)}{7!}x^{7}+...").shift(UP*1.5)
        complex_map_words.scale(.4)
        complex_map_words2.scale(.5)
        name3 = Text("...................(12)").shift(RIGHT*4).shift(UP*1).scale(.4)
        name4 = Text("Now let's say,").shift(LEFT*4).scale(.4)
        equation0= MathTex(r"f(x) = cosx").shift(LEFT*2.3).scale(.5)
        equation1 = MathTex(r"f^{1}(x) = -sinx").shift(LEFT*3.5).shift(DOWN*.5).scale(.5)
        equation2 = MathTex(r"f^{2}(x) = -cosx").shift(LEFT*3.5).shift(DOWN*.9).scale(.5)
        equation3 = MathTex(r"f^{3}(x) =  sinx").shift(LEFT*3.5).shift(DOWN*1.3).scale(.5)
        equation4 = MathTex(r"f^{4}(x) =  cosx").shift(LEFT*3.5).shift(DOWN*1.7).scale(.5)
        equation5 = MathTex(r"f^{5}(x) = -sinx").shift(LEFT*3.5).shift(DOWN*2.1).scale(.5)
        equation6 = MathTex(r"f^{6}(x) = -cosx").shift(LEFT*3.5).shift(DOWN*2.5).scale(.5)
        equation7 = MathTex(r"f(0) = 1").shift(RIGHT*3.5).shift(DOWN*.2).scale(.5)
        equation8 = MathTex(r"f^{1}(0) = 0").shift(RIGHT*3.5).shift(DOWN*.5).scale(.5)
        equation9 = MathTex(r"f^{2}(0) = -1").shift(RIGHT*3.5).shift(DOWN*.9).scale(.5)
        equation10 = MathTex(r"f^{3}(0) = 0").shift(RIGHT*3.5).shift(DOWN*1.3).scale(.5)
        equation11 = MathTex(r"f^{4}(0) = 1").shift(RIGHT*3.5).shift(DOWN*1.7).scale(.5)
        equation12 = MathTex(r"f^{5}(0) = 0").shift(RIGHT*3.5).shift(DOWN*2.1).scale(.5)
        equation13 = MathTex(r"f^{6}(0) = -1").shift(RIGHT*3.5).shift(DOWN*2.5).scale(.5)
        name5 = Text("Putting these value in (12)").shift(DOWN*2.7).scale(.4)
        equation14 = MathTex(r"cosx = 1 + (0)x + \frac{(-1)}{2!}x^{2} + \frac{0}{3!}x^{3} + \frac{1}{4!}x^{4} + \frac{0}{5!}x^{5} + \frac{(-1)}{6!}x^{6} + \frac{0}{7!}x^{7}+...").shift(DOWN*3.3).scale(.4)
        equation15 = MathTex(r"cosx = 1 - \frac{1}{2!}x^{2} + \frac{1}{4!}x^{4} - \frac{1}{6!}x^{6} + \frac{1}{8!}x^{8}...........(13)").shift(DOWN*3.3).scale(.5)



        self.play(FadeTransform(linear_transform_words, complex_map_words),runtime=5)
        self.play(FadeTransform(complex_map_words, complex_map_words2),runtime=5)
        self.play(Create(name3),runtime=5)
        self.play(Create(name4),runtime=5)
        self.play(Write(equation0),runtime=5)
        self.play(Write(equation1),runtime=5)
        self.play(Write(equation2),runtime=5)
        self.play(Write(equation3),runtime=5)
        self.play(Write(equation4),runtime=5)
        self.play(Write(equation5),runtime=5)
        self.play(Write(equation6),runtime=5)
        self.play(Write(equation7),runtime=5)
        self.play(Write(equation8),runtime=5)
        self.play(Write(equation9),runtime=5)
        self.play(Write(equation10),runtime=5)
        self.play(Write(equation11),runtime=5)
        self.play(Write(equation12),runtime=5)
        self.play(Write(equation13),runtime=5)
        self.play(Create(name5),runtime=5)
        self.play(Write(equation14),runtime=5)
        self.play(FadeTransform(equation14, equation15),runtime=7)
        self.wait(7)