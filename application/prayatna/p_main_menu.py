import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup


from kivy.config import Config
  
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)

isDate = False
day = 0
month = 0
year = 0

class Display(GridLayout):
    pass

class DatePicker(BoxLayout):
  def getCalValue(self, picked):
      global day,month,year
      day = self.picked[0]
      month = self.month
      year = self.year
      isDate = True
      if(self.pop!=None):
        self.pop.dismiss()
        print(day,month,year)

class Screen_One(Screen):
    sx = ObjectProperty(None)
    sy = ObjectProperty(None)
    gx = ObjectProperty(None)
    sx = ObjectProperty(None)
    grid_size = ObjectProperty(None)
    robot_size = ObjectProperty(None)

    def getDate(self):
      dpicker = DatePicker()
      popup = Popup(title="Select Date", content=dpicker, size_hint=(None, None), size=(600,600))
      popup.open()
      dpicker.pop = popup

    def btn(self):
      sx = 10.0  # [m]
      sy = 10.0  # [m]
      gx = 50.0  # [m]
      gy = 50.0  # [m]
      grid_size = 2.0  # [m]
      robot_size = 1.0  # [m]
      if self.sx.text != '' and self.sx.text.isdigit():
        sx=int(self.sx.text)
      if self.sy.text != '' and self.sy.text.isdigit():
        sy=int(self.sy.text)
      if self.gx.text != '' and self.gx.text.isdigit():
        gx=int(self.gx.text)
      if self.gy.text != '' and self.gy.text.isdigit():
        gy=int(self.gy.text)
      if self.grid_size.text != '' and self.grid_size.text.isdigit():
        grid_size=int(self.grid_size.text) 
      if self.robot_size.text != '' and self.robot_size.text.isdigit():
        robot_size=int(self.robot_size.text) 
      print(sx, sy, gx, gy, grid_size, robot_size)
      print(day,year,month)
      # BFS.main(sx, sy, gx, gy, grid_size, robot_size)
      print(self.sx.text, self.sy.text, self.gx.text, self.gy.text, self.grid_size.text, self.robot_size.text)

      #Intialising to ''
      self.sx.text = '' 
      self.sy.text = '' 
      self.gx.text = '' 
      self.gy.text = '' 
      self.grid_size.text = '' 
      self.robot_size.text = ''


class Screen_Two(Screen):
    sx = ObjectProperty(None)
    sy = ObjectProperty(None)
    gx = ObjectProperty(None)
    sx = ObjectProperty(None)
    grid_size = ObjectProperty(None)
    robot_size = ObjectProperty(None)

    def getDate(self):
      dpicker = DatePicker()
      popup = Popup(title="Select Date", content=dpicker, size_hint=(None, None), size=(600,600))
      popup.open()
      dpicker.pop = popup

    def btn(self):
      sx = 10.0  # [m]
      sy = 10.0  # [m]
      gx = 50.0  # [m]
      gy = 50.0  # [m]
      grid_size = 2.0  # [m]
      robot_size = 1.0  # [m]
      if self.sx.text != '' and self.sx.text.isdigit():
        sx=int(self.sx.text)
      if self.sy.text != '' and self.sy.text.isdigit():
        sy=int(self.sy.text)
      if self.gx.text != '' and self.gx.text.isdigit():
        gx=int(self.gx.text)
      if self.gy.text != '' and self.gy.text.isdigit():
        gy=int(self.gy.text)
      if self.grid_size.text != '' and self.grid_size.text.isdigit():
        grid_size=int(self.grid_size.text) 
      if self.robot_size.text != '' and self.robot_size.text.isdigit():
        robot_size=int(self.robot_size.text) 
      print(sx, sy, gx, gy, grid_size, robot_size)
      # DFS.main(sx, sy, gx, gy, grid_size, robot_size)
      print(self.sx.text, self.sy.text, self.gx.text, self.gy.text, self.grid_size.text, self.robot_size.text)

      #Intialising to ''
      self.sx.text = '' 
      self.sy.text = '' 
      self.gx.text = '' 
      self.gy.text = '' 
      self.grid_size.text = '' 
      self.robot_size.text = ''

class Screen_Three(Screen):
    sx = ObjectProperty(None)
    sy = ObjectProperty(None)
    gx = ObjectProperty(None)
    sx = ObjectProperty(None)
    grid_size = ObjectProperty(None)
    robot_size = ObjectProperty(None)
    
    def getDate(self):
      dpicker = DatePicker()
      popup = Popup(title="Select Date", content=dpicker, size_hint=(None, None), size=(600,600))
      popup.open()
      dpicker.pop = popup

    
    def btn(self):
      sx = 10.0  # [m]
      sy = 10.0  # [m]
      gx = 50.0  # [m]
      gy = 50.0  # [m]
      grid_size = 2.0  # [m]
      robot_size = 1.0  # [m]
      if self.sx.text != '' and self.sx.text.isdigit():
        sx=int(self.sx.text)
      if self.sy.text != '' and self.sy.text.isdigit():
        sy=int(self.sy.text)
      if self.gx.text != '' and self.gx.text.isdigit():
        gx=int(self.gx.text)
      if self.gy.text != '' and self.gy.text.isdigit():
        gy=int(self.gy.text)
      if self.grid_size.text != '' and self.grid_size.text.isdigit():
        grid_size=int(self.grid_size.text) 
      if self.robot_size.text != '' and self.robot_size.text.isdigit():
        robot_size=int(self.robot_size.text) 
      print(sx, sy, gx, gy, grid_size, robot_size)
      # AStar.main(sx, sy, gx, gy, grid_size, robot_size)
      print(self.sx.text, self.sy.text, self.gx.text, self.gy.text, self.grid_size.text, self.robot_size.text)

      #Intialising to ''
      self.sx.text = '' 
      self.sy.text = '' 
      self.gx.text = '' 
      self.gy.text = '' 
      self.grid_size.text = '' 
      self.robot_size.text = ''

class PrayatnaApp(App):
  def build(self):
    return Display()
  
  def animate(self, instance):
      # create an animation object. This object could be stored
      # and reused each call or reused across different widgets.
      # += is a sequential step, while &= is in parallel
      animation = Animation(pos=(100, 100), t='out_bounce')
      animation += Animation(pos=(200, 100), t='out_bounce')
      animation &= Animation(size=(500, 500))
      animation += Animation(size=(100, 50))

      # apply the animation on the button, passed in the "instance" argument
      # Notice that default 'click' animation (changing the button
      # color while the mouse is down) is unchanged.
      animation.start(instance)

      # button = Button(size_hint=(None, None), text='plop',
      #                 on_press=self.animate)
      # return button

if __name__ =='__main__':
  PrayatnaApp().run()
  