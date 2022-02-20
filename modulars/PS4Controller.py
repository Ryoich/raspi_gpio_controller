from .raspberrypi_gpio import My_Raspi_GPIO_Controller
from pyPS4Controller.controller import Controller

class MyController(Controller, My_Raspi_GPIO_Controller):
    
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    def on_x_press(self):
        self.go_forward()

    def on_x_press(self):
        self.stop()

