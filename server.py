import socket 
import time, threading


def err_control(func):
    def connect_server(self,*args):

        try:
            func(self,*args)

        except Exception as e:
            print(f"{args[0]} port ve {args[1]} host için bir bağlantı hatası mevcut ",e) if args else None

            print("program çalışma sırasında bir hata meydana geldi")


    return connect_server



class Socket:

    def __init__(self, capacity=2):

        self.host = "localhost"
        self.port = 12000
        self.capacity = capacity
        self.message = "merhaba servera hosgeldin sana nasıl hitap etmeliyim? "

    

    def send_server_message(self, user):

        self.user.send(self.message.encode('utf-8'))




    def user_thread(self, client, addr):

        user_key = f"{addr[0]}-{addr[1]}"
        user_name = f"anon_{addr[1]}"

        print(f"{user_name}, bağlandı")


        client.send(self.message.encode('utf-8'))

        while True:
            try:
                answer_msg = client.recv(1024)
                if not answer_msg :
                    break


                answer_utf = answer_msg.decode('utf-8')

                if answer_utf.split(" ")[0] == 'username':
                    user_name = answer_utf.split(" ")[1]

                print(f"{user_name} : ", answer_utf)


                if answer_utf.lower() == "exit":
                    break

            except Exception as e:
                break

        print(f"{user_name} serverdan ayrıldı")
        client.close()


    def show_users(self):
        
        for key, val in self.users.items:
            print(f"isim {val}, port {key}")


    #@err_control
    def run_server(self):
        
        self.sock.listen(self.capacity)    
        for i in "Server dinliyor...":
            time.sleep(0.2)
            print(i,end="")

            while True:
                client , addr = self.sock.accept()   
                threading.Thread(target=self.user_thread, args=(client, addr)).start()

    @err_control
    def create_socket(self,port, host):
        
        self.host = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP ve UDP ----  TCP
        self.sock.bind((self.host, self.port))



    

if __name__ == '__main__':
    myApp = Socket(3)
    myApp.create_socket(12355, "localhost")
    myApp.run_server()
