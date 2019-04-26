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
    #due to mOne failing, mTwo is effectively the only functioning GPIO.
    global mOne
    mOne = gpio.PWM(18,1000)
    global mTwo
    mTwo = gpio.PWM(17,1000)
    mOne.start(2.9)
    mTwo.start(2.88)
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
        #ChangeDutyCycle changed the % Duty Cycle output by the raspberry pi
        if msg==1:
            mOne.ChangeDutyCycle(2.25)
            mTwo.ChangeDutyCycle(3.3)
        elif msg==2:
            mOne.ChangeDutyCycle(2.6)
            mTwo.ChangeDutyCycle(3.1)
        elif msg==3:
            mOne.ChangeDutyCycle(2.88)
            mTwo.ChangeDutyCycle(2.88)
        elif msg==4:
            mOne.ChangeDutyCycle(3.2)
            mTwo.ChangeDutyCycle(2.6)
        elif msg==5:
            mOne.ChangeDutyCycle(3.5)
            mTwo.ChangeDutyCycle(2.25)
        else:
            print("?")
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

