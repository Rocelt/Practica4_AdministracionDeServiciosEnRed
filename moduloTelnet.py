import getpass
import telnetlib

def generarArchivo(ip):
    user = "rcp"
    password = "rcp"

    tn = telnetlib.Telnet(ip)

    tn.read_until(b"User: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"configure\n")
    tn.write(b"show interface\n")
    tn.write(b"copy running-config startup-config \n")
    tn.write(b"exit\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))