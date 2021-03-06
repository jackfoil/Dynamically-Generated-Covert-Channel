#! python

#from block import Block
from mitmproxy.options import Options
from mitmproxy.tools.dump import DumpMaster
from mitmproxy import http
from mitmproxy.addons import block

class GetInjection(object):
    """MiTMProxy addon that injects a message into the header of a response packet."""
    def __init__(self,p: DumpMaster):
        self.proxy = p
        self.m = ""
    # need to add timeout if flow not received in specified amount of time
    def request(self,flow: http.HTTPFlow) -> None:

        # get secret value
        if(int(flow.request.headers["RTT"]) == 999):
            with open('output.txt','w',encoding='utf-8-sig') as f:
                for i in self.m:
                    f.write(i)

            print("[*] Complete Message Received")
            self.proxy.shutdown()
        else:
            self.m+=chr(int(flow.request.headers["RTT"]))
            print("[!] Received Message")
            flow.kill()


def config_proxy():
    """Configures mitmproxy on specific port and address."""
    opts = Options(listen_host="138.47.142.77",listen_port=8080) 
    server = DumpMaster(opts)
    return server

if __name__ == """__main__""":
    # configurations
    prox = config_proxy()
    prox.addons.add(GetInjection(prox),block)

    # start proxying!
    prox.run()


