# ThereMyn
ThereMyn is a digital synthesizer meant to act as an easier, software based version of a ![theremin](https://www.youtube.com/watch?v=ajM4vYCZMZk), and was built for the Spring 2019 15-112 Term Project (@ CMU). Beyond the traditional aspects of a theremin (motion-based pitch control), ThereMyn includes customizable waveforms and fixed harmonizations, as well as loop functionality. 

Though meant to be played with an ultrasonic sensor hooked up to an Arduino Leonardo, ThereMyn can be demoed using the number keys 1-8 to produce pitches. ThereMyn is built in python 2.7 using pyfirmata (for interfacing with the arduino) and pyo (for digital signal processing). ThereMyn won 2nd place at the Spring 2019 15-112 Term Project Showcase.

## Required Modules
* Pyo
* Pyfirmata
* Threading

## Required Hardware
* Arduino Leonardo
* ultrasonic sensor
* Arduino pins
