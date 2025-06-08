# 🍓 Raspberry Pi Projects Collection

A comprehensive collection of Raspberry Pi projects ranging from beginner-friendly tutorials to advanced IoT implementations. Each project includes detailed documentation, circuit diagrams, and complete source code.

## 🎯 About This Repository

This repository serves as a centralized hub for various Raspberry Pi projects that demonstrate different aspects of hardware interfacing, sensor integration, automation, and IoT development. Whether you're a beginner looking to learn the basics or an experienced developer seeking inspiration, you'll find projects suited to your skill level.

## 🚀 Featured Projects
### 🌡️ Sensor Projects
- [x] **[Temperature Monitor](./temp_sensor/)** 🟢 - Use a DHT11 sensor to read and display temperature & humidity on the terminal
- [ ] **[Motion Detector Alarm](./motion-detector/)** 🟢 - Use a PIR sensor to trigger a buzzer or LED when motion is detected
- [ ] **[Plant Health Monitor](./plant-monitor/)** 🟡 - Interface soil moisture sensor, display health status
- [ ] **[Air Quality Monitoring Device](./air-quality/)** 🟡 - Use sensors (MQ135, SDS011) to measure PM2.5 and CO2
- [ ] **[Energy Monitoring Smart Meter](./energy-monitor/)** 🔴 - Read current/voltage from CT sensors and visualize data

### 📊 Display & Interface
- [ ] **[Digital Clock with Python & Tkinter](./digital-clock/)** 🟢 - GUI-based clock application for local and UTC time
- [ ] **[GPIO Button Counter](./button-counter/)** 🟢 - Count button presses and show count on an LCD
- [ ] **[CPU Temp and Usage Dashboard](./system-dashboard/)** 🟢 - Create a local dashboard showing system stats using Bash/Python
- [ ] **[Digital Photo Frame](./photo-frame/)** 🟡 - Pull images from Google Photos and display them in slideshow mode
- [ ] **[Touchscreen Smart Mirror](./smart-mirror/)** 🟡 - Display weather, news, time on a reflective surface

### 🌐 IoT & Connectivity
- [ ] **[Raspberry Pi Weather Station (API version)](./weather-station-api/)** 🟢 - Fetch and display real-time weather using an online API
- [ ] **[Simple Web Server (Flask)](./flask-server/)** 🟢 - Serve a basic webpage and interact with buttons on your Pi
- [ ] **[Network Speed Logger](./network-logger/)** 🟢 - Record internet speed hourly using Python and log to CSV
- [ ] **[IoT Weather Station](./iot-weather/)** 🟡 - Push sensor data to the cloud (ThingSpeak / InfluxDB / MQTT)
- [ ] **[Smart Doorbell with Camera](./smart-doorbell/)** 🟡 - Detect press, take photo, notify via Telegram/email
- [ ] **[Pi as a VPN Server (WireGuard)](./vpn-server/)** 🟡 - Build a personal secure VPN you can connect to from anywhere
- [ ] **[Industrial IoT Gateway](./iot-gateway/)** 🔴 - Bridge Modbus (RS485) to MQTT for remote PLC monitoring
- [ ] **[Mesh Network Communication System](./mesh-network/)** 🔴 - Use LoRa or ESP-NOW to connect multiple Pi units across distances

### 🏠 Home Automation
- [ ] **[LED Blinker](./led-blinker/)** 🟢 - Learn GPIO basics by toggling an LED using Python
- [ ] **[IR Remote Controlled Devices](./ir-remote/)** 🟡 - Control appliances via infrared (send/receive signals)
- [ ] **[Home Automation System (Basic)](./home-automation/)** 🟡 - Control lights and fans via a web dashboard using relays
- [ ] **[RFID Access System](./rfid-access/)** 🟡 - Use MFRC522 to create a basic access control system

### 🔐 Security & Surveillance
- [ ] **[Raspberry Pi Surveillance System](./surveillance/)** 🟡 - Stream real-time video with motion detection using OpenCV
- [ ] **[USB Security Key](./usb-security/)** 🟢 - Use a Pi Pico or Zero as a 2FA USB device
- [ ] **[Pi-hole Setup](./pi-hole/)** 🟢 - Block ads and trackers on your network
- [ ] **[Edge-based Face Recognition Attendance System](./face-recognition/)** 🔴 - Recognize and log faces locally without cloud dependency
- [ ] **[Security Camera with ML Intruder Detection](./ml-security/)** 🔴 - Notify only when unusual activity is detected, reduce false positives

### 🎮 Entertainment & Media
- [ ] **[Photo Booth](./photo-booth/)** 🟢 - Use the Pi camera to take pictures with a button press and save them
- [ ] **[Bluetooth Speaker](./bluetooth-speaker/)** 🟢 - Configure your Pi to stream music over Bluetooth
- [ ] **[Mini Retro Gaming Console](./retro-gaming/)** 🟡 - Use RetroPie to emulate NES/SNES/GBA with USB controller
- [ ] **[Voice Assistant (Offline)](./voice-assistant/)** 🟡 - Use Vosk or Picovoice to create a basic voice command system
- [ ] **[Realtime Audio DSP](./audio-dsp/)** 🔴 - Process mic input and add effects in real-time (echo, filter, etc.)

