#Import essential modules
import paho.mqtt.client as mqtt
import RPi.GPIO as gpio

#Set up RPI GPIO pins
def gpioSetup():
    
    #Set pin numbering to Broadcom scheme
    gpio.setmode(gpio.BCM)
    #Set PWM GPIOS for the motor controller
    gpio.setup(18, gpio.OUT)
    gpio.setup(17, gpio.OUT)
    global mOne
    mOne = gpio.PWM(18,1000)
    global mTwo
    mTwo = gpio.PWM(17,1000)
    mOne.start(0)
    mTwo.start(0)
#Execute when a connection has been established ot the MQTT server
def connectionStatus(client, userdata, flags, rc):
    #Subscribe client to a topic
    mqttClient.subscribe("rpi/servo")

#Execute when a message has been received from the MQTT server
def messageDecoder(client, userdata, msg):
        #Decode message
        message = msg.payload.decode(encoding='UTF-8')
        msg = int(message)
        print(msg)
        mOne.ChangeDutyCycle(msg)
        mTwo.ChangeDutyCycle(msg)
#Set up RPI GPIO pins
gpioSetup()

#set client name
clientName = "RPISpeed"

#Set MQTT server address
serverAddress = "169.254.213.44"

#Instantiate Eclipse Paho as mqttClient
mqttClient = mqtt.Client(clientName)

#Set calling functions to mqttCLient
mqttClient.on_connect = connectionStatus
mqttClient.on_message = messageDecoder

#Connect client to Server
mqttClient.connect(serverAddress)

#Monitor client activity forever
mqttClient.loop_forever()

