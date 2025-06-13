# 📱 Network Speed Logger for Raspberry Pi

A simple project to log internet speed hourly in a csv file and display results in the terminal. Useful for tracking network performance over time.

---

## 🔧 Features

* 🕒 Hourly speed tests using `speedtest-cli`
* 📁 Results logged in a CSV file
* 🔤 Clean terminal output after each test

---

## 📁 Project Structure

```
network_logger/
├── speed_logger.py       # Runs speedtest, logs to CSV, prints to terminal
├── speed_log.csv         # Auto-generated log file (timestamp, DL, UL, ping)
└── README.md             # This file
```

---

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
pip install speedtest-cli
```

---

### 2. Run the Script

**Terminal Speed Logger (every 1 hour)**

```bash
python3 speed_logger.py
```

---

## 🔄 Auto-Run on Boot (Optional)

Edit crontab:

```bash
crontab -e
```

Add:

```bash
@reboot python3 /home/pi/network_logger/speed_logger.py &
```

