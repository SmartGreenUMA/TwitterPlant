import serial, time, datetime
import RPi.GPIO as GPIO
import serial.tools.list_ports

time.sleep(15) ##Se espera 15 segundos al arrancar el sistema para que de tiempo a los puertos para configurarse antes de conectarlos

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

        message1="Qué temperatura tan agradable %s:%s:%s" %(x.hour, x.minute, x.second)
        message2="Tengo calor %s:%s:%s" %(x.hour, x.minute, x.second)
        message3="Me estoy asando. En Mordor se estaría mejor %s:%s:%s" %(x.hour, x.minute, x.second)
        message4="Qué fresquito hace %s:%s:%s" %(x.hour, x.minute, x.second)
        message5="Qué frio!! Pues no parece que estoy robando pingüinos %s:%s:%s" %(x.hour, x.minute, x.second)
        message6="Me ahogo, mi amo pretende asesinarme, socorroooo!! %s:%s:%s" %(x.hour, x.minute, x.second)
        message7="Necesitaría un poco de agua!! Algún tuitero seria tan amable de regarme :) %s:%s:%s" %(x.hour, x.minute, x.second)
        message8="Estoy seca, no estoy preparada para vivir en el desierto. Regadme por favor!!! %s:%s:%s" %(x.hour, x.minute, x.second)
        message9="Estoy en condiciones perfectas para hacer la fotosíntesis, nos leemos luego. %s:%s:%s" %(x.hour, x.minute, x.second)

        if numero==1 :
                twitter.update_status(status=message1)
                print("Tuiteando ", message1)
        elif numero==2:
                twitter.update_status(status=message2)
                print("Tuiteando ", message2)
        elif numero==3 :
                twitter.update_status(status=message3)
                print("Tuiteando ", message3)
        elif numero==4 :
                twitter.update_status(status=message4)
                print("Tuiteando ", message4)
        elif numero==5 :
                twitter.update_status(status=message5)
                print("Tuiteando ", message5)
        elif numero==6 :
                twitter.update_status(status=message6)
                print("Tuiteando ", message6)
        elif numero==7 :
                twitter.update_status(status=message7)
                print("Tuiteando ", message7)
        elif numero==8 :
                twitter.update_status(status=message8)
                print("Tuiteando ", message8)
        elif numero==9 :
                twitter.update_status(status=message9)
                print("Tuiteando ", message9)
        else:
            print("ERROR")
                
    except:
        print("Error conectándome a la planta")
