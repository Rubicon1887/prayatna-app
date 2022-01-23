import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.factory import Factory
import datepicker_good as dp

from model_loader import *
from data_values import *

from kivy.config import Config
  
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)

class Display(GridLayout):
    pass

# class DatePicker(BoxLayout):
#   def getCalValue(self, picked):
#       global day,month,year
#       day = self.picked[0]
#       month = self.month
#       year = self.year
#       if(hasattr(self, 'pop')):
#         self.pop.dismiss()
#         print(day,month,year)



class Screen_Model(Screen):
    crop_name = StringProperty(None)
    spinner_state = ObjectProperty(None)
    spinner_district = ObjectProperty(None)
    spinner_market = ObjectProperty(None)
    max_price = ObjectProperty(None)
    min_price = ObjectProperty(None)
    mod_price = ObjectProperty(None)
    date_btn = ObjectProperty(None)
    
    def __init__(self, touch_switch=False, *args, **kwargs):
        super(Screen_Model, self).__init__(*args, **kwargs)
        self.day, self.month, self.year = 0,0,0
        # self.init_ui() 
    
    def getDate(self):
      self.dpicker = dp.DatePicker()
      popup = Popup(auto_dismiss= True,content=self.dpicker , title= "Select Date", size_hint= (None, None), size= (600,600))
      popup.bind(on_dismiss=self.changeDate)
      popup.open()
      print(self.dpicker)
      print(self.date_btn.text)

    def changeDate(self,instance):

      time = self.dpicker.text
      print(time)
      self.date_btn.text = time
      if(time!=None and time!=''):
        self.day, self.month, self.year = time.split('-')
        self.day, self.month, self.year = int(self.day), int(self.month), int(self.year)

    def spinner_state_clicked(self, value):
        print("State selected is " + value)
        self.spinner_state.text = value
        if(value!='Select State' and self.crop_name!=None):
          if self.crop_name == "[b]WHEAT[/b]":
            self.spinner_district.values = wheat_district_dict[value]
            self.spinner_market.values = wheat_market_dict[value]
          elif self.crop_name == "[b]RICE[/b]":
            self.spinner_district.values = rice_district_dict[value]
            self.spinner_market.values = rice_market_dict[value]
          elif self.crop_name == "[b]BAJRA[/b]":
            self.spinner_district.values = bajra_district_dict[value]
            self.spinner_market.values = bajra_market_dict[value]
    
    def spinner_district_clicked(self, value):
        print("District selected is " + value)
        self.spinner_district.text = value

    def spinner_market_clicked(self, value):
        print("Market selected is " + value)
        self.spinner_market.text = value

    def btn(self):
      crop_name = 'WHEAT'  # [m]
      print(self.crop_name, self.spinner_state.text, self.spinner_district.text, self.spinner_market.text, self.day, self.month, self.year, self.min_price.text,self.mod_price.text, self.max_price.text)
      if (self.crop_name != None) and (self.spinner_state.text != 'Select State') and (self.spinner_district.text != 'Select District') and (self.spinner_market.text != 'Select Market') and self.day != 0 and self.month!=0 and self.year != 0:
          print(self.crop_name, self.spinner_state.text, self.spinner_district.text, self.spinner_market.text, self.min_price.text,self.mod_price.text, self.max_price.text)
          if self.crop_name == "[b]WHEAT[/b]":
            min_price, max_price, mod_price = predict_wheat_model(self.spinner_market.text, self.day, self.month, self.year%2000)
            self.min_price.text, self.max_price.text, self.mod_price.text =str(min_price), str(max_price), str(mod_price)
          elif self.crop_name == "[b]RICE[/b]":
            min_price, max_price, mod_price = predict_rice_model(self.spinner_market.text, self.day, self.month, self.year%2000)
            self.min_price.text, self.max_price.text, self.mod_price.text =str(min_price), str(max_price), str(mod_price)
          elif self.crop_name == "[b]BAJRA[/b]":
            min_price, max_price, mod_price = predict_bajra_model(self.spinner_market.text, self.day, self.month, self.year%2000)
            self.min_price.text, self.max_price.text, self.mod_price.text =str(min_price), str(max_price), str(mod_price)
      else:
        popText = 'Invalid Input'
        if (self.crop_name == None):
          popText='Invalid Crop'
        elif (self.spinner_state.text == 'Select State'):
          popText='Invalid State'
        elif (self.spinner_district.text == 'Select District'):
          popText='Invalid District'
        elif (self.spinner_market.text == 'Select Market'):
          popText='Invalid Market'
        elif self.day != 0 and self.month!=0 and self.year != 0:
          popText='Invalid Date'
          
        popup = Popup(title="Invalid Input", content=Factory.Label(text=popText),size_hint=(None, None), size=(400, 400))
        popup.open()

      #Intialising to ''
      # self.crop_name.text = '' 
      # self.spinner_state.text = 'Select State' 
      # self.spinner_district.text = 'Select District'  
      # self.spinner_market.text = 'Select Market' 
      # self.min_price.text = ''
      # self.max_price.text = ''

class Screen_One(Screen_Model):
  pass

class Screen_Two(Screen_Model):
  pass

class Screen_Three(Screen_Model):
  pass

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

    # def getDate(self):
    #   popup = DatePopup()
    #   popup.bind(on_dismiss=self.changeDate)
    #   popup.open()
    #   self.dpicker = popup.DatePicker
    #   print(self.dpicker)
    #   print(self.date_btn.text)