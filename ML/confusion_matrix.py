from manimlib.imports import *
from scipy.stats import beta
import numpy as np

class IOMachine(Scene):
    #A few simple shapes
    def construct(self):
        circle = Circle()
        square = Square()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        self.add(circle)
        self.play(ShowCreation(line))
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))
        self.add(line)

class ProbabilityDistribution(GraphScene):
    CONFIG = {
        "x_max" : 1.01,    
        "x_min" : 0,
        "x_axis_label": "P(X)",
        "y_max" : 6, 
        "y_min" : 0,
        # "y_axis_label": "Number of Observations",


        "x_tick_frequency": 0.1,
        "exclude_zero_label":False,
        
        "function_color" : RED,
    }   
    def construct(self):
        self.setup_axes(animate=True)
        beta_neg = self.get_graph(self.beta_negative, self.function_color)
        beta_pos = self.get_graph(self.beta_positive)

        thr = 0.5
        threshold = self.get_vertical_line_to_graph(thr, beta_pos, DashedLine, color=YELLOW)

        FP_area = self.get_area(beta_pos,0,thr)
        TP_area = self.get_area(beta_pos,thr,1)
        TN_area = self.get_area(beta_neg,0,thr)
        FN_area = self.get_area(beta_neg,thr,1)


        self.play(ShowCreation(beta_neg))
        self.play(ShowCreation(beta_pos))
        self.play(ShowCreation(threshold))

        self.wait(1)
        self.play(ShowCreation(TP_area))
        self.play(ShowCreation(FP_area))
        self.play(FadeOut(TP_area), FadeOut(FP_area))

        self.play(ShowCreation(TN_area))
        self.play(FadeOut(TN_area), ShowCreation(FN_area))
        

    
    def beta_negative(self, x):
        offset = 2.5
        return beta.pdf(x, offset, 10-offset)
    def beta_positive(self, x):
        offset = 2.5
        return beta.pdf(x, 10-offset, offset)
        
