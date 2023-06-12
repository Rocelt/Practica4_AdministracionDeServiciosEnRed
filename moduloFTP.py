from ftplib import FTP

def extraerArchivo(ip,nombre):

    ftp = FTP(ip)  # connect to host, default port

    ftp.login("rcp","rcp")  # user anonymous, passwd anonymous@

    print(ftp.pwd())  # change into "debian" directory

    ftp.retrlines('LIST')  # list directory contents


    with open(nombre, 'wb+') as fp:
        ftp.retrbinary('RETR startup-config', fp.write)

    ftp.quit()
def enviarArchivo(ip):

    ftp = FTP(ip)  # connect to host, default port

    ftp.login("rcp","rcp")  # user anonymous, passwd anonymous@

    print(ftp.pwd())  # change into "debian" directory

    ftp.retrlines('LIST')  # list directory contents


    with open('startup-config', 'rb+') as fp:
        ftp.storbinary('STOR startup-config', fp)

    ftp.quit()