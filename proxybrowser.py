#! python
from os import walk,path,startfile
from pynput.keyboard import Key, Controller, Listener
from time import sleep
import subprocess
import pygetwindow as pw

#pip installed pygetwindow
#pip installed pynput
"""Improvements"""
'''
Error Handling:
2 Needs stealhify
4 Needes function to disable proxy
'''
I = .2
J = 1.05

def _configCert()->None:
    subprocess.run(["powershell","-Command","certutil -addstore root mitmproxy-ca-cert.cer"],capture_output=True)

def _revertCert()->None:
    subprocess.run(["powershell","-Command","certutil -delstore root mitmproxy-ca-cert.cer"],capture_output=True)

def _getWindow(app: str)->object:
    """Ensures the rigt window is in the foreground."""
    win = pw.getWindowsWithTitle(app)[0]
    print(win.title)
    while(True):
        try:
            win.activate()
            win.minimize()
            win.maximize()
            break
        except:
            win = pw.getWindowsWithTitle(app)[0]
            win.minimize()
            win.maximize()
        sleep(3)
    return win

def getUser()->str:
    """Gets current user of system."""
    u = subprocess.run(["powershell","-Command","whoami"],capture_output=True)
    u = (u.stdout).decode("ascii").strip('\n')
    return u

def findFile(inpath: str,user: str,browser: str = "")->str:
    """Configures path for executable."""
    paths = {
    'start_menu' : ['ProgramData','Microsoft','Windows','Start Menu','Programs'],
    'exec_path' : {
                    'chrome':['Program Files','Google','Chrome','Application'],
                    'firefox':['Program Files','Mozilla Firefox'],
                    'edge':['Program Files (x86)','Microsoft','Edge','Application']
                  },
    'task_bar_path' : ['Users',user,'AppData','Roaming','Microsoft','Internet Explorer','Quick Lauch','User Pinned','TaskBar'],
    'desktop_path' : ['Users',user,'Desktop']
    }
    start = "C:\\"
    loc = ""
    if browser != "": loc = paths[inpath][browser]
    else: loc = paths[inpath]
    for i in loc:
        for _,dirs,_ in walk(start):
            if i in dirs:
                start = path.join(start,i)
                break
    return start

def startExec(name:str,path:str) -> None:
    path = path + "\\" + name
    print(path)
    startfile(path)

def ProxyFirefox() -> None:
    window = _getWindow('Firefox')
    config=[[Key.ctrl,'l'],[Key.ctrl,'a'],'about:preferences',Key.enter,[Key.ctrl,'l'],Key.tab,Key.tab,Key.tab,Key.tab,Key.tab,Key.tab,Key.tab,'proxy',
            Key.tab,Key.tab,Key.enter,Key.down,Key.down,Key.down,Key.tab,'127.0.0.1',Key.tab,'8081',Key.enter,[Key.ctrl,Key.shift,'q']]

    kb = Controller()
    for i in config:
        if type(i) is list:
            for j in i:
                kb.press(j)
                sleep(I)
            for j in i:
                kb.release(j)
                sleep(I)
        elif type(i) is str and len(i) > 1:
            for j in i:
                kb.press(j)
                sleep(I)
                kb.release(j)
                sleep(I)
        else:
            if isinstance(i,Key):
                sleep(J)
            kb.press(i)
            sleep(I)
            kb.release(i)
            sleep(I)

def ProxyChrome()-> None:
    """Configure system for proxying traffic from Chrome."""
    window = _getWindow('Google Chrome')
    config = [[Key.ctrl,'l'],'chrome://settings/?search=proxy', Key.enter, Key.tab, Key.tab,
               Key.tab, Key.tab, Key.enter, Key.tab, Key.tab,Key.space, Key.backspace, Key.tab, Key.tab, Key.tab, [Key.ctrl, 'a'], '1','2','7','.','0','.','0','.','1',
               Key.tab,[Key.ctrl, 'a'],'8','0','8','1',Key.tab,Key.tab,Key.tab,Key.enter,[Key.alt, Key.f4],[Key.alt, Key.f4]]

    kb = Controller()
    for i in config:
        if type(i) is list:
            for j in i:
                kb.press(j)
                sleep(I)
            for j in i:
                kb.release(j)
                sleep(I)
        elif type(i) is str and len(i) > 1:
            for j in i:
                kb.press(j)
                sleep(I)
                kb.release(j)
                sleep(I)
        else:
            if isinstance(i,Key):
                sleep(J)
            kb.press(i)
            sleep(I)
            kb.release(i)
            sleep(I)

