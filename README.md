# Galileo University Proposal for HoverGames Challenge 
**Elevator pitch:** The approach of Turing Lab at Galileo University offers propose the use of drones to help firemen setting landmarks of clusters of people to create a dynamic map that indicates the dimensions of the fire and the location of the groups of persons that are in danger.

## Modules description
### Lepton Module
This is a modified package of the Lepton repository from Groupgets that makes it possible to interface the IR camera with the raspberry pi 3. Our module makes it possible to take screenshots of the IR image and receive the thermal signal with a shutterless lens.

### Stream 
This module contains a script that sends over UDP the video feed from the usb camera attached to the raspberry pi. The python script receives the video signal to the main computer using Opencv functions.

### Yolov3
Here a custom version of YoloV3 was adapted to detect persons, animals and cars. This are the main features intended to be inserted on to the map that will be used by the rescue teams that need to locate survivors and the fire status.

### ROS
In Turing Lab, we are great enthusiasts of using ROS and for this project we made use of the packages of MAVROS and MAPVIZ. MavRos gave us the opportunity to communicate with the drone using Mavlkink messages that provide all the information needed from the sensors of the drone. 
MapViz is a GPS visual interface that makes possible to generate maps, rutes and point positions on a global localization enviroment. 

## Bill of materials
Aditional to the NXP Drone kit our team add some components to the system.

| Descriptión                   | Price   |
|-------------------------------|--------:|
| 4200mAh Li-Po Battery         | $31.99  |
| 1200mAh Li-On Battery         | $21.00  |
| USB Logitech Web Camera       | $20.00  |
| Flir Lepton Thermal camera    | $239.95 |
| Raspberry Pi 3                | $35.00  |
| 3A Step-down DC-DC Converter  | $5.00   |

## Video and Photos
### Flight Demo
<a href="http://www.youtube.com/watch?feature=player_embedded&v=teqXtwTc360" target="_blank">
  <img src="http://img.youtube.com/vi/teqXtwTc360/0.jpg" 
    alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" />
</a>

