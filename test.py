import telnetlib
import time

HOST = "127.0.0.1"  # Use "192.168.1.162" for network access
PORT = 2323         # Must match your server port
TIMEOUT = 3         # Seconds

def send_command(tn, command):
    try:
        # Send command with proper line ending
        tn.write(f"{command}\r\n".encode('ascii'))
        
        # Wait briefly for response
        time.sleep(0.5)
        
        # Read all available data
        response = tn.read_very_eager().decode('ascii', errors='ignore')
        return response.strip()
        
    except Exception as e:
        return f"Error: {e}"

def main():
    try:
        # Create persistent connection
        with telnetlib.Telnet(HOST, PORT, TIMEOUT) as tn:
            print(f"Connected to {HOST}:{PORT}")
            print("Type 'exit' to quit\n")
            
            while True:
                # Get user input
                command = input("Enter command to send: ").strip()
                
                if command.lower() == 'exit':
                    break
                
                if not command:
                    continue
                
                # Send command and show response
                response = send_command(tn, command)
                print(f"Response: {response}\n")
                
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    main()
