# Discord Plain Text To Emote Converter

Convert `Plain text` to `:P_ps2p::L_ps2p::A_ps2p::I_ps2p::N_ps2p::_space_ps2p::T_ps2p::E_ps2p::X_ps2p::T_ps2p:`

# DISCLAIMER

You need nitro to use this in servers outside the one storing the emotes! Also, this is intended for people who have custom servers set up with individual font characters as emotes.

# HOW TO SET UP

Make a new json file, then format it like this:

```json
    "case_sensetive": false,
    "characters": {
        "A": "my_custom_A_font_emote_name",
        "B": "my_custom_B_font_emote_name"
    }
```

Then go into `emoji_keyboard.py` and change the first line to be:
`KEYBOARD_MAP = "path/to/your/json/file.json"`
