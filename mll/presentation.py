"""Presentation for MLL Symposium.

Presentation Draft:

Intro:
Pandas:
Problem:
Mission:
CSGM:
Problems of CSGM:
ILO:
SGILO:
"""
from manim import *
from manim_pptx import *

import copy
import itertools

screen_width = 13
time_per_char = 0.05

# captions
caption_font_size = 28
caption_color = YELLOW
caption_top_margin = 10
caption_left_margin = 8

factor: 0.5  # downsampling factor
image_resolution = 2048
text_margin = 8

# generator 
gen_width = 0.5
num_layers = 4
layers_dist = 6
gen_color = YELLOW

# loss
loss_width = 4.5
loss_height = 1.5
loss_color = RED

def connect_shapes(obj1, obj2, color=WHITE):
    arrow_up = Arrow(start=obj1.get_corner(RIGHT + UP), 
        end=obj2.get_corner(LEFT + UP), color=color)
    arrow_down = Arrow(start=obj1.get_corner(RIGHT + DOWN), 
        end=obj2.get_corner(LEFT + DOWN), color=color)
    return arrow_up, arrow_down


def get_text_runtime(text):
    return len(text) * time_per_char


def split_lines(text, limit=30000):
    words = text.split(' ')
    new_text = []
    counter = 0
    for word in words:
        if len(word) + counter > limit:
            new_text.append(r"\\ {}".format(word))
            counter = 0
        else:
            new_text.append(word)
            counter += len(word)
    return " ".join(new_text)
        

class Intro(PPTXScene):
    def construct(self):
        title = Tex(r"Generative Models for Reconstruction, Art and Things in Between")
        title.stretch_to_fit_width(screen_width)
        subtitle = Tex(r"A short introduction to Intermediate Layer Optimization")
        subtitle.stretch_to_fit_width(0.8 * screen_width)
        VGroup(title, subtitle).arrange(DOWN)
        self.play(
            FadeIn(title),
        )
        self.wait()
        self.endSlide()
        self.play(FadeIn(subtitle))
        self.wait()
        self.endSlide()


