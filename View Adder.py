import threading, requests, random, os
os.system("title 𝙂𝙄𝙏𝙃𝙐𝘽 𝙋𝙍𝙊𝙁𝙄𝙇𝙀 𝙑𝙄𝙀𝙒 𝘼𝘿𝘿𝙀𝙍"); os.system("cls")

# Example of link : https://camo.githubusercontent.com/0464ddf5c8b77ac9f8f09e523218f34b1b1232d1b2488de484d0bb9b8521fd6f/68747470733a2f2f70726f66696c652d636f756e7465722e676c697463682e6d652f25374276656e617879742537442f636f756e742e737667
link = input(" \033[94m[>] \033[38;2;100;90;255mProfile view plug-in link : ")

# The threads doesn't work with "def view(link)" and "threading.Thread(target=view(link)).start()", it will start you one thread and no more.
def view():
    while True:
        try:
            git = requests.get(link)
            print(f"\033[38;2;{random.randint(50,255)};{random.randint(50,255)};{random.randint(50,255)}m [<] API Response  : {git.status_code}")
        except:
            pass

for x in range(os.cpu_count()):
    threading.Thread(target=view).start()
