from manimlib.imports import *
from scipy.stats import norm, chi2, uniform
import numpy as np

def neat_dict(dict):
    print("\n".join("{}\t{}".format(k, v) for k, v in dict.items()))

class Shape(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.play(ShowCreation(circle))
        self.add(square)

class CircleTest(GraphScene):
    CONFIG = {
        "x_axis_label": "",
        "y_axis_label": "",
        "x_axis_width": FRAME_WIDTH - LARGE_BUFF,
        "y_axis_height": FRAME_HEIGHT / 2,
        "y_max": .5,
        "y_min": 0,
        "x_max": 4,
        "x_min": -4,
        "x_labeled_nums": np.arange(-4,4),
        #"y_labeled_nums": np.arange(0,.5,.1),
        #"y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "axes_color": WHITE,
        "graph_origin": np.array(
            (0, -FRAME_Y_RADIUS + LARGE_BUFF, 0)),
        "exclude_zero_from_default_numbers": True,
        "x_label_decimals": 1,
        "y_label_decimals": 1,

    }
    def generate_y_coords(self, x_vals):
        x_y_coords = []
        y_dict = {}
        for x in x_vals:
            if x in y_dict:
                y_dict[x] += .05
                x_y_coords.append([x, y_dict[x]])
            else:
                y_dict[x] = .05
                x_y_coords.append([x, y_dict[x]])
        return x_y_coords



    def construct(self):
        t1 = TexMobject('X \sim \mathcal{N}(\mu,\,\sigma^{2})')
        t1.to_edge(UR)
        t2 = TexMobject('X^2 \sim \chi^2_1')
        t2.next_to(t1, direction=DOWN)
        
        self.setup_axes()

        normal = self.get_graph(lambda x: norm.pdf(x), color=ORANGE, x_min=-3, x_max=3)
        chisquaredf1 = self.get_graph(lambda x: chi2.pdf(x, df=1), color=BLUE, x_min=0, x_max=3)

        self.play(
            FadeIn(t1),
            FadeIn(self.axes)
        )
        dot1 = Dot(self.coords_to_point(2, .2))
        dot2 = Dot(self.coords_to_point(-2, .2))
        
        x_vals = [round(x * 10) / 10 for x in norm.rvs(size=150)]
        x_vals_squared = [round(x**2 * 10) / 10 for x in x_vals]
        coords = self.generate_y_coords(x_vals)
        coords_squared = self.generate_y_coords(x_vals_squared)
        
        dots_norm = [Dot(point=self.coords_to_point(*coord)) for coord in coords]
        dots_chi = [Dot(point=self.coords_to_point(*coord)) for coord in coords_squared]
        
        dots_norm_anim = dots_norm[:5]
        dots_chi_anim = dots_chi[:5]

        dots_norm_group = VGroup(*dots_norm[5:])
        dots_chi_group = VGroup(*dots_chi[5:])
        
        
        for dot in dots_norm_anim: self.play(FadeInFrom(dot, UP), run_time=0.25)
        self.wait(1)
        self.play(FadeInFrom(dots_norm_group, UP))
        self.play(ShowCreation(normal))

        for i in range(len(dots_norm)):
            self.play(ApplyMethod(dots_norm[i].move_to, dots_chi[i]), run_time=.05,)
            dots_norm[i].set_color(GREEN) 
        self.wait(1)

        # self.play(
        #     ApplyMethod(dots_norm_group.move_to, dots_chi_group)
        # )


        self.play(FadeIn(t2))
        self.play(ShowCreation(chisquaredf1))
    
    

        

class Perf1(GraphScene):
    """
    A simple scene of two animations from the end of a video on recursion.

    - Uses a graph in 1/4 of the scene.
    - First fades in multiple lines of text and equations, and the graph axes.
    - Next animates creation of two graphs and the creation of their text
      labels.
    """
    CONFIG = {
        "x_axis_label":
        "$n$",
        "y_axis_label":
        "$time$",
        "x_axis_width":
        FRAME_HEIGHT,
        "y_axis_height":
        FRAME_HEIGHT / 4,
        "y_max":
        50,
        "y_min":
        0,
        "x_max":
        100,
        "x_min":
        0,
        "x_labeled_nums": [50, 100],
        "y_labeled_nums":
        range(0, 51, 10),
        "y_tick_frequency":
        10,
        "x_tick_frequency":
        10,
        "axes_color":
        BLUE,
        "graph_origin":
        np.array(
            (-FRAME_X_RADIUS + LARGE_BUFF, -FRAME_Y_RADIUS + LARGE_BUFF, 0))
    }

    def construct(self):
        t1 = TextMobject(
            "Dividing a problem in half over and over means\\\\"
            "the work done is proportional to $\\log_2{n}$").to_edge(UP)

        t2 = TextMobject(
            '\\textit{This is one of our\\\\favorite things to do in CS!}')
        t2.to_edge(RIGHT)

        t3 = TextMobject(
            'The new \\texttt{power(x,n)} is \\underline{much}\\\\better than the old!'
        )
        t3.scale(0.8)
        p1f = TexMobject('x^n=x \\times x^{n-1}').set_color(ORANGE)
        t4 = TextMobject('\\textit{vs.}').scale(0.8)
        p2f = TexMobject(
            'x^n=x^{\\frac{n}{2}} \\times x^{\\frac{n}{2}}').set_color(GREEN)
        p1v2g = VGroup(t3, p1f, t4, p2f).arrange(DOWN).center().to_edge(RIGHT)

        self.setup_axes()
        o_n = self.get_graph(lambda x: x, color=ORANGE, x_min=1, x_max=50)
        o_log2n = self.get_graph(lambda x: math.log2(x),
                                 color=GREEN,
                                 x_min=2,
                                 x_max=90)
        onl = TexMobject('O(n)')
        olog2nl = TexMobject('O(\\log_2{n})')
        onl.next_to(o_n.get_point_from_function(0.6), UL)
        olog2nl.next_to(o_log2n.get_point_from_function(0.8), UP)
        self.play(
            FadeIn(t1),
            FadeIn(self.axes),
            # FadeInFromDown(t2),
            FadeIn(p1v2g),
            run_time=1
        )
        self.play(ShowCreation(o_n),
                  ShowCreation(o_log2n),
                  ShowCreation(onl),
                  ShowCreation(olog2nl),
                  run_time=3)
        self.wait(duration=5)

        