class Pandas(PPTXScene):
    def construct(self):
        gen_text = r"Generative models are {{impressive}}"
        title = Tex(gen_text)
        title.set_color_by_tex('impressive', RED)
        self.play(FadeIn(title, run_time=get_text_runtime(title)))
        self.wait()
        self.endSlide()

        transform_title = Tex(gen_text)
        transform_title.set_color_by_tex('impressive', RED)
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
        )
        self.wait()
        self.endSlide()
        
        monkey_text = Tex(r"\textit{A toilet car}", font_size=caption_font_size, 
            color=caption_color).to_corner(
                UP + LEFT + np.array([0, caption_top_margin, 0]))
        monkey_image = ImageMobject("images/toilet_car.jpeg", 
            scale_to_resolution=image_resolution).shift(4 * LEFT + UP)
        monkey_image.next_to(monkey_text, UP)

        self.play(FadeIn(monkey_text), FadeIn(monkey_image))
        self.wait()
        monkey_group = Group(monkey_text, monkey_image)
        self.endSlide()



        pandas_text = Tex(r"\textit{Cute golden retriever puppy \\ wearing glasses and a suit}", font_size=caption_font_size, 
            color=caption_color).to_corner(
                UP + LEFT + np.array([0, caption_top_margin, 0]))
        pandas_text.next_to(monkey_text, 8 * RIGHT)
        pandas_image = ImageMobject("images/golden_retriever.jpeg", 
            scale_to_resolution=image_resolution).shift(4 * LEFT + UP)
        pandas_image.next_to(pandas_text, UP)
        self.play(FadeIn(pandas_text), FadeIn(pandas_image))
        self.wait()
        pandas_group = Group(pandas_text, pandas_image)
        self.endSlide()


        picasso_text = Tex(r"\textit{Hyperrealistic painting of an \\ extraterrestrial  alien lovingly \\holding a rabbit}", font_size=caption_font_size, 
            color=caption_color).to_corner(
                UP + LEFT + np.array([0, caption_top_margin, 0]))
        picasso_text.next_to(pandas_text, 8 * RIGHT)
        picasso_image = ImageMobject("images/alien.jpeg", 
            scale_to_resolution=image_resolution).shift(4 * LEFT + UP)
        picasso_image.next_to(picasso_text, UP)
        self.play(FadeIn(picasso_text, picasso_image))
        self.wait()
        picasso_group = Group(picasso_text, picasso_image)
        self.endSlide()

        # make objects small
        mobj = Group(monkey_group, pandas_group, picasso_group)
        factor = 0.5
        new_width = mobj.width * factor
        new_height = mobj.height * factor
        self.play(
            mobj.animate.stretch_to_fit_height(
                new_height).stretch_to_fit_width(
                    new_width).next_to(title, DOWN).align_to(title, LEFT))
        self.wait()
        self.endSlide()

        # StyleGAN photos
        stylegan_face1 = ImageMobject("images/stylegan2.jpeg", 
            scale_to_resolution=1.20 * image_resolution).next_to(mobj, DOWN)
        stylegan_face1.align_to(title, LEFT)
        # self.play(FadeIn(stylegan_face1))
        # self.wait()
        # self.add(stylegan_face1)

        stylegan_face2 = ImageMobject("images/stylegan3.jpeg", 
            scale_to_resolution=1.25 * image_resolution).next_to(stylegan_face1)
        stylegan_photos = Group(stylegan_face1, stylegan_face2)
        self.play(FadeIn(stylegan_face1), FadeIn(stylegan_face2))
        self.wait()
        self.endSlide()

        gpt_text = r"``It is important for AI researchers to be aware of the potential biases in large generative models like GPT-3 and to take steps to mitigate these biases. \\ -- Written by GPT-3.''"
        gpt_text = Tex(split_lines(gpt_text, limit=18), font_size=35, color=YELLOW)
        gpt_text.next_to(stylegan_photos, 2.0 * RIGHT + 0.5 * UP)
        self.play(FadeIn(gpt_text, run_time=3))
        self.wait()
        self.endSlide()




class Problem(PPTXScene):
    def construct(self):
        gen_text = r"Generative models are {{impressive}}"
        title = Tex(gen_text)
        title.set_color_by_tex('impressive', RED)
        self.play(FadeIn(title, run_time=2))
        self.endSlide()
        useful_text = r"Are they {{useful}}?"
        title.set_color_by_tex('useful', RED)
        useful_text = Tex(useful_text)
        
        self.remove(title)
        self.play(Create(useful_text))
        self.wait()
        self.endSlide()

        self.play(useful_text.animate.align_on_border(LEFT + UP))
        problems_text = Tex(r"Examples of problems we care about:")
        problems_text.next_to(useful_text, 3 * DOWN).align_to(useful_text, LEFT)
        blist = BulletedList("Inpainting", "Denoising", "Accelerating MRI", height=2, width=4)
        blist.set_color_by_tex("Inpainting", RED)
        blist.set_color_by_tex("Denoising", GREEN)
        blist.set_color_by_tex("Accelerating MRI", BLUE)
        self.play(FadeIn(problems_text), FadeIn(blist))
        self.wait()
        self.endSlide()

        


