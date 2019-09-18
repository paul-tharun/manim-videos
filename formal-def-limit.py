# Part of this code has been taken from Purushart Saxsena's animation on limit of a sequence.
from manimlib.imports import *
import numpy as np
import math

def get_definition_text():
    return TextMobject(r"Let", r"$f(x)$", r"""be a function defined on an open interval around $x_{0}$ \\ """,
                        r"we say the limit", r"$f(x)$", r"as $x$ approaches $x_{0}$ is", r"L \\",
                        r"i.e $\lim _{x \rightarrow x_{0}} f(x)=L$ \\",
                        r"if for every $\varepsilon \textgreater 0 $ there exists a $\delta \textgreater 0$ such that for all x \\",
                        r"the following condition holds true \\" ,
                        r"$0 \textless \left|x-4\right| \textgreater \delta \Longrightarrow|f(x)-L| \textgreater \varepsilon$"
                       )

def get_custom_definition_text():
    custom_definition = TextMobject(r"The number", "5" ,"is said to be the limit of the",
                        r"function $f(x) = x +1$ \\",
                        r"as x tends to 4", r"for an arbitary $\epsilon$ say 1",
                        r"there exists a positive number \\ $\delta = 1$,",
                        r"such that for all", r"$|x-4| \textless \delta $ ", "the inequality",
                        r"$| f(x) - 5 | \textless 1$ \\", "holds true.")
    custom_definition.set_color_by_tex_to_color_map({r"function $f(x) = x +1$ \\": YELLOW,
                                                     r"$|x-4| \textless \delta $ ": BLUE,
                                                     r"$| f(x) - 5 | \textless 1$ \\": ORANGE})
    custom_definition.scale(0.6)
    custom_definition.shift(3.3*RIGHT+3*UP)

    return custom_definition

class IntroDefinitionText(Scene):
    def construct(self):
        definition = get_definition_text()
        title = TextMobject(r"The formal definition", "of a", "Limit")
        definition.set_color_by_tex_to_color_map({r"$f(x)$": YELLOW,
                                                  r"i.e $\lim _{x \rightarrow x_{0}} f(x)=L$ \\": PURPLE,
                                                  r"$0 \textless \left|x-x_{0}\right| \textgreater \delta \Longrightarrow|f(x)-L| \textgreater \varepsilon$": PURPLE})
        title.shift(3 * UP)
        title.scale(1.5)
        title.set_color_by_tex_to_color_map({
            "Limit": BLUE
        })

        self.play(Write(definition))
        self.wait(4)
        self.play(ApplyMethod(definition.move_to, 1*DOWN))
        self.play(Write(title))
        self.wait(3)

        but_what_does_it_mean = TextMobject("But what does it mean?")
        self.play(ReplacementTransform(definition, but_what_does_it_mean))
        self.wait(2)
        self.play(FadeOut(but_what_does_it_mean), FadeOut(title))
        self.wait(1)
def label(x,y):
        a = TexMobject(y)
        a.scale(0.5)
        a.set_color(x.get_color())
        a.add_background_rectangle()
        a.next_to(
                x.get_center(), 
                buff = SMALL_BUFF
            )
        return a


class ShowEquation(Scene):
    def construct(self):
        text = TextMobject("Consider the Function")
        text.shift(1*UP)
        eqn = TextMobject(r"$f(x) = x +1$")
        self.play(Write(text), Write(eqn))
        self.wait(2)
def epsilon_explain():
    
    a = TextMobject(r"The definition shows that if limit exists for however \\ small" ,
                    r"margin of error ($\varepsilon$) ",
                    r"we can find a", r"delta $\delta$" ,
                    r"such that \\ the interval", r"$(x-\delta,x+\delta)$" ,
                    r"corresponds to the",
                    r"margin of error", r"(L-$\varepsilon$,L+$\varepsilon$)")
    a.set_color_by_tex_to_color_map({r"$(x-\delta,x+\delta)$": YELLOW,
                                    r"(L-$\varepsilon$,L+$\varepsilon$)": YELLOW,
                                    r"margin of error ($\varepsilon$)": PURPLE,
                                     r"delta $\delta$": PURPLE})
    return a
def conclusion():
    return TextMobject(r"This can be tested by taking different values of delta and  \\seeing if an epsilon that satisfies the conditions can be found")
