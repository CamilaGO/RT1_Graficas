from lib import color

class Material(object):
  def __init__(self, diffuse):
    self.diffuse = diffuse



ivory = Material(diffuse=color(100, 100, 80))
rubber = Material(diffuse=color(80, 10, 0))
snow = Material(diffuse=color(200, 200, 200))