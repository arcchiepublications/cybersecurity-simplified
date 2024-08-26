from scapy.all import sniff, TCP
import smtplib
import logging

# Setup logging for alerts
logging.basicConfig(filename='alerts.log', level=logging.INFO)

# Function to send email alerts
def send_alert(message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("youremail@gmail.com", "password")  # Replace with your email and password
        server.sendmail("youremail@gmail.com", "alertrecipient@gmail.com", message)  # Replace with sender and recipient emails
        server.quit()
        print("Alert sent via email.")
    except Exception as e:
        print(f"Failed to send alert: {e}")

# Function to log alerts
def log_alert(message):
    logging.info(message)
    print("Alert logged.")

# Function to analyze packets for potential threats
def analyze_packet(packet):
    if packet.haslayer(TCP):
        # Detect potential SYN scan (TCP flag "S" indicates SYN packets)
        if packet[TCP].flags == "S":
            alert_message = f"Potential SYN scan detected from {packet[IP].src} to {packet[IP].dst}"
            print(alert_message)
            # Log the alert and send an email notification
            log_alert(alert_message)
            send_alert(alert_message)

# Function to capture and process network packets
def packet_callback(packet):
    # Print a summary of the captured packet
    print(packet.summary())
    # Analyze the packet for suspicious activity
    analyze_packet(packet)

# Start capturing packets with a callback to process each packet
def start_sniffing():
    sniff(prn=packet_callback, count=10)  # Adjust count as needed

if __name__ == "__main__":
    print("Starting packet capture...")
    start_sniffing()
