    # -*- coding: utf-8 -*-  
    # author: orangleliu date: 2014-11-12  
    # python2.7.x ip_scaner.py  
      
    # '''''  
    # 扫描局域网内活跃IP  
    # 执行：python ip_scaner.py 192.168.1.1  
    # '''  
    
# import platform  
# import sys  
# import os  
# import time  
# import thread  
      
# def get_os():  
#     '''''  
#     get os 类型  
#     '''  
#     os = platform.system()
    
#     if os == "Windows":  
#         return "n"  
#     else:  
#         return "c"  
      
      
# def ping_ip(ip_str):  
#     cmd = ["ping", "-{op}".format(op=get_os()),  
#                "1", ip_str]
#     print get_os  
#     output = os.popen(" ".join(cmd)).readlines()  
#     print cmd
#     flag = False  
#     for line in list(output):  
#         if not line:  
#             continue  
#             if str(line).upper().find("TTL") >= 0:  
#                 flag = True  
#                 break  
#         if flag:  
#             return True  
#         else:  
#             return False  
# def find_ip(ip_prefix):  
#     '''''  
#     给出当前的127.0.0 ，然后扫描整个段所有地址  
#     '''  
#     for i in range(1, 256):  
#         ip = '%s.%s' % (ip_prefix, i)  
#         thread.start_new_thread(ping_ip, (ip,))  
#         time.sleep(0.3)  
#         print ip_prefix
# if __name__ == "__main__":  
#     print "start time %s" % time.ctime()  
#     commandargs=sys.argv[1:]  
#     args = "".join(commandargs)  
      
#     ip_prefix = '.'.join(args.split('.')[:-1])  
#     find_ip(ip_prefix)  
#     print "end time %s" % time.ctime()  


#-*- coding:utf-8 -*-  
#2105-03-25  
Port = [80,21,23,22,25,110,443,1080,3306,3389,1521,1433]  
Server = ['HTTP','FTP','TELNET','SSH','SMTP','POP3','HTTPS','SOCKS','MYSQL','Misrosoft RDP','Oracle','Sql Server']  
result = []  
  
import socket   
import sys  
import threading  
import time  
  
  
def get_remote_machine_info(Domain):  
    try:  
        return socket.gethostbyname(Domain)  
    except socket.error,e:  
        print '%s: %s'%(Domain,e)  
        return 0  
  
def scan(Domain,port,server):  
    temp = []  
    try:  
        s = socket.socket()  
        print "Attempting to connect to "+Domain+': '+str(port)  
        s.connect((Domain,port))  
        temp.append(port)  
        temp.append(server)  
        result.append(temp)  
        s.close()  
    except:  
        pass  
          
  
def output(Domain,IP):  
    if result:  
        print '\n'+Domain+': --> '+IP  
        print '\nThe Open Port:'  
        for i in result:  
            print Domain+': %4d -->%s'%(i[0],i[1])  
    else:  
        print 'None Port!'  
  
def main():  
    print '''''\nX-man Port Scan 2.0 payload:./Scan.py www.xxx.zzz'''  
    payload = sys.argv
    print payload  
    IP = get_remote_machine_info(payload[0])  
    print '\n'  
    for port,server in zip(Port,Server):  
        t = threading.Thread(target=scan,args=(payload[0],port,server,)) #for循环创建线程，每个端口开一个线程  
        t.setDaemon(True) #将线程声明为守护线程,使其可快速退出  
        t.start()  
        time.sleep(0.1) #每个线程之间设置时间间隔，避免输出混乱  
    output(payload[0],IP)  
  
if __name__=='__main__':  
    main() 