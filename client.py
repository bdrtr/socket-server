import socket

s = socket.socket()



host = "localhost"
port = 12355

try:
    s.connect((host,port))

    yanit = s.recv(1024)
    print(yanit.decode('utf-8'))

    while True:
        girdi = input(">>> ")


        if girdi == 'q':
            break


        s.send(girdi.encode('utf-8'))
    

    s.close()


except:
    print("hata")