def ProxyEdge()->None:
    """Configure system for proxying internet traffic from Microsoft Edge."""
    window = _getWindow('Edge')
    config = [[Key.ctrl,'l'],'edge://settings/?search=proxy',Key.enter, [Key.ctrl,'l'], Key.esc,Key.tab, Key.tab, Key.tab, Key.tab, Key.tab, Key.tab, Key.tab,
              Key.tab, Key.tab, Key.tab, Key.tab, Key.tab,Key.tab,Key.tab,Key.tab,Key.tab,Key.enter, Key.backspace, Key.tab, Key.tab, Key.tab, Key.space, Key.tab, [Key.ctrl, 'a'],'1','2','7','.','0','.','0','.','1', Key.tab,
              [Key.ctrl, 'a'],'8','0','8','1',Key.tab,Key.tab,Key.tab,Key.enter,[Key.alt, Key.f4],[Key.alt, Key.f4]]
    kb = Controller()
    for i in config:
        if type(i) is list:
            sleep(I)
            for j in i:
                kb.press(j)
                sleep(I)
            for j in i:
                kb.release(j)
                sleep(I)
        elif type(i) is str and len(i) > 1:
            for j in i:
                kb.press(j)
                sleep(I)
                kb.release(j)
                sleep(I)
        else:
            sleep(J)
            if i is Key.enter: 
                kb.touch(i,True)
                sleep(J)
            else:
                kb.press(i) 
                sleep(I)
            kb.release(i)
            if i is Key.enter: sleep(J)
            else: sleep(I)

def releaseProxyFirefox():
    """Disables firefox browser using key shortcuts."""
    window = _getWindow('Firefox')
    config = [[Key.ctrl,'l'],[Key.ctrl,'a'],'about:preferences',Key.enter,[Key.ctrl,'l'],Key.tab,Key.tab,Key.tab,Key.tab,Key.tab,Key.tab,Key.tab,'proxy',
             Key.tab,Key.tab,Key.enter,Key.up,Key.up,Key.up,Key.enter,[Key.ctrl,Key.shift,'q']]
    sleep(3)
    kb = Controller()
    for i in config:
        if type(i) is list:
            for j in i:
                kb.press(j)
                sleep(I)
            for j in i:
                kb.release(j)
                sleep(I)
        elif type(i) is str and len(i) > 1:
            for j in i:
                kb.press(j)
                sleep(I)
                kb.release(j)
                sleep(I)
        else:
            if isinstance(i,Key): sleep(J)
            
            if i is Key.enter: 
                kb = Controller()
                lis = Listener()
                kb.press(i)
                sleep(J)
            else:
                kb.press(i) 
                sleep(I)
            
            if i is Key.enter: 
                kb = Controller()
                kb.release(i)
                sleep(J)
            else: 
                kb.release(i)
                sleep(I)

def releaseProxyChrome()->None:
    """Disables chrome browser using key shortcuts."""
    window = _getWindow('Google Chrome')
    config = [[Key.ctrl,'l'],'chrome://settings/?search=proxy', Key.enter, Key.tab, Key.tab,
               Key.tab, Key.tab, Key.enter, Key.tab, Key.tab,Key.space, Key.backspace, Key.tab, Key.tab, Key.tab,Key.space,
               [Key.alt, Key.f4],[Key.alt, Key.f4]]
    sleep(3)
    kb = Controller()
    for i in config:
        if type(i) is list:
            for j in i:
                kb.press(j)
                sleep(I)
            for j in i:
                kb.release(j)
                sleep(I)
        elif type(i) is str and len(i) > 1:
            for j in i:
                kb.press(j)
                sleep(I)
                kb.release(j)
                sleep(I)
        else:
            if isinstance(i,Key):
                sleep(J)
            kb.press(i)
            sleep(I)
            kb.release(i)
            sleep(I)

