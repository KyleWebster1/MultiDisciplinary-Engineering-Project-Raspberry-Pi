# MultiDisciplinary-Engineering-Project-Raspberry-Pi
This is the full compilation of the code on a Raspberry Pi to control an RC car
The forward.py program subscribes to the MQTT server as a gpio subscriber and activates the forward and backward enable pins.
The servo.py program subscribes to the MQTT server as a servo subscriber and controls the servo's angle depending on the input
The speedControl.py subscribes to the MQTT server as a speed subscriber and controls the motor driver's speed controls for each motor.