def final():
    final = TextMobject(r"As for any value of", r"$\delta$", r"how ever close to zero an",
                        r"$\varepsilon$", r"can be \\ found that satisfies the condition" ,
                      r"Hence it can be said \\" ,
                      r"$\lim _{x \rightarrow {4}} x+1=5$")
    final.set_color_by_tex_to_color_map({r"$\lim _{x \rightarrow {4}} x+1=5$": PURPLE,
                                         r"$\delta$": YELLOW,
                                         r"$\varepsilon$": YELLOW})
    final.scale(0.6)
    final.shift(3.3*RIGHT+3*UP)
    return final
def delta_val(x=1):
    delt = TextMobject(r"The value of $\delta$ is" , x)
    delt.scale(0.6)
    delt.shift(3.3*RIGHT+3*UP)
    return delt


class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 8,
        "y_min": 0,
        "y_max": 12,
        "graph_origin": ORIGIN+3*DOWN+6*LEFT,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$x$",
        "y_axis_label": "$f(x)$",
        "exclude_zero_label": True,
        "x_labeled_nums": range(0, 9, 2),
        "y_labeled_nums": range(0,13,2)
     }
    
    def construct(self):
        X_TICKS_DISTANCE = self.x_axis_width/(self.x_max - self.x_min)
        Y_TICKS_DISTANCE = self.y_axis_height / (self.y_max - self.y_min)
        epsilon = 1
        limit = 5
        delta = epsilon
        c = 4
        self.setup_axes(animate=True)
