import socket
import time
local_name=socket.gethostname()
local_ip=socket.gethostbyname(local_name)
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((local_ip,6666))
addrlist=[]
while 1:
    mess,addr=server.recvfrom(4096)
    timepre=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    f=open('record.txt','a')
    f.write(timepre+"   "+addr[0]+":"+str(addr[1])+"    "+mess+"\n")
    f.close()
    print timepre+"   "+addr[0]+":"+str(addr[1])+"    "+mess+"\n"
    if not (addr in addrlist):
        addrlist.append(addr)
    for a in addrlist:
        if mess!="initing...":
            server.sendto(timepre+"   "+addr[0]+":"+str(addr[1])+"    "+mess+"\n",a)
