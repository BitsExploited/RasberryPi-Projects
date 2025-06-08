import time
import board
import adafruit_dht

dht = adafruit_dht.DHT11(board.D4)

try:
    while True:
        try:
            temp_c = dht.temperature
            humidity = dht.humidity
            
            if temp_c is not None and humidity is not None:
                temp_f = temp_c * (9/5) + 32
                print(f"Temp: {temp_c:.1f}°C ({temp_f:.1f}°F) | Humidity: {humidity:.1f}%")
            else:
                print("Sensor reading failed. Retrying...")
                
        except RuntimeError as error:
            print(f"Reading error: {error.args[0]}")
            
        time.sleep(2)
        
except KeyboardInterrupt:
    print("\nExiting program...")
finally:
    dht.exit()