class SuperResolution(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=1,
            zoomed_display_width=6,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )

    def construct(self):
        image = ImageMobject("downsampled_white.jpg", 
            scale_to_resolution=image_resolution)
        self.add(image)
        self.wait()

        aligned = ImageMobject("downsampled_white.jpg", 
            scale_to_resolution=2.00 * image_resolution).align_on_border(LEFT)


        clean_image = ImageMobject("test_image.jpg", 
            scale_to_resolution=1.00 * image_resolution).next_to(aligned, RIGHT * 8)

        
        arrow_up = Arrow(start=aligned.get_corner(RIGHT + UP), end=clean_image.get_corner(LEFT + UP))
        arrow_down = Arrow(start=aligned.get_corner(RIGHT + DOWN), end=clean_image.get_corner(LEFT + DOWN))
        self.play(Transform(image, aligned),
            FadeIn(arrow_up), 
            FadeIn(arrow_down),
            FadeIn(clean_image))

        self.wait()

        dot1 = Dot(aligned.get_center(), color=YELLOW)
        dot2 = Dot(clean_image.get_center(), color=BLUE)
        self.add(dot1, dot2)

        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        
        frame2 = zoomed_camera.frame
        frame1 = copy.deepcopy(frame2)
        frame1.set_color(YELLOW)
        frame2.set_color(BLUE)

        zoomed_display_frame1 = zoomed_display.display_frame
        frame1.move_to(dot1)
        frame2.move_to(dot2)

        frame1_dot_group = Group(frame1, dot1)
        frame2_dot_group = Group(frame2, dot2)
        
        # zoomed_display_frame2.set_color(RED)

        zoomed_display.shift(
            3 * DOWN + 0.9 * RIGHT).scale_to_fit_width(0.8 * zoomed_display.width)

        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)

        self.play(Create(frame1), frame2_dot_group.animate.set_y(frame1.get_y()))

        self.zoom_activated = True
        self.renderer.camera.add_image_mobject_from_camera(self.zoomed_display)
        self.add_foreground_mobjects(
            self.zoomed_camera.frame,
            frame1,
        )
        self.play(self.get_zoomed_display_pop_out_animation())

        self.play(
            frame2_dot_group.animate.shift(1.0 * DOWN),
            frame1_dot_group.animate.shift(0.5 * DOWN))
        self.wait()
        
        left_corner = frame2.get_corner(LEFT + DOWN)
        right_corner = frame2.get_corner(RIGHT + DOWN)

        self.wait()



class Generator(PPTXScene):
    def construct(self):
        layers = []
        for index in range(num_layers):
            layers.append(Rectangle(width=gen_width, height=1.4**(index + 1)))
            if index != 0:
                layers[-1].next_to(layers[index - 1], layers_dist * RIGHT)
                text = MathTex(r"z_{}".format(index)).next_to(layers[-1], DOWN)
                arrow_up, arrow_down = connect_shapes(layers[-2], layers[-1], 
                    color=gen_color)
                gen_text = MathTex(r"G_{}".format(index), color=gen_color)
                gen_text.next_to(layers[-2], 2 * RIGHT)
                # gen_text.set(0.5 * layers[-2].get_center() + 
                #     0.5 * layers[-1].get_center())
                self.play(FadeIn(layers[-1]),
                    FadeIn(arrow_up), FadeIn(arrow_down),
                    Create(text), Create(gen_text))
            else:
                layers[0].align_on_border(LEFT).shift(1.8 * UP)
                first_text = MathTex(r"z_{}".format(index)).next_to(layers[-1], DOWN)
                self.play(FadeIn(layers[0]), Create(first_text))
        generator = VGroup(*layers)
        self.add(generator)
        self.wait()
        self.endSlide()


        ax = Axes(x_range=[0, 10])[0]
        ax.align_on_border(LEFT + DOWN)

        dot = Dot(ax.get_center(), color=BLUE)
        value_tracker = ValueTracker(0)
        dot.add_updater(lambda z: z.set_x(value_tracker.get_value()))


        line = Line(first_text, dot.get_center())
        line.add_updater(lambda z: z.become(Line(dot.get_center(), first_text)))

        image_paths = itertools.cycle(sorted(['images/interpolations/' + x for x in os.listdir('images/interpolations')]))

        image = ImageMobject(next(image_paths), 
            scale_to_resolution=0.6 * image_resolution).next_to(layers[-1], RIGHT * 4)        
        def image_updater(z):
            nonlocal image
            new_image = ImageMobject(next(image_paths), 
                scale_to_resolution=0.6 * image_resolution).next_to(layers[-1], RIGHT * 4)
            image.pixel_array = new_image.pixel_array
        image.add_updater(image_updater)

        # def first_text_updater(z):
        #     nonlocal first_text
        #     first_text.tex_string = r"z_0={}".format(value_tracker.get_value())
        # first_text.add_updater(first_text_updater)
    
        self.play(FadeIn(dot), FadeIn(image), FadeIn(line), FadeIn(ax))
        # self.wait()
        self.endSlide()


        self.play(value_tracker.animate.set_value(5), run_time=4)
        self.wait()
        self.endSlide()


