import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt)
        if option1 in response or option2 in response:
            return response


def intro(enemy):
    print_pause('\nYou find yourself standing in an open field,'
                'filled with grass and yellow wildflowers.')
    print_pause(f'Rumor has it that a {enemy} is somewhere around here,'
                'and has been terrifying the nearby village.')
    print_pause('In front of you is a house.')
    print_pause('To your right is a dark cave.')
    print_pause('In your hand you hold your trusty '
                '(but not very effective) dagger.')


def house(enemy):
    print_pause('\nYou approach the door of the house.')
    print_pause('You are about to knock when the door opens '
                'and out steps a ' + enemy + '.')
    print_pause(f'Eep! This is the {enemy}\'s house!')
    print_pause(f'The {enemy} attacks you!')
    print_pause('You feel a bit under-prepared for this, '
                'what with only having a tiny dagger.')


def cave(sword):
    print_pause('\nYou peer cautiously into the cave.')
    if sword is False:
        print_pause('It turns out to be only a very small cave.')
        print_pause('Your eye catches a glint of metal behind a rock.')
        print_pause('You have found the magical Sword of Ogoroth!')
        print_pause('You discard your silly old dagger '
                    'and take the sword with you.')
        print_pause('You walk back out to the field.')
    else:
        print_pause('You\'ve been here before, and gotten all the good stuff.'
                    'It\'s just an empty cave now.')
        print_pause('You walk back out to the field.')
    return True


def field():
    print_pause('\nYou run back into the field. Luckily, '
                'you don\'t seem to have been followed.')


def win(enemy):
    print_pause(f'\nAs the {enemy} moves to attack, '
                'you unsheath your new sword.')
    print_pause('The Sword of Ogoroth shines brightly in your hand '
                'as you brace yourself for the attack.')
    print_pause(f'But the {enemy} takes one look at your shiny new toy '
                'and runs away!')
    print_pause(f'You have rid the town of the {enemy}. You are victorious!')
    choose_play_again()


def lose(enemy):
    print_pause('\nYou do your best...')
    print_pause(f'but your dagger is no match for the {enemy}.')
    print_pause('You have been defeated!')
    choose_play_again()


def choose_location(sword, enemy):
    while True:
        print_pause('\nEnter 1 to knock on the door of the house.')
        print_pause('Enter 2 to peer into the cave.')
        print_pause('What would you like to do?')
        response = valid_input('(Please enter 1 or 2.)\n', '1', '2')
        if '1' in response:
            house(enemy)
            choose_action(sword, enemy)
            break
        elif '2' in response:
            sword = cave(sword)


def choose_action(sword, enemy):
    response = valid_input('Would you like to (1) fight '
                           'or (2) run away?\n', "1", "2")
    while True:
        if '1' in response:
            if sword is False:
                lose(enemy)
                break
            else:
                win(enemy)
                break
        elif '2' in response:
            field()
            choose_location(sword, enemy)
            break


def choose_play_again():
    response = valid_input('Would you like to play again? (y/n)\n', 'y', 'n')
    while True:
        if 'y' in response:
            print_pause('\nExcellent! Restarting the game ...')
            play_game()
            break
        elif 'n' in response:
            print_pause('\nThanks for playing! See you next time.')
            break


# the main function which starts the game
def play_game():
    enemies = ['troll', 'pirate', 'gorgon', 'demon']
    enemy = random.choice(enemies)
    sword = False
    intro(enemy)
    choose_location(sword, enemy)


play_game()
