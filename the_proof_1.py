from manim import *
import numpy as np
class OpeningManimExample(Scene):
    def construct(self):
        
        name = Text("Now, Carefully notice the exapansion of").shift(UP*3).scale(.5)
        name.set_color_by_gradient(PURE_BLUE, WHITE)
        equation = MathTex(r"e^{x}.....").shift(UP*3).shift(RIGHT*3.5).scale(.7)
        equation2 = MathTex(r"e^{x} = 1 + x +\frac{1}{2!}(x)^{2} +\frac{1}{3!}(x)^{3}+\frac{1}{4!}(x)^{4}+\frac{1}{5!}(x)^{5}+ \frac{1}{6!}x^{6}.....", tex_to_color_map={"x": RED}).shift(UP*2.3).scale(.7)
        name2 = Text("We can write it as..").shift(LEFT*4).shift(UP*1.6).scale(.5)
        name2.set_color_by_gradient(PURE_BLUE, WHITE)
        equation3 = MathTex(r"e^{x} = (1 + \frac{1}{2!}x^{2} + \frac{1}{4!}x^{4} + \frac{1}{6!}x^{6} +...) + (x + \frac{1}{3!}x^{3} + \frac{1}{5!}x^{5} + \frac{1}{7!}x^{7} +....) ", tex_to_color_map={"x": RED}).shift(UP*.8).scale(.7)
        circ = Circle().scale(.22).shift(UP*.8).shift(LEFT*3.89)
        circ2 = Circle().scale(.22).shift(UP*.8).shift(LEFT*1.6)
        rect = Rectangle(color = WHITE, height = .5, width = 1.2).shift(LEFT*2.5).shift(DOWN*1.2)
        arrow1 = Line(start=circ.get_bottom(), end=rect.get_top(), buff=0.2).add_tip()
        arrow2 = Line(start=circ2.get_bottom(), end=rect.get_top(), buff=0.2).add_tip()
        name3 = Text("-").shift(LEFT*2.5).shift(DOWN*1.2).scale(1)
        circ3 = Circle().scale(.22).shift(UP*.8).shift(RIGHT*3.45)
        circ4 = Circle().scale(.22).shift(UP*.8).shift(RIGHT*1.15)
        rect2 = Rectangle(color = WHITE, height = .5, width = 1.2).shift(RIGHT*2.5).shift(DOWN*1.2)
        arrow3 = Line(start=circ3.get_bottom(), end=rect2.get_top(), buff=0.2).add_tip()
        arrow4 = Line(start=circ4.get_bottom(), end=rect2.get_top(), buff=0.2).add_tip()
        name4 = Text("-").shift(RIGHT*2.5).shift(DOWN*1.2).scale(1)
        name5 = Text("cosx").shift(LEFT*2.5).shift(DOWN*2).scale(1)
        name6 = Text("sinx").shift(RIGHT*2.5).shift(DOWN*2).scale(1)
        name7 = Text("So how do we get '-' then??").shift(DOWN*3).scale(.7)
        name.set_color_by_gradient(BLUE, WHITE)
        
        
        
        
        
        
        
        self.play(Create(name),runtime=5)
        self.play(Write(equation),runtime=5)
        self.play(Write(equation2),runtime=5)
        self.play(Create(name2),runtime=5)
        self.play(Write(equation3),runtime=5)
        self.play(Create(circ),runtime=5)
        self.play(Create(circ2),runtime=5)
        arrows = [arrow1, arrow2]
        self.play(*[Create(arrow) for arrow in arrows], runtime=5)
        self.play(Create(rect),runtime=5)
        self.play(Create(name3),runtime=5)
        self.play(Create(name5),runtime=5)
        self.play(Create(circ3),runtime=5)
        self.play(Create(circ4),runtime=5)
        arrows = [arrow3, arrow4]
        self.play(*[Create(arrow) for arrow in arrows], runtime=5)
        self.play(Create(rect2),runtime=5)
        self.play(Create(name4),runtime=5)
        self.play(Create(name6),runtime=5)
        self.play(Create(name7),runtime=5)
        self.wait(5)