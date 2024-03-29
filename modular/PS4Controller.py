from raspberrypi_gpio import My_Raspi_GPIO_Controller
from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.raspi_gpio = My_Raspi_GPIO_Controller()
        self.state

    def on_x_press(self):
        print("Now I press the x button")
        self.raspi_gpio.go_forward()

    def on_x_release(self):
        print("Now I release the x button")
        self.raspi_gpio.stop()
    
    def on_circle_press(self):
        print("Now I press the o button")
        self.raspi_gpio.go_backward()

    def on_circle_release(self):
        print("Now I release the o button")
        self.raspi_gpio.stop()

    def on_triangle_press(self):
        print("Now I press the ^ button")
        self.raspi_gpio.turn_right()
    

    def on_triangle_release(self):
        print("Now I release the ^ button")
        self.raspi_gpio.stop()

    def on_L1_press(self):
        print("Now I press the L1 button")
        self.raspi_gpio.turn_left()
    

    def on_L1_release(self):
        print("Now I release the L1 button")
        self.raspi_gpio.stop()
