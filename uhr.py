#!/usr/bin/python3
#  @filename : uhr.py
#  @brief : Parameter der Uhr einstellen
#  @author : Borys 12 Nov 2025 08 Jun 2020 29 Aug 2019
##
# für Farbe:
# GET /color?r=0&g=68&b=255
#
import socket, time
import sys, requests
from datetime import datetime, date
DESCRIPTION="Tageszeitabhängige Helligkeitssteuerung für die Wordclock"
def main():

    # TCP_IP = 'Uhr.fritz.box'
    # TCP_PORT = 80
    # BUFFER_SIZE = 8
    # MESSAGE=B'GET /brightness?brightness=50'
    # data=B'nichts empfangen'
    heute = datetime.now()
    stunde = heute.timetuple()[3]
    
    if stunde < 8:
        print("keine")
        print("Änderung")
        return
    elif stunde < 9:
        hell = 55
    elif stunde < 10:
        hell = 65
    # elif stunde<11 :hell=75
    elif stunde < 13:
        print("keine")
        print("Änderung")
        return
    elif stunde < 14:
        hell = 90
    elif stunde < 19:
        print("keine")
        print("Änderung")
        return
    elif stunde < 20:
        hell = 70
    elif stunde < 22:
        print("keine")
        print("Änderung")
        return
    elif stunde < 23:
        hell = 60
    else:
        hell = 40
    logging.debug(f"Stunde: {stunde} Helligkeit: {hell}")
    try:
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect((TCP_IP, TCP_PORT))
        # s.send(MESSAGE)
        # data = s.recv(BUFFER_SIZE)
        # payload = {'schluessel1': 'wert1', 'schluessel2': 'wert2'}
        payload = {"brightness": hell}
        farbe = {"r": 101, "g": 99, "b": 100}
        m = requests.get("http://uhr.fritz.box/brightness", params=payload)
        # m=requests.get('http://uhr.fritz.box/color',params=farbe)
        # m=data.decode()
        # print(m)
        # print (m.url)
        logging.info(m.text)
        # print ('OK')
    except ConnectionResetError:
        logging.error("Connect Reset")
    except:
        logging.error("Fehler", (sys.exc_info()))
    # else:
    # m=(data.decode()).split(';')
    # print ('{}\n{}\n{}\nOK'.format(m[0],m[1],m[2]))
    # finally:
    # s.close()
    # print('Ende')

if __name__ == "__main__":
    import argparse, sys,logging
    # Parser-Objekt erstellen
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--verbose','-v', action='store_true', help='Debug-Modus einschalten')
    #------------------------------------------------------------
    # Debug-Modus setzen
    arguments = parser.parse_args()
    Dbg = arguments.verbose
    if Dbg: logging.basicConfig(level=logging.DEBUG)
    else:   logging.basicConfig(level=logging.ERROR)

    main()
