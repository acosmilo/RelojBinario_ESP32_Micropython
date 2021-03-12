# Server Reloj

import machine
import time
import network
import socket

h=11
m=8
rtc = machine.RTC()
#rtc.datetime((2021, 3, 9, 1, h, m, 50, 0)) # set a specific date and time
#rtc.datetime() # get date and time
led = machine.Pin(15, machine.Pin.OUT)

#g19
a = machine.Pin(19, machine.Pin.OUT)

#g18
b = machine.Pin(18, machine.Pin.OUT)

#g5
c = machine.Pin(5, machine.Pin.OUT)

#g17
d = machine.Pin(17, machine.Pin.OUT)

#g16
e = machine.Pin(16, machine.Pin.OUT)

#g4
f = machine.Pin(4, machine.Pin.OUT)

#g2
g = machine.Pin(2, machine.Pin.OUT)


#Defino el boton
boton = machine.Pin(14, machine.Pin.IN)

#Defino el boton para iniciar coneccion
boton_conex = machine.Pin(27, machine.Pin.IN)

#Defino una bandera para salir del bucle
flag=1

#Funcion para conectarse a la red
def do_connect():

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('galaci', 'miaumiau')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

#Esta funcion la cree porque esta con logica negativa el boton
def NotBoton(arg):
    if arg==1:
        return 0
    else:
        return 1

def ApagoTodo():
    a.off()
    b.off()
    c.off()
    d.off()
    e.off()
    f.off()
    g.off()

def ImprimeHora(arg):
    if arg==0:
        ApagoTodo()
    elif arg==1:
        a.value(boton.value())
    elif arg==2:
        b.value(boton.value())
    elif arg==3:
        a.value(boton.value())
        b.value(boton.value())
    elif arg==4:
        f.value(boton.value())
    elif arg==5:
        f.value(boton.value())
        a.value(boton.value())
    elif arg==6:
        f.value(boton.value())
        b.value(boton.value())
    elif arg==7:
        f.value(boton.value())
        b.value(boton.value())
        a.value(boton.value())
    elif arg==8:
        g.value(boton.value())
    elif arg==9:
        g.value(boton.value())
        a.value(boton.value())
    #10-19
    elif arg==10:
        c.value(boton.value())
    elif arg==11:
        #Mas significativo
        c.value(boton.value())
        #Menos significativo reloj
        a.value(boton.value())
    elif arg==12:
        #Mas significativo
        c.value(boton.value())
        #Menos significativo reloj
        b.value(boton.value())
    elif arg==13:
        #Mas significativo
        c.value(boton.value())
        #Menos significativo reloj
        a.value(boton.value())
        b.value(boton.value())
    elif arg==14:
        #Mas significativo
        c.value(boton.value())
        #Menos significativo reloj
        f.value(boton.value())
    elif arg==15:
        #Mas significativo
        c.value(boton.value())
        #Menos significativo reloj
        f.value(boton.value())
        a.value(boton.value())
    elif arg==16:
        #Mas significativo
        c.value(boton.value())
        #Menos significativo reloj
        f.value(boton.value())
        f.value(boton.value())
        b.value(boton.value())
    elif arg==17:
        #Mas significativo
        c.value(boton.value())
        #Menos significativo reloj
        f.value(boton.value())
        b.value(boton.value())
        a.value(boton.value())
    elif arg==18:
        #Mas significativo
        c.value(boton.value())
        #Menos significativo reloj
        g.value(boton.value())
    elif arg==19:
        #Mas significativo
        c.value(boton.value())
        #Menos significativo reloj
        g.value(boton.value())
        a.value(boton.value())
    elif arg==20:
        e.value(boton.value())
    elif arg==21:
        #Mas significativo
        e.value(boton.value())
        #Menos significativo reloj
        a.value(boton.value())
    elif arg==22:
        #Mas significativo
        e.value(boton.value())
        #Menos significativo reloj
        b.value(boton.value())

    elif arg==23:
        e.value(boton.value())
        b.value(boton.value())
        a.value(boton.value())

    print("ImprimeHora al servicio")

