import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

try:
    while True:

        humidity, temp_c = Adafruit_DHT.read_retry(sensor, pin)
        
        if humidity is not None and temp_c is not None:
            print(f"Temp: {temp_c:.1f}°C | Humidity: {humidity:.1f}%")
        else:
            print("Sensor reading failed. Retrying...")
            
        time.sleep(2)
        
except KeyboardInterrupt:
    print("\nExiting program...")
    print("Program terminated by user")
