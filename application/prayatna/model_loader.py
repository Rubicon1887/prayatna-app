import pandas as pd
import numpy as np
import os
from geopy.geocoders import Nominatim
from contextlib import suppress
import math
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.callbacks import CSVLogger


wheat = tf.keras.models.load_model('wheat_model')
rice = tf.keras.models.load_model('rice_model')
bajra = tf.keras.models.load_model('bajra_model')


def predict_wheat_model(market, date, month, year):
  address=market.split('(')[0]
  geolocator = Nominatim(user_agent="Your_Name")
  try:
    location = geolocator.geocode(address)
    lat=location.latitude
    longi=location.longitude
  except:
    lat = 4.5
    longi= 5.5

  wheat_df = pd.read_csv('wheat_final.csv')
  X=wheat_df[['Latitude','Longitude','Date','Month','Year']].values
  Y=wheat_df[['Min Price','Max Price','Modal Price']].values
  X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.05,random_state=26)
  sc=StandardScaler()
  sc.fit(X_train)
  dummy=np.array([[ lat, longi, date, month, year]])
  dummy= sc.transform(dummy)
  ans = wheat.predict(dummy)
  print(ans)
  mini, maxi, mod = ans[0]
  return mini, maxi, mod

def predict_rice_model(market, date, month, year):
  address=market.split('(')[0]
  geolocator = Nominatim(user_agent="Your_Name")
  location = geolocator.geocode(address)
  lat=location.latitude
  longi=location.longitude

  rice_df = pd.read_csv('rice_final.csv')
  X=rice_df[['Latitude','Longitude','Date','Month','Year']].values
  Y=rice_df[['Min Price','Max Price','Modal Price']].values
  X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.05,random_state=26)
  sc=StandardScaler()
  sc.fit(X_train)
  dummy=np.array([[ lat, longi, date, month, year]])
  dummy= sc.transform(dummy)
  ans = rice.predict(dummy)
  print(ans)
  mini, maxi, mod = ans[0]
  return mini, maxi, mod

def predict_bajra_model(market, date, month, year):
  address=market.split('(')[0]
  geolocator = Nominatim(user_agent="Your_Name")
  location = geolocator.geocode(address)
  lat=location.latitude
  longi=location.longitude

  bajra_df = pd.read_csv('bajra_final.csv')
  X=bajra_df[['Latitude','Longitude','Date','Month','Year']].values
  Y=bajra_df[['Min Price','Max Price','Modal Price']].values
  X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.05,random_state=26)
  sc=StandardScaler()
  sc.fit(X_train)
  dummy=np.array([[ lat, longi, date, month, year]])
  dummy= sc.transform(dummy)
  ans = bajra.predict(dummy)
  print(ans)
  mini, maxi, mod = ans[0]
  return mini, maxi, mod

if __name__ =='__main__':
  predict_wheat_model('Jajpur',6,9,12)
  # predict_rice_model()
  predict_bajra_model('Najafgarh',16, 12, 19)