import socket
import threading
import time,sys
from Tkinter import *
local_name=socket.gethostname()
local_ip=socket.gethostbyname(local_name)
local_port=5129
server_ip="#server's ip"
server_port=6666
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.bind((local_ip,local_port))
client.sendto("initing...",(server_ip,server_port))
init1=client.recvfrom(1024)
flag=True
def Sendinfo():
    messsend=var.get()
    var.set("")
    if messsend!="":
        client.sendto(messsend,(server_ip,server_port))
def listeninfo(flag,client):
    while 1:
        message,addr=client.recvfrom(4096)
        text.insert(END,message)
def Exitf():
    root.destroy()
    sys.exit(0)
def main():
    root=Tk()
    global root
    root.geometry("700x350")
    c=Canvas(root,width=700,height=500,bg='white')
    message="Your IP is "+local_ip
    Label(root,text=message).grid(row=0,column=0)
    var=StringVar()
    e=Entry(root,textvariable=var,width=75).place(x=0,y=300,anchor=NW)
    var.set("")
    global var
    text=Text(root,width=75,height=17,wrap=WORD)
    text.grid(row=1,column=0)
    global text
    Button(root,text="Send",command=Sendinfo,width=18,height=2).place(x=550,y=300,anchor=NW)
    Button(root,text="Exit",command=Exitf,width=18,height=2).place(x=550,y=150,anchor=NW)
    mainloop()
t1=threading.Thread(target=listeninfo,args=(flag,client))
t1.start()
main()
