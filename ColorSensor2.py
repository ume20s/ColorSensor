import serial
import time
import subprocess

thre=80

def main():
    con = serial.Serial('/dev/ttyS8', 9600)
    time.sleep(2)
    print(con.portstr)
    str=con.readline()
    while 1:
        str=con.readline()
        rgb = str.split()
        print(rgb)
        r = int(rgb[0])
        g = int(rgb[1])
        b = int(rgb[2])
        if r<thre and g<thre and b>thre:
            print("BLUE")
            subprocess.call("aplay ao.wav", shell=True)
        if r>thre and g<thre and b<thre:
            print("RED")
            subprocess.call("aplay aka.wav", shell=True)
        if r>thre and g<thre and b>thre:
            print("PURPLE")
            subprocess.call("aplay murasaki.wav", shell=True)
        if r<thre and g>thre and b<thre:
            print("GREEN")
            subprocess.call("aplay midori.wav", shell=True)
        if r<thre and g>thre and b>thre:
            print("LIGHT BLUE")
            subprocess.call("aplay mizuiro.wav", shell=True)
        if r>thre and g>thre and b<thre:
            print("YELLOW")
            subprocess.call("aplay kiiro.wav", shell=True)

if __name__ == '__main__':
    main()