def ImprimeMinuto(arg):
    if arg==0:
        ApagoTodo()
    elif arg==1:
        a.value(NotBoton(boton.value()))
    elif arg==2:
        b.value(NotBoton(boton.value()))
    elif arg==3:
        a.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
    elif arg==4:
        f.value(NotBoton(boton.value()))
    elif arg==5:
        f.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    elif arg==6:
        f.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
    elif arg==7:
        f.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    elif arg==8:
        g.value(NotBoton(boton.value()))
    elif arg==9:
        g.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    #10-19
    elif arg==10:
        c.value(NotBoton(boton.value()))
    elif arg==11:
        #Mas significativo
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        a.value(NotBoton(boton.value()))
    elif arg==12:
        #Mas significativo
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        b.value(NotBoton(boton.value()))
    elif arg==13:
        #Mas significativo
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        a.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
    elif arg==14:
        #Mas significativo
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
    elif arg==15:
        #Mas significativo
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    elif arg==16:
        #Mas significativo
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        f.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
    elif arg==17:
        #Mas significativo
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    elif arg==18:
        #Mas significativo
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        g.value(NotBoton(boton.value()))
    elif arg==19:
        #Mas significativo
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        g.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))

    #20-29
    elif arg==20:
        e.value(NotBoton(boton.value()))
    elif arg==21:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        #Menos significativo reloj
        a.value(NotBoton(boton.value()))
    elif arg==22:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        #Menos significativo reloj
        b.value(NotBoton(boton.value()))
    elif arg==23:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        #Menos significativo reloj
        a.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
    elif arg==24:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
    elif arg==25:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    elif arg==26:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        f.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
    elif arg==27:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    elif arg==28:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        #Menos significativo reloj
        g.value(NotBoton(boton.value()))
    elif arg==29:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        #Menos significativo reloj
        g.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))

    #30-39
    elif arg==30:
        e.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
    elif arg==31:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        a.value(NotBoton(boton.value()))
    elif arg==32:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        b.value(NotBoton(boton.value()))
    elif arg==33:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        a.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
    elif arg==34:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
    elif arg==35:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    elif arg==36:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        f.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
    elif arg==37:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    elif arg==38:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        g.value(NotBoton(boton.value()))
    elif arg==39:
        #Mas significativo
        e.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        g.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))

    #40-49
    elif arg==40:
        d.value(NotBoton(boton.value()))
    elif arg==41:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        #Menos significativo reloj
        a.value(NotBoton(boton.value()))
    elif arg==42:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        #Menos significativo reloj
        b.value(NotBoton(boton.value()))
    elif arg==43:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        #Menos significativo reloj
        a.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
    elif arg==44:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
    elif arg==45:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    elif arg==46:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        f.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
    elif arg==47:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    elif arg==48:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        #Menos significativo reloj
        g.value(NotBoton(boton.value()))
    elif arg==49:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        #Menos significativo reloj
        g.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))

    #50-59
    elif arg==50:
        d.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
    elif arg==51:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        a.value(NotBoton(boton.value()))
    elif arg==52:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        b.value(NotBoton(boton.value()))
    elif arg==53:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        a.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
    elif arg==54:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
    elif arg==55:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    elif arg==56:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        f.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
    elif arg==57:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        f.value(NotBoton(boton.value()))
        b.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    elif arg==58:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        g.value(NotBoton(boton.value()))
    elif arg==59:
        #Mas significativo
        d.value(NotBoton(boton.value()))
        c.value(NotBoton(boton.value()))
        #Menos significativo reloj
        g.value(NotBoton(boton.value()))
        a.value(NotBoton(boton.value()))
    print("ImprimeMinuto al servicio")

do_connect()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))

while True:

    if NotBoton(boton_conex.value())==0:
        flag=1
        lista=rtc.datetime()
        hora=lista[4]
        minuto=lista[5]
        print(lista)# Escribe tu código aquí :-)
        print(hora)
        print(minuto)


        for i in range(10):
            led.on()
            time.sleep_ms(200)
            led.off()
            time.sleep_ms(800)
        #print(NotBoton(boton.value()))
        #a.value(NotBoton(boton.value()))
            if NotBoton(boton.value())==0:
                ApagoTodo()
                ImprimeHora(hora)
            else:
                ApagoTodo()
                ImprimeMinuto(minuto)

    elif NotBoton(boton_conex.value())==1:
        ApagoTodo()
        d.value(NotBoton(boton_conex.value()))
        g.value(NotBoton(boton_conex.value()))
        a.value(NotBoton(boton_conex.value()))

        while flag==1:


            s.listen(5)


            conexion, addr = s.accept()
            print(" nueva conexion")
            print(addr)
            peticion = conexion.recv(1024)
            peticion2 = conexion.recv(1024)
            #peticion3 = conexion.recv(1024)
            print(peticion)
            print(peticion2)
            #print(peticion3)
            peticion = peticion.decode()
            peticion2 = peticion2.decode()
            #peticion3 = peticion3.decode()
            h=int(peticion)
            m=int(peticion2)
            #flag=int(peticion3)

            print("La hora es ", h)
            print("El minuto es ",m)
            conexion.send("Su seteo la hora")

            conexion.close()
            rtc.datetime((2021, 3, 9, 1, h, m, 50, 0))
            flag=0

        e.value(NotBoton(boton_conex.value()))
        c.value(NotBoton(boton_conex.value()))
        f.value(NotBoton(boton_conex.value()))
        b.value(NotBoton(boton_conex.value()))