class CSGM(PPTXScene):
    def construct(self):
        layers = []
        arrows = []
        texts = []
        for index in range(num_layers):
            layers.append(Rectangle(width=gen_width, height=1.4**(index + 1)))
            if index != 0:
                layers[-1].next_to(layers[index - 1], layers_dist * RIGHT)
                text = MathTex(r"z_{}".format(index)).next_to(layers[-1], DOWN)
                arrow_up, arrow_down = connect_shapes(layers[-2], layers[-1], 
                    color=gen_color)
                arrows.append(arrow_up)
                arrows.append(arrow_down)
                gen_text = MathTex(r"G_{}".format(index), color=gen_color)
                gen_text.next_to(layers[-2], 2 * RIGHT)
                self.add(layers[-1],
                    arrow_up, arrow_down,
                    text, gen_text)
                texts.append(gen_text)
                texts.append(text)
            else:
                layers[0].align_on_border(LEFT).shift(1.8 * UP)
                first_text = MathTex(r"z_{}".format(index)).next_to(layers[-1], DOWN)
                self.add(layers[0], first_text)
                texts.append(first_text)
        generator = VGroup(*layers, *texts, *arrows)
        self.play(FadeIn(generator))
        self.wait()
        self.endSlide()

        loss = MathTex(r"\left|\left|G_3G_2G_1(z_0) - x\right|\right|^2")
        loss_rec = Rectangle(height=loss_height, width=loss_width, color=loss_color)
        loss_rec.next_to(0.5 * layers[1].get_center() + 
            0.5 * layers[2].get_center(), 12 * DOWN + 0.25 * RIGHT)
        loss.move_to(loss_rec.get_center())


        # smooth connections
        dot1 = Dot()
        dot1.next_to(layers[-1], 10 * RIGHT)
        x_text = MathTex(r"x")
        x_text.next_to(dot1, UP)

        x_image = ImageMobject("images/alex_real.png", scale_to_resolution=1.00 * image_resolution)
        x_image.next_to(x_text, RIGHT)

        dot2 = Dot()
        dot2.next_to(dot1, 12 * DOWN)
        dot2.set_y(loss_rec.get_center()[1])

        dot3 = Dot()
        dot3 = dot3.next_to(dot2, LEFT)
        rec_right_x = (0.5 * loss_rec.get_corner(RIGHT + UP) + 0.5 * loss_rec.get_corner(DOWN + RIGHT))[0]
        dot3.set_x(rec_right_x)



        n_arrows = []
        things_to_connect = [layers[-1].get_center(), dot1, dot2, dot3]
        for index in range(0, len(things_to_connect) - 1):
            n_arrows.append(Arrow(start=things_to_connect[index], 
                end=things_to_connect[index + 1]))
        
        dot4 = Dot()
        dot4.next_to(loss_rec, LEFT)
        rec_left_x = (0.5 * loss_rec.get_corner(LEFT + UP) + 0.5 * loss_rec.get_corner(DOWN + LEFT))[0]
        dot4.set_x(rec_left_x)
        
        dot5 = Dot()
        dot5.next_to(dot4, LEFT)
        dot5.set_x(first_text.get_center()[0])

        n_arrows.append(Arrow(start=dot4, end=dot5))
        n_arrows.append(Arrow(start=dot5, end=first_text))


        scene_components = [loss, loss_rec, dot1, dot2, dot3, dot4, dot5, *n_arrows, x_text, x_image]
        self.play(*[FadeIn(x) for x in scene_components])
        self.wait()
        self.endSlide()

        mobj = Group(generator, *scene_components)
        orig_coords = mobj.get_center()
        factor = 0.5
        new_width = mobj.width * factor
        new_height = mobj.height * factor
        self.play(
            mobj.animate.stretch_to_fit_height(
                new_height).stretch_to_fit_width(
                    new_width).align_on_border(UP + LEFT))
        self.wait()
        self.endSlide()

        rec_text = MathTex(r"G(z_0*)", color=YELLOW)
        rec_image = ImageMobject("images/alex_csgm.png", scale_to_resolution=0.5 * image_resolution)
        rec_image.move_to(np.array([3., 0., 0.]))
        rec_text.next_to(rec_image, DOWN)
        self.play(FadeIn(rec_image), FadeIn(rec_text))
        self.wait()
        self.endSlide()

        
        self.play(FadeOut(rec_text), FadeOut(rec_image), mobj.animate.move_to(orig_coords))
        self.wait()
        self.endSlide()


        ###### ILO
        ilo_tex = Tex(r"Intermediate Layer Optimization")
        ilo_tex.align_on_border(UP + LEFT)
        ax = Axes(x_range=[0, 10])[0]
        ax.align_on_border(LEFT + DOWN)

        layers = []
        arrows = []
        texts = []
        for index in range(num_layers):
            layers.append(Rectangle(width=gen_width, height=1.4**(index + 1)))
            if index != 0:
                layers[-1].next_to(layers[index - 1], layers_dist * RIGHT)
                text = MathTex(r"z_{}".format(index)).next_to(layers[-1], DOWN)
                arrow_up, arrow_down = connect_shapes(layers[-2], layers[-1], 
                    color=gen_color)
                arrows.append(arrow_up)
                arrows.append(arrow_down)
                gen_text = MathTex(r"G_{}".format(index), color=gen_color)
                gen_text.next_to(layers[-2], 2 * RIGHT)
                self.add(layers[-1],
                    arrow_up, arrow_down,
                    text, gen_text)
                texts.append(gen_text)
                texts.append(text)
            else:
                layers[0].align_on_border(LEFT).shift(1.8 * UP)
                first_text = MathTex(r"z_{}".format(index)).next_to(layers[-1], DOWN)
                self.add(layers[0], first_text)
                texts.append(first_text)
        generator = VGroup(*layers, *texts, *arrows)

        loss = MathTex(r"\left|\left|G_2G_1(z_1) - x\right|\right|^2")
        loss_rec = Rectangle(height=loss_height, width=loss_width, color=loss_color)
        loss_rec.next_to(0.5 * layers[1].get_center() + 
            0.5 * layers[2].get_center(), 12 * DOWN + 0.25 * RIGHT)
        loss.move_to(loss_rec.get_center())


        # smooth connections
        dot1 = Dot()
        dot1.next_to(layers[-1], 10 * RIGHT)
        x_text = MathTex(r"x")
        x_text.next_to(dot1, UP)

        x_image = ImageMobject("images/alex_real.png", scale_to_resolution=1.00 * image_resolution)
        x_image.next_to(x_text, RIGHT)

        dot2 = Dot()
        dot2.next_to(dot1, 12 * DOWN)
        dot2.set_y(loss_rec.get_center()[1])

        dot3 = Dot()
        dot3 = dot3.next_to(dot2, LEFT)
        rec_right_x = (0.5 * loss_rec.get_corner(RIGHT + UP) + 0.5 * loss_rec.get_corner(DOWN + RIGHT))[0]
        dot3.set_x(rec_right_x)



        n_arrows = []
        things_to_connect = [layers[-1].get_center(), dot1, dot2, dot3]
        for index in range(0, len(things_to_connect) - 1):
            n_arrows.append(Arrow(start=things_to_connect[index], 
                end=things_to_connect[index + 1]))
        
        dot4 = Dot()
        dot4.next_to(loss_rec, LEFT)
        rec_left_x = (0.5 * loss_rec.get_corner(LEFT + UP) + 0.5 * loss_rec.get_corner(DOWN + LEFT))[0]
        dot4.set_x(rec_left_x)
        
        dot5 = Dot()
        dot5.next_to(dot4, LEFT)
        dot5.set_x(texts[2].get_center()[0])

        n_arrows.append(Arrow(start=dot4, end=dot5))
        n_arrows.append(Arrow(start=dot5, end=texts[2]))


        scene_components = [loss, loss_rec, dot1, dot2, dot3, dot4, dot5, *n_arrows, x_text, x_image]
        n_mobj = Group(generator, *scene_components)        


        self.play(FadeOut(mobj), FadeIn(n_mobj))
        self.wait()
        self.endSlide()

        mobj = n_mobj
        factor = 0.5
        new_width = mobj.width * factor
        new_height = mobj.height * factor
        self.play(
            mobj.animate.stretch_to_fit_height(
                new_height).stretch_to_fit_width(
                    new_width).align_on_border(UP + LEFT))
        self.wait()
        self.endSlide()

        rec_text = MathTex(r"G_2G_1(z_1*)", color=YELLOW)
        rec_image = ImageMobject("images/alex_fake.png", scale_to_resolution=1.5 * image_resolution)
        rec_image.move_to(np.array([2., 0., 0.]))
        rec_text.next_to(rec_image, DOWN)
        self.play(FadeIn(rec_image), FadeIn(rec_text))
        self.wait()
        self.endSlide()
        # self.wait()


