import socket

def scan_port(port):
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(0.5)
      result = s.connect_ex(('127.0.0.1', port)) 
      return result == 0