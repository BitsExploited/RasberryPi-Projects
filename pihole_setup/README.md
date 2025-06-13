# Pi-hole Network-wide Ad Blocker 🌐🚫

Set up a Raspberry Pi-based ad blocker using **Pi-hole** and enjoy a cleaner, faster internet across all your devices — Android, iOS, Linux, Windows, and macOS.

---

## 📦 What is Pi-hole?

Pi-hole is a network-wide ad blocker that acts as a **DNS sinkhole**, filtering out ads, trackers, and malicious domains for every device on your network.

---

## 📡 Requirements

* Raspberry Pi (any model, ideally Pi 2 or newer)
* Raspberry Pi OS (Lite recommended)
* SSH or monitor access to the Pi
* Internet connection
* Static IP or reserved IP for the Pi (recommended)

---

## ⚙️ Installation

SSH into your Pi or access it locally:

```bash
sudo apt update && sudo apt upgrade -y
curl -sSL https://install.pi-hole.net | bash
```

The installer will guide you through:

* Selecting the network interface
* Setting a static IP (important)
* Choosing DNS upstream providers (Google, Cloudflare, etc.)
* Installing the web admin interface

Once installed, access the dashboard:

📍 **Web UI:** `http://<Pi-IP>/admin`
💡 Default login password can be set/reset with:

```bash
pihole -a -p
```

---

## 🧪 Test If Pi-hole Is Working

```bash
dig doubleclick.net @<Pi-IP>
```

Should return: `0.0.0.0` (blocked)

---

## 📱 Device Configuration

To make Pi-hole block ads, each device must use it as its **DNS server**.

---

### ✅ Android

1. Go to **Settings → Network & Internet → Wi-Fi**
2. Tap your current network → **Advanced → IP settings**
3. Change from **DHCP** to **Static**
4. Set **DNS 1** to your Pi-hole IP (e.g., `192.168.1.5`)
5. Leave Gateway and IP as-is

📌 Ads will now be blocked on Wi-Fi

---

### ✅ iPhone (iOS)

1. Open **Settings**
2. Tap **Wi-Fi**
3. Tap the ℹ️ next to your connected network
4. Scroll to **DNS** and tap **Configure DNS**
5. Select **Manual**
6. Delete existing servers
7. Add your Pi-hole IP (e.g., `192.168.1.5`)
8. Tap **Save**

🔗 Now your iPhone uses Pi-hole to resolve DNS

---

### ✅ macOS

1. Open **System Settings → Network**
2. Select your active connection (Wi-Fi or Ethernet)
3. Click **Details** → **DNS** tab
4. Click **+** and enter Pi-hole IP
5. Remove other DNS servers
6. Click **OK** and **Apply**

---

### ✅ Windows 10/11

1. Open **Control Panel → Network and Internet → Network Connections**
2. Right-click your network → **Properties**
3. Select **Internet Protocol Version 4 (TCP/IPv4)** → Click **Properties**
4. Choose **Use the following DNS server addresses**
5. Enter your Pi-hole IP in **Preferred DNS**
6. Click **OK**

---

### ✅ Linux (NetworkManager)

```bash
nmcli con show              # List connections
nmcli con mod "<YourConnection>" ipv4.dns "192.168.1.5"
nmcli con mod "<YourConnection>" ipv4.ignore-auto-dns yes
nmcli con up "<YourConnection>"
```

Replace `192.168.1.5` with your actual Pi-hole IP.

---

## ✨ Make It Automatic

Set Pi-hole as the **default DNS server** in your router’s DHCP settings:

* Log in to your router (usually `192.168.1.1`)
* Find DHCP or LAN settings
* Set **DNS Server 1** to your Pi-hole IP
* Save and reboot router

All connected devices will now automatically use Pi-hole for DNS!

---

