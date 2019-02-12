# MicroPython ST7735 TFT display driver example usage

from machine import Pin, SPI
from ESP8266Libraries.ST7735 import Display
from ESP8266Libraries.ST7735 import Fonts
from ESP8266Libraries.Widgets import Gauges
from ESP8266Libraries.Widgets import Diagnostics
from ESP8266Libraries.ConfigReader import ConfigReader
from ESP8266Libraries.ConnectionHandler import WifiController
from ESP8266Libraries.ConnectionHandler import ServerController

import utime
import dht
import urequests

import gc

gc.enable()

print( b'--- Startup ---')
print( b'Starting up LCD' )

oTFT = Display.TFT( 128, 160, 1, 4, 2, 5, None, Display.ORIENTATION_PORTRAIT2 )
oLogger = Diagnostics.TFTStatusLogger( oTFT )
oLogger.init()

oLogger.LogTaskStart( "LCD" )
oLogger.LogTaskResult( True ) # yep, im dead serious

oLogger.LogTaskStart( "CONFIG" )
oConfigReader = ConfigReader.ConfigReader()
oLogger.LogTaskResult( oConfigReader.init() )

oLogger.LogTaskStart( "WIFI" )
oNetworkController = WifiController.WifiController()
oLogger.LogTaskResult( oNetworkController.init() )

oLogger.LogTaskStart( "CONNECTION" )
oNetworkController.ConnectToWifi( *oConfigReader.GetWifiConfig() )
oLogger.LogTaskResult( oNetworkController.IsConnected() )

oLogger.LogTaskStart( "SERVER" )
oServerController = ServerController.ServerController()
oLogger.LogTaskResult( oServerController.init( *oConfigReader.GetServerConfig() ) )

#d = dht.DHT22(Pin(10))
#measures = 0
# while( True ):
#
#     d.measure()
#     temp = d.temperature()
#     hum = d.humidity()
#     measures +=1
#
#     #oTFT.clear(oTFT.rgbcolor(0, 0, 0))
#     #tft.text(0,0,"Temp: " + str(temp) + "°C", font.terminalfont, tft.rgbcolor(255, 255, 255), 2)
#     #tft.text(0,24,"Hum: " + str(hum) + "%" , font.terminalfont, tft.rgbcolor(255, 255, 255), 2)
#     #tft.text(0,48,"Ticks: " + str(measures) , font.terminalfont, tft.rgbcolor(255, 255, 255), 2)
#
#     print( "Tick: " + str( measures) + " , Temp: " + str( temp ))
#
#     oThermometer.SetTemperature( temp )
#
#     utime.sleep(5)
