#!/usr/bin/python3
#  @filename : uhr.py
#  @brief : Parameter der Uhr einstellen
#  @author : Borys 18 Dez 12 Nov 2025 08 Jun 2020 29 Aug 2019
##
# für Farbe:
# GET /color?r=0&g=68&b=255
#
import logging, sys, requests
from datetime import datetime

DESCRIPTION = "Tageszeitabhängige Helligkeitssteuerung für die Wordclock"


def main():

    heute = datetime.now()
    stunde = heute.timetuple()[3]

    if stunde < 8:
        hell = -1
    elif stunde < 9:
        hell = 55
    elif stunde < 10:
        hell = 65
    elif stunde < 11:
        hell = 75
    elif stunde < 13:
        hell = -1
    elif stunde < 14:
        hell = 90
    elif stunde < 19:
        hell = -1
    elif stunde < 20:
        hell = 70
    elif stunde < 22:
        hell = -1
    elif stunde < 23:
        hell = 60
    else:
        hell = 40
    if hell < 0:
        logging.debug(f"Stunde: {stunde} keine Änderung")
    else:
        logging.debug(f"Stunde: {stunde} Helligkeit: {hell}")
        try:
            # payload = {'schluessel1': 'wert1', 'schluessel2': 'wert2'}
            payload = {"brightness": hell}
            farbe = {"r": 101, "g": 99, "b": 100}
            m = requests.get("http://uhr.fritz.box/brightness", params=payload)
            logging.debug(f"Uhr antwortet: {m.text}")
        except ConnectionResetError:
            logging.exception("Connect Reset")
        except Exception as e:
            logging.fatal("Fehler")
            print(e)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Debug-Modus einschalten"
    )
    arguments = parser.parse_args()
    if arguments.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)

    main()
