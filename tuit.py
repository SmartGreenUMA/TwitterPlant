import serial, time, datetime
import RPi.GPIO as GPIO
import serial.tools.list_ports

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, True) 
time.sleep(2)
GPIO.output(4, False)
time.sleep(1)
GPIO.output(4, True)
time.sleep(10)

ports=list(serial.tools.list_ports.comports())
port_no = ports[0][0]
print("intentando abrir %s" %port_no)
arduino = serial.Serial(port_no, 9600,timeout=1)
print("Puerto abierto y leido")
         
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

while True:
    x=datetime.datetime.now()
    try:
        read_serial=arduino.readline()
        print("\nLeí bien")
        numero = int(read_serial)
        print(str(numero))
        print("la hora es,", x)

        message1="Que temperatura tan agradable %s:%s:%s" %(x.hour, x.minute, x.second)
        message2="Tengo calor %s:%s:%s" %(x.hour, x.minute, x.second)
        message3="Me estoy asando. En Mordor se estaria mejor %s:%s:%s" %(x.hour, x.minute, x.second)
        message4="Que fresquito hace %s:%s:%s" %(x.hour, x.minute, x.second)
        message5="GUANTES Y BUFANDAS A MI, ME CONGELO %s:%s:%s" %(x.hour, x.minute, x.second)
        message6="Me ahogo, mi amo pretende asesinarme @policia %s:%s:%s" %(x.hour, x.minute, x.second)
        message7="Necesitaria un poco de agua %s:%s:%s" %(x.hour, x.minute, x.second)
        message8="Estoy seca, no estoy preparada para vivir en el desierto. %s:%s:%s" %(x.hour, x.minute, x.second)
        message9="Estoy en condiciones perfectas de la muerte para hacer la fotosintesis, nos leemos luego. %s:%s:%s" %(x.hour, x.minute, x.second)

        if numero==1 :
                print("Tuiteando ", message1)
                twitter.update_status(status=message1)   
        elif numero==2: 
                twitter.update_status(status=message2)
        elif numero==3 :
                twitter.update_status(status=message3)   
        elif numero==4 :
                twitter.update_status(status=message4)
        elif numero==5 :
                twitter.update_status(status=message5)   
        elif numero==6 :
                twitter.update_status(status=message6)
        elif numero==7 : 
                twitter.update_status(status=message7)   
        elif numero==8 :
                twitter.update_status(status=message8)
        elif numero==9 :
                print("Intentando tuitear msg 9");
                twitter.update_status(status=message9)
                print("Tuiteando ", message9)
        else:
            print("ERROR")
                
        print("Tuit enviado")
    except:
        print("Error conectándome a la planta")
 #       arduino.close()
