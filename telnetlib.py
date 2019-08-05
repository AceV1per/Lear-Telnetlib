import getpass
import sys
import telnetlib

#router_list = [
#{'ip':'10.10.10.1','username':'cisco','password':'cisco'},
#{'ip2': '10.10.10.2', 'username2' : 'cisco' , 'password2':'cisco'} ]


#for r in router_list:
HOST = '10.10.10.1'
user = 'cisco'   #r['username']
password = 'cisco'  #r[{'password'}]

tn = telnetlib.Telnet(HOST)
tn.read_until("Username: ")
tn.write(user + "\n")
tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("hostname saya_tampan\n")

for x in range(1,10):
     tn.write("interface loopback{}\n".format(x))
     tn.write("description FROM_TELNET_SCRIPT\n")
     tn.write("ip address 1.1.1.{} 255.255.255.255\n".format(x))
tn.write("exit\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()

