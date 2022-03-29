#! python
from mitmproxy.options import Options
from mitmproxy.tools.dump import DumpMaster
from mitmproxy import tcp, http
from mitmproxy.addons import next_layer


class AddTCPHeader():

    def request(self,flow: http.HTTPFlow):
        print(flow.request.content)




def config_proxy():
    """Configures mitmproxy on specific port and address."""
    opts = Options(listen_host=TARGET,listen_port=TARGET_PORT,rawtcp=True) 
    server = DumpMaster(opts)
    # server.options.set("save_stream_file=stream.pcap")
    return server

if __name__ == "__main__":
    TARGET = '127.0.0.1' #ip address of proxy
    TARGET_PORT = 8080   #port of proxy
    #WEBSERVER = "10.172.188.126"

    prox = config_proxy()
    prox.addons.add(AddTCPHeader()) #load addon into proxy

    # start proxying!
    try:
        prox.run()
    except KeyboardInterrupt:
        prox.shutdown()