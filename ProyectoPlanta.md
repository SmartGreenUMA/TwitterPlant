#include <DHT11.h>
  
const int pinTemperatura=8;
const int pinHumedad = A0;
const int pinLuminosidad=A1;
DHT11 dht11(pinTemperatura);

int TipMensjTemp=0;
int TipMensjHum=0;
int TipMensjLuz=0;

void setup()
   {
       Serial.begin(9600);
       pinMode(13,OUTPUT);
       digitalWrite(13,HIGH);
       delay(1000);
   }

void loop()
   {
       digitalWrite(13,LOW);
       int err;
       float temp, hum;
       int humedad = analogRead(pinHumedad);
       int luminosidad = analogRead(pinLuminosidad);
       Serial.print("humedad: "); Serial.println(humedad);
       Serial.print("Temperatura: "); Serial.println(temp);
       Serial.print("Luminosidad: "); Serial.println(luminosidad);
       if((err = dht11.read(hum, temp)) == 0)    // Si devuelve 0 es que ha leido bien
          {
            Serial.println(10);//Pruebaaaaaaaaaaaaaaaaaaasssss
            if((temp>=17) && (temp<26) && (TipMensjTemp != 1)){
              TipMensjTemp=1;
               Serial.println(1);
            }else if((temp>26) && (temp<34) && (TipMensjTemp != 2)){
              TipMensjTemp=2;
               Serial.println(2);
            }else if(temp>34 && (TipMensjTemp !=3)){
              TipMensjTemp=3;
               Serial.println(3);
            }else if((temp<17) && (temp>8) && (TipMensjTemp !=4)){
              TipMensjTemp=4;
               Serial.println(4);
            }else if(temp<8 && (TipMensjTemp !=5)){
              TipMensjTemp=5;
               Serial.println(5);
            }
          }

       if(humedad<=100  && (TipMensjHum !=6)){
          TipMensjHum=6;
           Serial.println(6);
       }else if((humedad>750) && (humedad<900)  && (TipMensjHum !=7)){
          TipMensjHum=7;
           Serial.println(7);
       }else if(humedad>=900  && (TipMensjHum !=8)){
          TipMensjHum=8;
           Serial.println(8);
       }

       if(luminosidad>900){
          if(TipMensjLuz !=9){
              TipMensjLuz=9;
              Serial.println(9);
          }
       }else{
          TipMensjLuz=0;
       }

        
       delay(1000);            //Recordad que solo lee una vez por segundo
   }