class Regularization(PPTXScene):
    def construct(self):
        text = Tex(r"The issue of regularization", color=YELLOW)
        text.align_on_border(UP + LEFT)

        image1 = ImageMobject("images/alex_inp.png", scale_to_resolution=0.5 * image_resolution)
        image1.move_to(np.array([-2.0, 0.0, 0.0]))
        self.play(FadeIn(text), FadeIn(image1))
        self.wait()
        self.endSlide()
        
        image2 = ImageMobject("images/alex_inp_failure.png", scale_to_resolution=0.5 * image_resolution)
        image2.move_to(np.array([2.0, 0.0, 0.0]))
        self.play(FadeIn(image2))
        self.wait()
        self.endSlide()
        
class SGILO(PPTXScene):
    def construct(self):
        ilo_tex = Tex(r"Score Guided Intermediate Layer Optimization")
        ilo_tex.align_on_border(UP + LEFT)
        ax = Axes(x_range=[0, 10])[0]
        ax.align_on_border(LEFT + DOWN)

        layers = []
        arrows = []
        texts = []
        for index in range(num_layers):
            layers.append(Rectangle(width=gen_width, height=1.4**(index + 1)))
            if index != 0:
                layers[-1].next_to(layers[index - 1], layers_dist * RIGHT)
                text = MathTex(r"z_{}".format(index)).next_to(layers[-1], DOWN)
                arrow_up, arrow_down = connect_shapes(layers[-2], layers[-1], 
                    color=gen_color)
                arrows.append(arrow_up)
                arrows.append(arrow_down)
                gen_text = MathTex(r"G_{}".format(index), color=gen_color)
                gen_text.next_to(layers[-2], 2 * RIGHT)
                self.add(layers[-1],
                    arrow_up, arrow_down,
                    text, gen_text)
                texts.append(gen_text)
                texts.append(text)
            else:
                layers[0].align_on_border(LEFT).shift(1.8 * UP)
                first_text = MathTex(r"z_{}".format(index)).next_to(layers[-1], DOWN)
                self.add(layers[0], first_text)
                texts.append(first_text)
        generator = VGroup(*layers, *texts, *arrows)

        loss = MathTex(r"\left|\left|G_2G_1(z_1) - x\right|\right|^2 + \\ - \lambda \log p_{\theta}(z_1)")
        loss_rec = Rectangle(height=loss_height, width=1.2 * loss_width, color=loss_color)
        loss_rec.next_to(0.5 * layers[1].get_center() + 
            0.5 * layers[2].get_center(), 12 * DOWN + 0.25 * RIGHT)
        loss.move_to(loss_rec.get_center())


        # smooth connections
        dot1 = Dot()
        dot1.next_to(layers[-1], 10 * RIGHT)
        x_text = MathTex(r"x")
        x_text.next_to(dot1, UP)

        x_image = ImageMobject("images/alex_inp.png", scale_to_resolution=1.00 * image_resolution)
        x_image.next_to(x_text, RIGHT)

        dot2 = Dot()
        dot2.next_to(dot1, 12 * DOWN)
        dot2.set_y(loss_rec.get_center()[1])

        dot3 = Dot()
        dot3 = dot3.next_to(dot2, LEFT)
        rec_right_x = (0.5 * loss_rec.get_corner(RIGHT + UP) + 0.5 * loss_rec.get_corner(DOWN + RIGHT))[0]
        dot3.set_x(rec_right_x)



        n_arrows = []
        things_to_connect = [layers[-1].get_center(), dot1, dot2, dot3]
        for index in range(0, len(things_to_connect) - 1):
            n_arrows.append(Arrow(start=things_to_connect[index], 
                end=things_to_connect[index + 1]))
        
        dot4 = Dot()
        dot4.next_to(loss_rec, LEFT)
        rec_left_x = (0.5 * loss_rec.get_corner(LEFT + UP) + 0.5 * loss_rec.get_corner(DOWN + LEFT))[0]
        dot4.set_x(rec_left_x)
        
        dot5 = Dot()
        dot5.next_to(dot4, LEFT)
        dot5.set_x(texts[2].get_center()[0])

        n_arrows.append(Arrow(start=dot4, end=dot5))
        n_arrows.append(Arrow(start=dot5, end=texts[2]))


        scene_components = [loss, loss_rec, dot1, dot2, dot3, dot4, dot5, *n_arrows, x_text, x_image]
        mobj = Group(generator, *scene_components)
        self.play(FadeIn(mobj))  
        self.wait()
        self.endSlide()


