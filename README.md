# Dynamically Generated Covert Channel
### A covert channel generator designed for cyber security proffessionals.
# Installation
## **Scapy Setup**
**Pre-requisites**  
*[Python 2.7.X or 3.4+](https://www.python.org/downloads/)*
  
First ensure python installation directory and scripts directory are to your PATH
1. Control Panel/System and Security/System/Advanced System Settings  
2. Select environment variables
3. Select PATH
4. Add the python installation directory and scripts directory. These are typically:  
`C:\Users\user\AppData\Local\Programs\Python\PythonXX`  
`C:\Users\user\AppData\Local\Programs\Python\PythonXX\Scripts`  

Pip install dependicies for the complete scapy module  
`./requirements`  

Install the latest version of [Npcap](https://nmap.org/npcap/#download) & [MikTex](https://miktex.org/download)

Next git clone scapy repository & install the scapy module  
`git clone https://github.com/secdev/scapy`  
`python setup.py install`

Run the scapy command in preferred shell
`scapy`
- *scapy needs elevated privileges to execute*
- *ignore all the bootstrap errors; they're just there to add spice*








