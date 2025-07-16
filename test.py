import socket

HOST = "127.0.0.1"  # Use this for local connection (or your phone's IP)
PORT = 2323         # Must match your server's port
TIMEOUT = 3         # Seconds

def send_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            s.connect((HOST, PORT))
            s.sendall(f"{command}\r\n".encode())  # Explicit CR+LF
            
            # Read all available data
            response = b""
            while True:
                data = s.recv(1024)
                if not data:
                    break
                response += data
            
            return response.decode('latin-1').strip()  # Handles binary data
            
    except Exception as e:
        return f"Error: {e}"

# Example usage:
print(send_command("AT"))   # Test command
print(send_command("51"))  # Your position command
