# Matheus Angelicio

from wifi_lib import conecta
import urequests
import dht
import machine
import time

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

# variavel "d" faz referencia ao medidor.
# variavel "r" faz referencia ao relé.

while True:
    print ("Conectando...")
    station = conecta("linksys","17041970")
    if not station.isconnected():
        print("Não conectado")
    else :
        d.measure()
        print("Conectado!!!")
        print("Acessando o site...")
        resposta = urequests.get("https://api.thingspeak.com/update?api_key=KJVVI069DX4DVDG2&field1={}&field2={}".format(d.temperature(), d.humidity()))
        resposta.close()
        print("Página acessada:")
        print("Temperatura {}  Umidade {}".format(d.temperature(), d.humidity()))
                                    
        if d.temperature() >21 or d.humidity() > 70 :
            r.value(1)
        else:
            r.value(0)
            
    time.sleep(23)
    