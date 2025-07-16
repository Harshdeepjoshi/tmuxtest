import os
import subprocess
import serial
from time import sleep

def ensure_usb_permission(device_path):
    """Automatically handles USB permissions"""
    try:
        # Try to request permission
        subprocess.run(['termux-usb', '-r', device_path], check=True)
        
        # Verify permission by attempting to list
        result = subprocess.run(['termux-usb', '-l'], capture_output=True, text=True)
        if device_path not in result.stdout:
            raise PermissionError(f"Failed to get permission for {device_path}")
        
        print(f"Successfully acquired permissions for {device_path}")
        return True
        
    except Exception as e:
        print(f"Permission error: {e}")
        return False

def connect_to_esp():
    PORT = '/dev/bus/usb/001/002'  # Your device path
    BAUDRATE = 115200
    
    # First ensure we have permissions
    if not ensure_usb_permission(PORT):
        print("Failed to get USB permissions")
        return

    try:
        print(f"Connecting to {PORT}...")
        ser = serial.Serial(PORT, BAUDRATE, timeout=1)
        print("Connected successfully!")
        
        # Simple communication test
        ser.write(b'AT\r\n')
        print("Response:", ser.readline().decode().strip())
        
        # Your actual communication logic here
        while True:
            cmd = input("Enter command (or 'exit'): ")
            if cmd.lower() == 'exit':
                break
            ser.write((cmd + '\n').encode())
            print("Response:", ser.readline().decode().strip())
            
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    finally:
        if 'ser' in locals():
            ser.close()

if __name__ == "__main__":
    connect_to_esp()
