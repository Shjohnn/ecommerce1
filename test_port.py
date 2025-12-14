import socket

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(('127.0.0.1', port))
        print(f"Port {port}: BOSH (OK)")
        sock.close()
        return True
    except PermissionError:
        print(f"Port {port}: RUXSAT YO'Q (Permission Denied)")
    except OSError as e:
        print(f"Port {port}: BAND yoki XATO - {e}")
    return False

print("Tekshirilmoqda...")
ports_to_check = [8000, 8001, 8080, 8090, 9000, 55555, 6060]

for p in ports_to_check:
    check_port(p)
