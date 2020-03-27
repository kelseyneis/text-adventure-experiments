import time, keyboard
import world, asciiArt
from player import Player

# asciiArt.handle_image_conversion('https://i.ytimg.com/vi/WXJ3cyeuhYU/hqdefault.jpg')
def slowPrint(text):
    for letter in text:
        print(letter, end='', flush=True)
        if not keyboard.is_pressed('enter'):
            time.sleep(.05)
        else:
            time.sleep(0)
    keyboard.release('enter')
    time.sleep(1)

def play():
    world.load_tiles()
    player = Player()
    room = world.tile_exists(player.location_x, player.location_y)
    slowPrint(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("What do you want to do:")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
    play()