### 🤖 Robotics & AI
- [ ] **[Self-Balancing Robot](./self-balancing-robot/)** 🔴 - Use MPU6050, motor drivers, and PID loops for real-time stability
- [ ] **[Autonomous RC Car with Obstacle Avoidance](./autonomous-car/)** 🔴 - Integrate camera, lidar/ultrasonic sensors, and path planning
- [ ] **[AI Object Detection System](./ai-detection/)** 🔴 - Use TensorFlow Lite or YOLOv5 on Pi + camera for real-time object detection
- [ ] **[Neural Network Inference Accelerator](./nn-accelerator/)** 🔴 - Offload deep learning inferences using Coral USB or Intel NCS2

### 🔧 System Administration & Networking
- [ ] **[Remote SSH Setup](./ssh-setup/)** 🟢 - Configure headless setup and learn the power of remote access
- [ ] **[Wireless Print Server](./print-server/)** 🟢 - Turn your Pi into a print server for non-Wi-Fi printers
- [ ] **[Pi NAS (Network Attached Storage)](./pi-nas/)** 🟡 - Configure Samba/FTP with attached HDDs for home file sharing
- [ ] **[Raspberry Pi Cluster (Docker or Kubernetes)](./pi-cluster/)** 🟡 - Run a 2–3 node cluster and distribute lightweight jobs
- [ ] **[Hypervisor and VM on Pi 5](./hypervisor/)** 🔴 - Run multiple OS instances using KVM

### 🔬 Advanced & Experimental
- [ ] **[Bare-metal OS on Raspberry Pi](./bare-metal-os/)** 🔴 - Write a simple operating system (e.g., display Hello World on UART)
- [ ] **[Custom Linux Kernel Compilation](./custom-kernel/)** 🔴 - Build and boot your own kernel with custom modules
- [ ] **[FPGA over Pi (with iCE40 or Lattice)](./fpga-interface/)** 🔴 - Use SPI/UART to interface and control a soft-core CPU
- [ ] **[CAN Bus Sniffer for Automotive](./can-sniffer/)** 🔴 - Interface with vehicles to log CAN messages using MCP2515


## 📋 Requirements

### Hardware
- **Raspberry Pi** (Any model with GPIO pins - Pi 3B+, Pi 4, Pi Zero recommended)
- **MicroSD Card** (16GB or larger, Class 10)
- **Power Supply** (Official Pi adapter recommended)
- **Breadboard and Jumper Wires**
- **Various Sensors and Components** (specific to each project)

### Software
- **Raspberry Pi OS** (Latest version recommended)
- **Python 3.7+**
- **Git** for cloning repositories
- **Various Python libraries** (specified in each project)

## 🛠️ Getting Started

### 1. Set Up Your Raspberry Pi
```bash
# Update your system
sudo apt update && sudo apt upgrade -y

# Install essential packages
sudo apt install python3-pip git vim -y

# Enable GPIO and other interfaces
sudo raspi-config
```

### 2. Clone This Repository
```bash
git clone https://github.com/yourusername/raspberry-pi-projects.git
cd raspberry-pi-projects
```

### 3. Choose a Project
Each project has its own directory with:
- `README.md` - Project-specific documentation
- `requirements.txt` - Python dependencies
- `circuit_diagram.png` - Wiring schematic
- Source code files
- Example configuration files

### 4. Install Dependencies
```bash
cd project-name
pip3 install -r requirements.txt
```

## 🎓 Difficulty Levels

Projects are categorized by difficulty:

- 🟢 **Beginner** - Basic GPIO control, simple sensors
- 🟡 **Intermediate** - Multiple components, basic networking
- 🔴 **Advanced** - Complex systems, IoT integration, machine learning

## 🔧 Common Tools & Libraries

### Essential Python Libraries
```bash
# GPIO Control
pip3 install RPi.GPIO gpiozero

# Sensor Libraries
pip3 install adafruit-circuitpython-dht w1thermsensor

# Display Libraries
pip3 install luma.oled luma.lcd

# Web Framework
pip3 install flask

# IoT & Communication
pip3 install paho-mqtt requests

# Computer Vision
pip3 install opencv-python picamera
```

### Useful Hardware Components
- **Sensors:** DHT11/22, HC-SR04, PIR, LDR, DS18B20
- **Displays:** 16x2 LCD, OLED (SSD1306), 7-segment
- **Actuators:** Servo motors, stepper motors, relays
- **Communication:** ESP8266, nRF24L01, Bluetooth modules
- **Power:** Buck converters, battery packs, solar panels

## 🐛 Troubleshooting

### Common Issues

**GPIO Permission Errors**
```bash
sudo usermod -a -G gpio $USER
# Log out and back in
```

**I2C Not Working**
```bash
sudo raspi-config
# Enable I2C in Interfacing Options
sudo reboot
```

**Python Module Not Found**
```bash
# Use Python 3 explicitly
python3 -m pip install module-name
```

**GPIO Already in Use**
```bash
# Reset GPIO state
sudo systemctl restart gpio-shutdown

**🍓 Happy Making with Raspberry Pi!**
