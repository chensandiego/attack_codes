import socket,sys,os
host='example.com'

open_ports=[]
start_port=1
end_port=10


ip=socket.gethostbyname(host)



def probe_port(host,port,result=1):
    try:
        sockObj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sockObj.settimeout(0.5)
        r=sockObj.connect_ex((host,port))
        if r==0:
            result=r
        socket.close()
    except Exception as e:
        pass
    return result



for port in range(start_port,end_port+1):
    sys.stdout.flush()
    print (port)
    response = probe_port(host,port)
    if response == 0:
        open_port.append(port)
    if not port == end_port:
        sys.stdout.write('\b' * len(str(port)))


if open_ports:
    print ("open port")
    print (sorted(open_ports))
else:
    print ("sorry no open ports found")



common_ports={21,22,23,25,53,69,80,88,109,110,123,137,138,139,143,156,161,389,443,445,500,546,547,587,660,995,993,2086,2087,2082,2083,3306,8443,10000}


for p in sorted(common_ports):
    sys.stdout.flush()
    print (p)
    response = probe_port(host,p)
    if response == 0:
        open_ports.append(p)
    if not p == end_port:
        sys.stdout.write('\b' * len(str(p)))
