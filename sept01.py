from lib2 import *
from sphere import *
from math import pi, tan
from materials import *

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)


class Raytracer(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.scene = []
    self.clear()

  def clear(self):
    self.pixels = [
      [BLACK for x in range(self.width)]
      for y in range(self.height)
    ]

  def write(self, filename):
  	writebmp(filename, self.width, self.height, self.pixels)

  def display(self, filename='out.bmp'):
  	self.render()
  	self.write(filename)

  def point(self, x, y, c = None):
    try:
      self.pixels[y][x] = c or self.current_color
    except:
      pass

  def scene_intersect(self, orig, direction):
  	for obj in self.scene:
  		if obj.ray_intersect(orig, direction):
  			return obj.material
  	return None

  def cast_ray(self, orig, direction):
  	#esta funcion devuelve un color gracias al rayo
  	impacted_material = self.scene_intersect(orig, direction)
  	if impacted_material:
  		return impacted_material.diffuse
  	else:
  		return color(0, 0, 0)

  """def cast_ray(self, orig, direction, sphere):
    if sphere.ray_intersect(orig, direction):
      return color(255, 0, 0)
    else:
      return color(0, 0, 255)"""

  def render(self):
    alfa = int(pi/2)
    for y in range(self.height):
      for x in range(self.width):
        i =  (2*(x + 0.5)/self.width - 1)*self.width/self.height*tan(alfa/2)
        j =  (1 - 2*(y + 0.5)/self.height)*tan(alfa/2)
        # x = int(x)
        # y = int(y)
        # print(x, y)
        direction = norm(V3(i, j, -1))
        self.pixels[y][x] = self.cast_ray(V3(0,0,0), direction)

  """def basicRender(self):
  #Esto llena la pantalla de un color degradado
    for x in range(self.width):
      for y in range(self.height):
        r = int((x/self.width)*255) if x/self.width < 1 else 1
        g = int((y/self.height)*255) if y/self.height < 1 else 1
        b = 0
        self.pixels[y][x] = color(r, g, b)"""

r = Raytracer(1000, 1000)
r.scene = [
	Sphere(V3(0,-1.5,-10), 1.5, ivory),
    Sphere(V3(2,-1,-12), 2, snow)
]
#s = Sphere(V3(0, 0, -16), 2)
#r.render()
r.display()