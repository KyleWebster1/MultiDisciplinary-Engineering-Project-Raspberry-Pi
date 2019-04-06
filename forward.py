#Import essential modules
import paho.mqtt.client as mqtt
import RPi.GPIO as gpio

#Set up RPI GPIO pins
def gpioSetup():
    
    #Set pin numbering to Broadcom scheme
    gpio.setmode(gpio.BCM)
    
    #Set Forward GPIO pins as an output pin
    gpio.setup(21, gpio.OUT)
    gpio.setup(20, gpio.OUT)

    #Set Backward GPIO pins as an output pin
    gpio.setup(19, gpio.OUT)
    gpio.setup(26, gpio.OUT)

    #Set PWM GPIOS for the motor controller
    gpio.setup(13, gpio.OUT)
    gpio.setup(16, gpio.OUT)
    global mOne
    mOne  = gpio.PWM(13,50)
    global mTwo 
    mTwo = gpio.PWM(16,50)
    mOne.start(2.5)
    mTwo.start(2.5) 
#Execute when a connection has been established ot the MQTT server
def connectionStatus(client, userdata, flags, rc):
    #Subscribe client to a topic
    mqttClient.subscribe("rpi/gpio")

#Execute when a message has been received from the MQTT server
def messageDecoder(client, userdata, msg):
    #Decode message received from topic
    message = msg.payload.decode(encoding='UTF-8')
    if message =='for on':
        gpio.output(21, gpio.HIGH)
        gpio.output(20, gpio.HIGH)
        print("LED is ON!")
    elif message == "for off":
        gpio.output(21, gpio.LOW)
        gpio.output(20, gpio.LOW)
        print("LED is OFF!")
    elif message =="back on":
        gpio.output(19, gpio.HIGH)
        gpio.output(26, gpio.HIGH)
        print("LED IS ON!")
    elif message == "back off":
        gpio.output(19, gpio.LOW)
        gpio.output(26, gpio.LOW)
        print("LED IS OFF!")
    else:
        print(message)
        print("Unknown message!")
        
#Set up RPI GPIO pins
gpioSetup()

#set client name
clientName = "RPI"

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
