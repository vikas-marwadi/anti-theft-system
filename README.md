# Anti-Theft-System
System will detect the intruder in shop or home and send the alert notification to owner with intruder photos

# Implementation
We created some portions of project in windows and some portion in Raspberry-Pi

All the training related work was done in windows the reason for that is the raspberry-pi takes much time then windows and get hot after some amount of time. so, we prefered that the training and testing part done in windows and after all complate we directly deploy it in Raspberry-Pi.

## For Windows Part

Step 1: Install required dataset and labeling them using LabelImg which is one python framework for converting images to labels.
Step 2: Install model-master folder which is nothing but Object-Detection API for train the model to predict the intruder.
Step 3: Generate the tfrecord file which having the all images with their perticular portion which we was selected in LabelImg software.
Step 4: Train the model.
Step 5: Generate .pb model but as we run the our project in raspberry-pi we required .tflite file or model which is faster then .pb model so we have to convert .pb to .tflite.

So, till now we complate all work in windows and now we have jump into raspberry-pi OS.

## For Raspberry-Pi Part

Step 1: Install raspios-buster from official site of raspberry-pi.

before we move on next step we must have hardwares: raspberry-pi model 3, pi camera (5MP), ethernet cable, 16GB SD card, Card Reader

Step 2: Now, if sd card not empty then we have to format it and then install **Raspbery Pi Imager** in windows and then make sd card as bootable by selecting sd card and raspi-buster.

before moving step 3 we have to install **putty** and **vnc player** for accessing raspi-os remotely. 

Step 3: Insert sd card into raspi board and connect the ethernet with pi to windows and power up the pi.
Step 4: Launch Putty and write in hostname **raspberrypi.local** and click on open.
Step 5: It will open the terminal emulater and it asked for password by default password is raspberry and later if you wish to change then you can change.
Step 6: After succesffuly logged in write command **sudo raspi-config** which will open the GUI based screen and we have to select the interface option and then select vnc and start the vnc by clicking on that.
Step 7: Launch vnc player and write server address as **raspberrypi.local** and hit enter will ask password, enter the password you will successfully done with installtion part.
Step 8: Then create virtual environment in raspi and run .bash file which is available in my repo.
Step 9: And you done now you just write the python code for detecting person and model we already have from windows.
Step 10: In our project we make raspi as auto launch the system at the booting time, means we not need to required every time to connect ethernet and then connect vnc like that stuff. we simply give power up to raspi-board and it will automatically start the system.  
