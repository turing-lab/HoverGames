# Galileo University Proposal for HoverGames Challenge 
**Elevator pitch:** The approach of Turing Lab at Galileo University proposes the use of drones to help firefighters in setting landmarks of clusters of people to create a dynamic map that indicates the dimensions of the fire and the location of the groups of people in danger.

## Modules description
### Lepton Module
This is a modified package of the Lepton repository from Groupgets that makes it possible to interface the IR camera with the Raspberry Pi 3. Our module can take screenshots of the IR image and receive the thermal signal with a shutterless lens.

### Stream 
This module contains a script that sends a video feed from the usb camera attached to the Raspberry Pi over UDP. The python script receives the video signal into the main computer using OpenCV functions. Currently we are using a conventional router to stream the video with a range of approximately 100m. This limitation will be enhanced by getting a more robust transmiter. 

### YOLOv3
Here a custom version of YOLOv3 was adapted to detect people, animals and cars. These are the main features intended to be found in the map, which will be used by the rescue teams to locate survivors and assess the fire status.

### ROS
At the Turing Lab, we are great enthusiasts of ROS, so for this project we made extensive use of the MAVROS and MAPVIZ packages. MavRos enabled us to communicate with the drone using Mavlkink messages that provide all the information we needed from the drone sensors. 
MapViz is a GPS visual interface that enabled us to generate maps, routes and point positions on a global localization enviroment. 

## Bill of materials
Aditional to the NXP Drone Kit, our team added some components to the system.

| Descriptión                   | Price   |
|-------------------------------|--------:|
| 4200mAh Li-Po Battery         | $31.99  |
| 1200mAh Li-On Battery         | $21.00  |
| USB Logitech Web Camera       | $20.00  |
| Flir Lepton Thermal camera    | $239.95 |
| Raspberry Pi 3                | $35.00  |
| 3A Step-down DC-DC Converter  | $5.00   |
| Router                        | $60.00  |

## Video and Photos
### Flight Demo
<a href="http://www.youtube.com/watch?feature=player_embedded&v=teqXtwTc360" target="_blank">
  <img src="http://img.youtube.com/vi/teqXtwTc360/0.jpg" 
    alt="Flight Demo" width="240" height="180" border="10" />
</a>

### YOLO Demo
<a href="http://www.youtube.com/watch?feature=player_embedded&v=-Jbw3nPCIjI" target="_blank">
  <img src="http://img.youtube.com/vi/-Jbw3nPCIjI/0.jpg" 
    alt=" Yolo Demo" width="240" height="180" border="10" />
</a>

### Thermal Camera Demo
<a href="http://www.youtube.com/watch?feature=player_embedded&v=BC_lhx5vdAs" target="_blank">
  <img src="http://img.youtube.com/vi/BC_lhx5vdAs/0.jpg" 
    alt="Thermal Camera Demo" width="240" height="180" border="10" />
</a>

### Mapviz Screenshot
![mapviz-screenshot](assets/mapviz-screenshot.jpg?raw=true)
Mapviz is used as a visualization tool to show the drone location in a map (provided by the Bing Maps API) using the GPS information. The trajectory of the drone is drawn in the map using a red line. The video that is being captured from the camera that is mounted on the drone is displayed in the top left corner.
We are currently working on adding people, animals and other objects in the map as markers, and also adding the information from the thermal camera as a heat map to help the rescue teams in their tasks.

## CAD Files
To equip the drone with the additional gear for our project, some 3D printed parts were necessary, which we made available in the following GrabCad folder.
[Galileo Hovergames GrabCad](https://grabcad.com/library/hovergames-galileo-1)


![cameraholder](https://github.com/turing-lab/HoverGames/blob/master/assets/cameraholder.JPG)
![raspyholder](https://github.com/turing-lab/HoverGames/blob/master/assets/raspyholder.JPG)
