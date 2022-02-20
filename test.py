from modular.PS4Controller import MyController

if __name__ == '__main__':
    controller = MyController(
        interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()
