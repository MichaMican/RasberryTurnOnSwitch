# RasberryTurnOnSwitch
  
## What it does:
These two Scripts (run.py and currentStatus.py) create a website to turn a computer on and off from the distance via the internet. 
**run.py** handles the website and the intputs of the user and turns the computer on (GPIO 16)  
**currentStatus.py** checks the actual status of the computer (via the on/off LED of the computer (GPIO 15)) and syncs it if necessary with the website.
  
## WARNING
There is no secure authentication implemented! This should only be used in a closed network. If you realy want to use this on the web please implement your own secureing of the website (e.g. VPN tunel, 3rd party authentication etc.)
  
## How to setup:

### Installation:
_This Guide is based on Raspbian_  
Open Terminal and run:  
``git clone https://github.com/MichaMican/RaspberryTurnOnSwitch.git``  
``pip3 install flask``   
``pip3 install flask_cors``  

### Connection:  
![circuit diagram](https://i.imgur.com/lRkw57g.png)



