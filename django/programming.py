#07/04/2021  Duck typing
class Pycharm:
    def open(self):
        print("pycharm open")
    def run(self):
        print("pycharm run")
    def debug(self):
        print("pycharm debug")


class Vscod:
    def open(self):
        print("vscod open")
    def run(self):
        print("vscod run")
    def debug(self):
        print("vscod debug")





class Programmer:
    def coding(self,ide):
        ide.open()
        ide.run()
        ide.debug()
py=Pycharm()
vs=Vscod()
pr=Programmer()
pr.coding(vs)