#        grid = NumberPlane()
#        self.add(grid)
        func_graph = self.get_graph(self.func_to_graph)
        equation = TextMobject(r"$x +1$")
        explain = epsilon_explain();explain.scale(0.6); explain.shift(2.3*RIGHT+2.8*UP)
        conclude = conclusion();conclude.scale(0.6); conclude.shift(2.5*RIGHT+2.8*UP)
        custom_definition = get_custom_definition_text(); custom_definition.shift(1*LEFT);
        positive_epsilon = [DashedLine(start = self.graph_origin + Y_TICKS_DISTANCE*(limit + epsilon)*UP ,
                                      end=self.graph_origin + Y_TICKS_DISTANCE*(limit + epsilon)*UP + X_TICKS_DISTANCE*(c+delta)*RIGHT ,
                                      color=DARK_BROWN)]

        negative_epsilon = [DashedLine(start = self.graph_origin + Y_TICKS_DISTANCE*(limit - epsilon)*UP ,
                                      end=self.graph_origin + Y_TICKS_DISTANCE*(limit - epsilon)*UP + X_TICKS_DISTANCE*(c+delta)*RIGHT ,
                                      color=DARK_BROWN)]
        positive_delta = [DashedLine(start = self.graph_origin + X_TICKS_DISTANCE*(c + delta)*RIGHT ,
                                    end=self.graph_origin + X_TICKS_DISTANCE*(c + delta)*RIGHT+ Y_TICKS_DISTANCE*(limit+epsilon)*UP,
                                      color=BLUE)]
        negative_delta = [DashedLine(start = self.graph_origin + X_TICKS_DISTANCE*(c - delta)*RIGHT ,
                                    end=self.graph_origin + X_TICKS_DISTANCE*(c - delta)*RIGHT + Y_TICKS_DISTANCE*(limit+epsilon)*UP,
                                      color=BLUE)]
        y_line = Line(start = self.graph_origin + Y_TICKS_DISTANCE*5*UP,
                      end = self.graph_origin + Y_TICKS_DISTANCE*5*UP + X_TICKS_DISTANCE*4*RIGHT, color = WHITE)
        x_line = Line(start = self.graph_origin + X_TICKS_DISTANCE*4*RIGHT,
                      end = self.graph_origin + Y_TICKS_DISTANCE*5*UP + X_TICKS_DISTANCE*4*RIGHT, color = WHITE)
        N =  Dot(color = RED, radius = 0.05)
        L = Dot(color = BLUE, radius = 0.05)
        C = Dot(color = BLUE, radius = 0.05)
        plusd = [Dot(color = TEAL_A, radius = 0.05)]
        minusd = [Dot(color = TEAL_A, radius = 0.05)]
        pluse  = [Dot(color = PURPLE_A, radius = 0.05)]
        minuse = [Dot(color = PURPLE_A, radius = 0.05)]
        N.shift(self.graph_origin + X_TICKS_DISTANCE*4*RIGHT + Y_TICKS_DISTANCE*5*UP)
        L.shift(self.graph_origin + Y_TICKS_DISTANCE*5*UP)
        C.shift(self.graph_origin + X_TICKS_DISTANCE*4*RIGHT)
        plusd[0].shift(self.graph_origin + X_TICKS_DISTANCE*(delta+c)*RIGHT)
        minusd[0].shift(self.graph_origin + X_TICKS_DISTANCE*(c-delta)*RIGHT)
        pluse[0].shift(self.graph_origin + Y_TICKS_DISTANCE*(epsilon+limit)*UP)
        minuse[0].shift(self.graph_origin + Y_TICKS_DISTANCE*(limit-epsilon)*UP)
        L_label = label(L,"L")
        C_label = label(C,"C")
        pd_label = [label(plusd[0],"C + \\delta").shift(0.2*UP)]
        md_label = [label(minusd[0],"C - \\delta").shift(0.2*UP+0.8*LEFT)]
        pe_label= [label(pluse[0],"L + \\varepsilon").shift(0.2*UP)]
        me_label = [label(minuse[0],"L - \\varepsilon").shift(0.2*DOWN)]
        equation.shift(3.3*RIGHT+3*UP)
        self.play(FadeIn(equation))
        self.play(ShowCreation(func_graph))
        self.wait(3)
        self.play(FadeOut(equation));self.wait(1)
        self.play(FadeIn(custom_definition));self.wait(4)
        self.play(ShowCreation(N)); self.wait(2)
        self.play(ShowCreation(x_line),ShowCreation(C),ShowCreation(C_label));
        self.play(ShowCreation(y_line),ShowCreation(L),ShowCreation(L_label)) ; self.wait(3)
        self.play(ShowCreation(positive_epsilon[0]),ShowCreation(pluse[0]),ShowCreation(pe_label[0])); 
        self.play(ShowCreation(negative_epsilon[0]),ShowCreation(minuse[0]),ShowCreation(me_label[0])); self.wait(3)
        self.play(ShowCreation(positive_delta[0]) ,ShowCreation(negative_epsilon[0]),ShowCreation(plusd[0]),ShowCreation(pd_label[0]),
                  ShowCreation(negative_delta[0]),ShowCreation(negative_epsilon[0]),ShowCreation(minusd[0]),ShowCreation(md_label[0]));
        self.wait(3)
        self.play(ReplacementTransform(custom_definition,explain));self.wait(4)
        epsilon_rectangle = [Rectangle(color=GOLD_B, color_opacity=0.2, fill_color=GOLD_B, fill_opacity=0.2,
                                    height=Y_TICKS_DISTANCE*(2*epsilon), width=X_TICKS_DISTANCE*(c+delta))]
        epsilon_rectangle[0].shift(self.graph_origin + X_TICKS_DISTANCE*2.5*RIGHT + Y_TICKS_DISTANCE*5*UP)
        delta_rectangle = [Rectangle(color=BLUE_B, color_opacity=0.2, fill_color=BLUE_B, fill_opacity=0.2,
                                    height=Y_TICKS_DISTANCE*(limit+epsilon), width=X_TICKS_DISTANCE*(2*delta))]
        delta_rectangle[0].shift(self.graph_origin + X_TICKS_DISTANCE*4*RIGHT + Y_TICKS_DISTANCE*3*UP)
        self.play(ShowCreation(epsilon_rectangle[0]), ShowCreation(delta_rectangle[0])); self.wait(5)
        
        self.play(ReplacementTransform(explain,conclude));self.wait(5);
        delt = [delta_val()]
        self.play(ReplacementTransform(conclude,delt[0])); self.wait(2)
        
        i = 1
        vals = list(np.linspace(1,10,5,endpoint = False))
        vals.append(9.999)
        for k in vals:
            epsilon = round(1-(k/10),4)
            delta = epsilon
            plusd.append(Dot(color = TEAL_A, radius = 0.05))
            minusd.append(Dot(color = TEAL_A, radius = 0.05))
            pluse.append(Dot(color = PURPLE_A, radius = 0.05))
            minuse.append(Dot(color = PURPLE_A, radius = 0.05))
            plusd[i].shift(self.graph_origin + X_TICKS_DISTANCE*(delta+c)*RIGHT)
            minusd[i].shift(self.graph_origin + X_TICKS_DISTANCE*(c-delta)*RIGHT)
            pluse[i].shift(self.graph_origin + Y_TICKS_DISTANCE*(epsilon+limit)*UP)
            minuse[i].shift(self.graph_origin + Y_TICKS_DISTANCE*(limit-epsilon)*UP)
            pd_label.append(label(plusd[i],"C + \\delta").shift(0.2*UP))
            md_label.append(label(minusd[i],"C - \\delta").shift(0.2*UP+0.8*LEFT))
            pe_label.append(label(pluse[i],"L + \\varepsilon").shift(0.2*UP))
            me_label.append(label(minuse[i],"L - \\varepsilon").shift(0.2*DOWN))
            delt.append(delta_val(delta))
        
            positive_epsilon.append(DashedLine(start = self.graph_origin + Y_TICKS_DISTANCE*(limit + epsilon)*UP ,
                                    end=self.graph_origin + Y_TICKS_DISTANCE*(limit + epsilon)*UP + X_TICKS_DISTANCE*(c+delta)*RIGHT ,
                                    color=DARK_BROWN))

            negative_epsilon.append(DashedLine(start = self.graph_origin + Y_TICKS_DISTANCE*(limit - epsilon)*UP ,
                                    end=self.graph_origin + Y_TICKS_DISTANCE*(limit - epsilon)*UP + X_TICKS_DISTANCE*(c+delta)*RIGHT ,
                                    color=DARK_BROWN))
            positive_delta.append(DashedLine(start = self.graph_origin + X_TICKS_DISTANCE*(c + delta)*RIGHT ,
                                  end=self.graph_origin + X_TICKS_DISTANCE*(c + delta)*RIGHT+ Y_TICKS_DISTANCE*(limit+epsilon)*UP,
                                  color=BLUE))
            negative_delta.append(DashedLine(start = self.graph_origin + X_TICKS_DISTANCE*(c - delta)*RIGHT ,
                                  end=self.graph_origin + X_TICKS_DISTANCE*(c - delta)*RIGHT + Y_TICKS_DISTANCE*(limit+epsilon)*UP,
                                  color=BLUE))
            epsilon_rectangle.append(Rectangle(color=GOLD_B, color_opacity=0.2, fill_color=GOLD_B, fill_opacity=0.2,
                                     height=Y_TICKS_DISTANCE*(2*epsilon), width=X_TICKS_DISTANCE*(c+delta)))
            epsilon_rectangle[i].move_to(epsilon_rectangle[0].get_center())
            epsilon_rectangle[i].shift(((1-epsilon)/2)*LEFT)
            delta_rectangle.append(Rectangle(color=BLUE_B, color_opacity=0.2, fill_color=BLUE_B, fill_opacity=0.2,
                                    height=Y_TICKS_DISTANCE*(limit+epsilon), width=X_TICKS_DISTANCE*(2*delta)))
            delta_rectangle[i].move_to(delta_rectangle[0].get_center())
            delta_rectangle[i].shift(((1-epsilon)/4)*DOWN)
            self.play(ReplacementTransform(delt[i-1],delt[i]),
                      ReplacementTransform(positive_epsilon[i-1], positive_epsilon[i]),
                      ReplacementTransform(positive_delta[i-1], positive_delta[i]),
                      ReplacementTransform(negative_epsilon[i-1], negative_epsilon[i]),
                      ReplacementTransform(negative_delta[i-1], negative_delta[i]),
                      ReplacementTransform(epsilon_rectangle[i-1], epsilon_rectangle[i]),
                      ReplacementTransform(delta_rectangle[i-1], delta_rectangle[i]),
                      ReplacementTransform(plusd[i-1],plusd[i]),
                      ReplacementTransform(pluse[i-1],pluse[i]),
                      ReplacementTransform(minusd[i-1],minusd[i]),
                      ReplacementTransform(minuse[i-1],minuse[i]),
                      ReplacementTransform(pe_label[i-1],pe_label[i]),
                      ReplacementTransform(pd_label[i-1],pd_label[i]),
                      ReplacementTransform(me_label[i-1],me_label[i]),
                      ReplacementTransform(md_label[i-1],md_label[i])); self.wait(2)
            i += 1
            
        self.play(FadeOut(delt[i-1]),FadeIn(final())); self.wait(6)

    def func_to_graph(self,x):
        return x +1
