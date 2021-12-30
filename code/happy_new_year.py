from datetime import datetime
from time import sleep
from pyfiglet import Figlet
import os

def draw_happy_new_year():
    print("=" * 100);
    f = Figlet(font = "banner3");
    print(f.renderText('* 2022 *'))
    print(f.renderText('HAPPY NEW YEAR'))
    print("=" * 100);


if __name__ == "__main__":
    while(True):
        now = str(datetime.now()).split('.')[0]
        if now == '2022-01-01 00:00:00':
            print(now)
            draw_happy_new_year()
            break
        print(now)
        sleep(1)
        os.system('clear')