def releaseProxyEdge():
    """Disables edge browser using key shortcuts."""
    window=_getWindow('Edge')
    config = [[Key.ctrl,'l'],'edge://settings/?search=proxy',Key.enter, [Key.ctrl,'l'], Key.tab, Key.tab, Key.tab, Key.tab, Key.tab, Key.tab, Key.tab,
              Key.tab, Key.tab, Key.tab, Key.tab, Key.tab,Key.tab,Key.tab,Key.tab,Key.tab,Key.enter, Key.backspace, Key.tab, Key.tab, Key.tab, Key.space, Key.tab, [Key.ctrl, 'a'],'1','2','7','.','0','.','0','.','1', Key.tab,
              [Key.ctrl, 'a'],'8','0','8','1',Key.tab,Key.tab,Key.tab,Key.enter,[Key.alt, Key.f4],[Key.alt, Key.f4]]
    kb = Controller()
    for i in config:
        if type(i) is list:
            for j in i:
                kb.press(j)
                sleep(I)
            for j in i:
                kb.release(j)
                sleep(I)
        elif type(i) is str and len(i) > 1:
            for j in i:
                kb.press(j)
                sleep(I)
                kb.release(j)
                sleep(I)
        else:
            if isinstance(i,Key): sleep(J)
            if i is Key.enter: 
                kb = Controller()
                kb.press(i)
                sleep(J)
            else:
                kb.press(i) 
                sleep(I)
            
            if i is Key.enter: 
                kb.release(i)
                sleep(J)
            else: 
                kb.release(i)
                sleep(I)


def set():
    #_configCert()
    # configurations = {
    #     'edge':ProxyEdge,
    #     'chrome':ProxyChrome,
    #     'firefox':ProxyFirefox
    # }
    configurations = {
        'firefox':ProxyFirefox
    }
    # browsers = {
    # 'edge' : ['Microsoft Edge','Microsoft Edge','Microsoft Edge','msedge.exe'],
    # 'chrome' : ['Google Chrome','Google Chrome', 'Google Chrome','chrome.exe'],
    # 'firefox' : ['Firefox','Firefox','Firefox','firefox.exe']
    # }
    browsers = {
        'firefox' : ['Firefox','Firefox','Firefox','firefox.exe']
    }
    options = ['start_menu','task_bar_path','desktop_path','exec_path']
    attempt = 0
    flag1 = 0
    flag = 0
    user = getUser()

    for key,browser in browsers.items():
        if flag1:
            flag1 = 0
            continue
        attempt = 0
        while attempt < 4:
            if options[attempt] == 'exec_path':
                p = findFile(options[attempt],user,key)
            else:
                p = findFile(options[attempt],user)
            try:
                startExec(browser[attempt],p)
                print("[*] Browser started...")
                flag+=1
                break
            except:
                print("[!] Starting browser Failed...")
                print("[*] Attempting to start browser with {}".format(options[(attempt+1)%len(browser)]))
            attempt += 1 
            if attempt == 4:
                print("[!] All attempts to start {} failed...".format(key))
                print("[*] Attempting next browser...")

            if flag: break
        if flag:
            sleep(2)
            configurations[key]()
            if key == 'edge': flag1=1
            flag=0

def release():
    #_revertCert()
    configurations = {
        'firefox':releaseProxyFirefox
    }
    # configurations = {
    #     'edge':releaseProxyEdge,
    #     'chrome':releaseProxyChrome,
    #     'firefox':releaseProxyFirefox
    # }
    # browsers = {
    # 'edge' : ['Microsoft Edge','Microsoft Edge','Microsoft Edge','msedge.exe'],
    # 'chrome' : ['Google Chrome','Google Chrome', 'Google Chrome','chrome.exe'],
    # 'firefox' : ['Firefox','Firefox','Firefox','firefox.exe']
    # }
    browsers = {
        'firefox' : ['Firefox','Firefox','Firefox','firefox.exe']
    }
    options = ['start_menu','task_bar_path','desktop_path','exec_path']
    attempt = 0
    flag1 = 0
    flag = 0
    user = getUser()

    for key,browser in browsers.items():
        if flag1:
            flag1 = 0
            continue
        attempt = 0
        while attempt < 4:
            if options[attempt] == 'exec_path':
                p = findFile(options[attempt],user,key)
            else:
                p = findFile(options[attempt],user)
            try:
                startExec(browser[attempt],p)
                print("[*] Browser started...")
                flag+=1
                break
            except:
                print("[!] Starting browser Failed...")
                print("[*] Attempting to start browser with {}".format(options[(attempt+1)%len(browser)]))
            attempt += 1 
            if attempt == 4:
                print("[!] All attempts to start {} failed...".format(key))
                print("[*] Attempting next browser...")

            if flag: break
        if flag:
            sleep(2)
            configurations[key]()
            if key == 'edge': flag1=1
            flag=0