from os import system as run

run("wmctrl -a Exanima -b add,above")
keyboard.send_key("p")
run("wmctrl -a Exanima -b remove,above")
