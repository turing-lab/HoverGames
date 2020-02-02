# Galileo University Proposal for HoverGames challenge 
(Elevator Speach)
The aproach of Turing Lab at Galileo University offers propose the use of a drones to help firemen seting landmarks of clusters of people to create a dynamic map that indicates the dimentions of the fire and the location of the groups of persons that are in danger. 
## Modules desciption
### Lepton Module
This is a modified package of the Lepton repository from Groupgets that makes it posible to interface the IR camera with the raspberry pi 3. Our module makes it posible to take screenshots of the IR image and recive the thermal signal with a shutterless lens. 
### Stream 
This module contains a script that sends over UDP the video feed from the usb camera atached to the raspberry pi. The python script recives the video singal to the main computer using Opencv functions. 
### Yolov3
Here a costom version of YoloV3 was adapted to detect persons, animals and cars. This are the main features intended to be inserted on to the map that will be used by the recue teams that need to locate survivors and the fire status.
### ROS
In Turing Lab, we are great enthusiasts of using ROS and for this project we made use of the packeges of MAVROS and MAPVIZ. MavRos gave us the oportunity to comunicate with the drone using Mavlkink messages that provides all the information needed from the sensors of the drone. 
MapViz is a GPS visual interface that makes posible to generate maps, rutes and point positions on a global localizacion enviroment. 


## List of materials
Aditional to the NXP Drone kit out team add some components to the system. 
- 4200mAh Lipo Battery 
- 1200mAh Li-On Battery
- Usb Logitech web camera
- Flir Lepton Thermal camera
- Raspberry pi 3
- 3 Amps Step-down Dc Converter
## 
