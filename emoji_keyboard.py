

KEYBOARD_MAP = "emote_keyboard_maps/press_start_2P.json"
NON_CLOSEOPEN_CHARACTERS = [" "]








from termcolor import colored
import json
import clipboard
from colorama import Fore, Back, Style

og_message = input("Enter the message you want to convert to emojis:\n")

with open(KEYBOARD_MAP, 'r') as f:
    json_data = json.loads(f.read())
    
if "case_sensetive" in json_data.keys():
    case_sensetive = json_data["case_sensetive"]
else:
    case_sensetive = False
    
char_map = json_data["characters"]
char_plains = list(char_map.keys())
char_emotes = list(char_map.values())

final_message = ""
missing_chars = []

if not case_sensetive:
    og_message = [c.lower() for c in og_message]
    for c in char_plains:
        char_map[c.lower()] = char_map[c]
    char_plains = [c.lower() for c in char_plains]
    
    
for c in range(len(og_message)):
    char = og_message[c]
    
    new_char = ""
    missing = False
    
    if (char in char_plains) or (not case_sensetive and char.lower() in char_plains):
        new_char = char_map[char]
    elif char + "_open" in char_plains and char + "_close" in char_plains:
        if (c > 0 and og_message[c - 1] in NON_CLOSEOPEN_CHARACTERS) or c == 0:
            new_char = char_map[char + "_open"]
        else:
            new_char = char_map[char + "_close"]
    else:
        missing = True
    
    if not missing:
        final_message += f":{new_char}:"
    else:
        final_message += char
        if not char in missing_chars: missing_chars.append(char)
    

print("\n\n")
print(Style.BRIGHT + "Final message:\n" + Fore.GREEN + final_message)
print(Style.RESET_ALL)

if len(missing_chars) > 0:
    error_message = ""
    offset = 0
    for char in og_message:
        if char in missing_chars:
            error_message += f"{Fore.YELLOW}{Back.RED}" + char + Style.RESET_ALL
        else:
            error_message += char

    print("\n\n")
    print(colored('WARNING: At least one of the characters in your text does not have a cooresponding emote in the map you selected!', 'red'))
    print(error_message)
else:
    copy_answer = input("\n\nCopy to clipboard? (y/n)> ")
    if copy_answer.lower() == "y":
        clipboard.copy(final_message)
print(Style.RESET_ALL)
