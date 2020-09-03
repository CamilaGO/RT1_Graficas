from lib import color

# ===============================================================
# Paula Camila Gonzalez Ortega - 18398
# ===============================================================

class Material(object):
  def __init__(self, diffuse):
    self.diffuse = diffuse



ivory = Material(diffuse=color(100, 100, 80))
rubber = Material(diffuse=color(80, 10, 0))
snow = Material(diffuse=color(200, 200, 200))
button = Material(diffuse=color(0, 0, 0))
eye = Material(diffuse=color(250, 250, 250))
carrot = Material(diffuse=color(255, 165, 0))