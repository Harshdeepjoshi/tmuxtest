import telnetlib
import time

HOST = "127.0.0.1"  # Use "192.168.1.162" for network access
PORT = 2323         # Must match your server port
TIMEOUT = 3         # Seconds

def send_command(command):
    try:
        # Create connection (ignore deprecation warning)
        with telnetlib.Telnet(HOST, PORT, TIMEOUT) as tn:
            # Send command with proper line ending
            tn.write(f"{command}\r\n".encode('ascii'))
            
            # Wait briefly for response
            time.sleep(0.5)
            
            # Read all available data
            response = tn.read_very_eager().decode('ascii', errors='ignore')
            return response.strip()
            
    except Exception as e:
        return f"Error: {e}"

# Example usage
print(send_command("AT"))   # Test command
print(send_command("51"))  # Your position command
