# DHT11 Temperature and Humidity Sensor with Python

A simple Python project to read temperature and humidity data from a DHT11 sensor using a Raspberry Pi or compatible microcontroller.

## 🌡️ Features

- Real-time temperature and humidity monitoring
- Continuous data logging with 2-second intervals
- Error handling for sensor reading failures
- Support for both Celsius and Fahrenheit
- Clean console output with formatted readings
- Graceful program termination with Ctrl+C

## 📋 Requirements

### Hardware
- Raspberry Pi (any model with GPIO pins)
- DHT11 Temperature and Humidity Sensor
- Jumper wires
- Breadboard (optional)
- 4.7kΩ or 10kΩ pull-up resistor (recommended)

### Software
- Python 3.6 or higher
- pip package manager

## 🔧 Installation

### Option 1: Using Adafruit CircuitPython Libraries (Recommended)

```bash
# Install required packages
pip install adafruit-circuitpython-dht
sudo apt-get install libgpiod2

# For some systems, you might also need:
pip install adafruit-blinka
```

### Option 2: Using Legacy Adafruit DHT Library

```bash
pip install Adafruit-DHT
```

## 🔌 Hardware Setup

### Pin Connections

| DHT11 Pin | Raspberry Pi Pin | GPIO |
|-----------|------------------|------|
| VCC       | Pin 1 (3.3V) or Pin 2 (5V) | - |
| Data      | Pin 7            | GPIO4 |
| GND       | Pin 6 (Ground)   | - |

### Circuit Diagram

```
DHT11           Raspberry Pi
┌─────┐         ┌─────────────┐
│ VCC │─────────│ 3.3V (Pin 1)│
│     │         │             │
│Data │─────────│GPIO4 (Pin 7)│
│     │    │    │             │
│ GND │────┼────│ GND  (Pin 6)│
└─────┘    │    └─────────────┘
           │
        ┌──┴──┐
        │4.7kΩ│ (Pull-up resistor)
        │     │
        └──┬──┘
           │
       To VCC
```

## 🚀 Usage

1. Clone this repository:
```bash
git clone https://github.com/yourusername/dht11-python-sensor.git
cd dht11-python-sensor
```

2. Run the main script:
```bash
python tempSensor.py
```

### Continuous Monitoring
The main script provides continuous monitoring with error handling and graceful termination.

## 🔍 Sample Output

```
Temp: 24.0°C | Humidity: 45.0%
Temp: 24.1°C | Humidity: 44.8%
Temp: 24.0°C | Humidity: 45.2%
Sensor reading failed. Retrying...
Temp: 24.2°C | Humidity: 45.1%
^C
Exiting program...
```

### Common Issues

**"No module named board" Error**
- Install the required packages as shown in the installation section
- Make sure you're running on a compatible platform (Raspberry Pi, etc.)

**Sensor Reading Failures**
- Check all connections are secure
- Ensure the DHT11 is receiving proper power (3.3V or 5V)
- Add a pull-up resistor between data pin and VCC
- Try increasing the delay between readings

**Permission Errors**
- Run the script with `sudo` if you encounter GPIO permission issues:
```bash
sudo python tempSensor.py
```

**Inconsistent Readings**
- DHT11 sensors can be sensitive to timing and environmental factors
- Ensure stable power supply
- Keep the sensor away from heat sources or direct airflow

### DHT11 Sensor Specifications
- **Temperature Range:** 0°C to 50°C (±2°C accuracy)
- **Humidity Range:** 20% to 90% RH (±5% accuracy)
- **Operating Voltage:** 3.3V to 5V
- **Sampling Rate:** No more than 1Hz (once per second)