class Results(PPTXScene):
    def construct(self):
        text = Tex(r"Results", color=YELLOW)
        text.align_on_border(UP + LEFT)
        
        image1 = ImageMobject("images/posterior.png", scale_to_resolution=0.5 * image_resolution)
        image1.move_to(np.array([-2.0, 0.0, 0.0]))
        text1 = Tex(r"Super-resolution with posterior sampling", font_size=30)
        text1.next_to(image1, DOWN)
        self.play(FadeIn(text), FadeIn(image1), FadeIn(text1))
        self.wait()
        group1 = Group(image1, text1)
        self.endSlide()


        self.play(group1.animate.stretch_to_fit_height(
                group1.height * 0.5).stretch_to_fit_width(
                    group1.width * 0.5).next_to(text, DOWN + 2 * RIGHT))
        self.wait()
        self.endSlide()

        image2 = ImageMobject("images/ilo_inp.png", scale_to_resolution=1.6 * image_resolution)
        image2.next_to(image1, RIGHT)
        text2 = Tex(r"Inpainting", font_size=30)
        text2.next_to(image2, DOWN)
        self.play(FadeIn(image2), FadeIn(text2))
        self.wait()
        group2 = Group(image2, text2)
        self.endSlide()

        image3 = ImageMobject("images/frog.png", scale_to_resolution=1.3 * image_resolution)
        image3.next_to(image2, 5 * DOWN + LEFT)
        text3 = Tex(r"Converting humans to frogs", font_size=30)
        text3.next_to(image3, DOWN)
        self.play(FadeIn(image3), FadeIn(text3))
        self.wait()
        group3 = Group(image3, text3)
        self.endSlide()   


slides = [
    Intro,
    Pandas,
    Problem,
    Generator,
    CSGM,
    Regularization,
    SGILO,
    Results,
]


class Slides(*slides):

    def setup(self):
        # setup each scene
        for s in slides:
            s.setup(self)

    def construct(self):
        # play each scene
        for s in slides:
            s.construct(self)
            # if there are any objects left at the end of the animation, remove them!
            if len(self.mobjects) >= 1:
                self.remove(*self.mobjects)