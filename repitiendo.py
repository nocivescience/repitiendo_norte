from manim import *
class RepeatingScene(Scene):
    def construct(self):
        color=[RED,YELLOW,GREEN,WHITE,BLUE_B]
        lista=[
            'codelco',
            'chuquicamanta',
            'Ag',
            'Au',
            'Cu',
            'codelco',
            'intoxicación',
            'metales',
            'pesados',
            'Ricardo',
            'bullying',
            'abusos',
            'd-54'
        ]
        positions=np.array([[
            np.random.uniform(-config['frame_width']/2,config['frame_width']/2),
            np.random.uniform(-config['frame_height']/2,config['frame_height']/2),
            0
        ] for _ in range(100) ])
        texts=VGroup()
        for pos in positions:
            element=lista[int(np.floor(np.random.random()*len(lista)))]
            texting=Tex(element).move_to(pos).scale(np.random.random()*2).set_color(color[int(np.floor(np.random.random()*len(color)))])
            texts.add(texting)
        self.play(LaggedStartMap(Write,texts),run_time=30)
        self.wait()