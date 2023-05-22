from manim import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.


class OpeningManimExample(Scene):
    def construct(self):
         # Linear transform
        linear_transform_words = Tex("This is what the matrix")
        linear_transform_words.arrange(RIGHT)
        linear_transform_words.to_edge(UP)
        linear_transform_words.scale(1)

        # Complex map
        complex_map_words = Tex("This is what the matrlx")
        complex_map_words.arrange(RIGHT)
        complex_map_words.to_edge(UP)
        complex_map_words.scale(1)

        self.play(FadeTransform(linear_transform_words, complex_map_words))
        self.wait(2)
