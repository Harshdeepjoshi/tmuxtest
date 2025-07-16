import telnetlib

# Configure these:
HOST = "192.168.1.162"  # IP from your screenshot
PORT = 2323             # Port from your screenshot
TIMEOUT = 3             # Seconds

def send_command(command):
    try:
        with telnetlib.Telnet(HOST, PORT, TIMEOUT) as tn:
            tn.write(f"{command}\n".encode('ascii'))
            return tn.read_until(b"\n", timeout=1).decode('ascii').strip()
    except Exception as e:
        return f"Error: {e}"

# Example usage:
print(send_command("home"))      # Test ESP8266 response
