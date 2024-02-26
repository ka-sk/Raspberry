import os
from random import randint
from time import sleep, perf_counter

from gpiozero import LED, Button

from player import Player
from timer import Timer

from os import system

# number of players
NO_OF_PLAYERS = 2
STARTING_DIODE_PIN = 2
ROUND_DIODE_PIN = 3
EXIT_BUTTON_PIN = 4
ROUND_TIME = 2

# list of gpio numbers for each player.
LIST_OF_PINS = [21, 14]

# If length of list isn't equal to no of players it prints error
if len(LIST_OF_PINS) != NO_OF_PLAYERS:
    print("ERROR\nDifference in pins and no of players")
    exit()

# initialization of list of players based on list of pins
player_list = [Player(x) for x in LIST_OF_PINS]


# initialization of starting and round LEDs
starting_diode = LED(STARTING_DIODE_PIN)
round_diode = LED(ROUND_DIODE_PIN)
exit_button = Button(EXIT_BUTTON_PIN)

round_counter = 0

if_round_on = False

##############################################################################
# FUNCTIONS SEGMENT


def game_init():
    system('clear')
    sleep(1)
    print("Hey...")
    sleep(0.5)
    print("You wanna play a game?")
    sleep(0.5)
    print("( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)")
    sleep(2)
    print("LET'S PLAAAAYYYYY")
    pass


def round_initialization(p_list, r_counter):

    global round_diode

    system("clear")
    print(f"Round {r_counter}")
    sleep(1)
    print("\nGET READY")

    sleep(randint(1, 10))
    print("\nNOW")
    round_diode.on()

    init_time = perf_counter()
    for x in p_list:
        x.round_init(init_time)
    pass


def round_end():
    global ROUND_TIME
    timer = Timer()
    while True in [x.is_round_on() for x in player_list]:
        if not timer.not_passed(ROUND_TIME):
            print("WOOPS")
            sleep(0.5)
            print("BE BETTER NEXT TIME")
            sleep(0.5)
            print("...")
            sleep(0.5)
            print("SLOWPOKE... ಠ╭╮ಠ")
            break
        pass
    pass


def results():
    global player_list
    player_counter = 0
    for i in player_list:
        player_counter += 1
        i = i.show_results()

        print("------------")
        print(f"Player {player_counter}:")
        print("------------", end='\n\n')
        print(f"mean time: {i['mean time']}")
        print(f"points: {i['points']}")
        print(f"falstarts: {i['falstarts']}")

        sleep(1)


def exit_programme():
    global starting_diode
    global round_diode

    results()

    x = input("\n\n NIIIIIICE!")

    starting_diode.off()
    round_diode.off()

    exit()

##############################################################################
# MAIN


starting_diode.blink(0.5, 0.5, 3, False)

exit_button.when_activated = exit_programme

game_init()

while True:

    round_counter += 1

    round_initialization(player_list, round_counter)
    round_end()
    round_diode.off()

    sleep(5)
    pass

starting_diode.off()
round_diode.off()
exit()

