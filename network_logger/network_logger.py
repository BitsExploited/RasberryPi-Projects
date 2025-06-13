import csv
import os
from datetime import datetime
import speedtest

CSV_FILE = os.path.expanduser("~/network_speed_log.csv")  # Logs to your home directory

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Download_Mbps", "Upload_Mbps", "Ping_ms"])

def log_speed():
    print("🚀 Running speed test...")
    st = speedtest.Speedtest()
    st.get_best_server()

    download = round(st.download() / 1_000_000, 2)  # Mbps
    upload = round(st.upload() / 1_000_000, 2)      # Mbps
    ping = round(st.results.ping, 2)                # ms

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 📝 Log to CSV
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, download, upload, ping])

    # 📟 Print to terminal
    print(f"\n Time:     {timestamp}")
    print(f" Download: {download} Mbps")
    print(f" Upload:   {upload} Mbps")
    print(f" Ping:     {ping} ms\n")

if __name__ == "__main__":
    init_csv()
    log_speed()

