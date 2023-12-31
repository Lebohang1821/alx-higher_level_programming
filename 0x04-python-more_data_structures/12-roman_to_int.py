#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    numb = 0
    las_rom = 0

    for ch in roman_string:
        if ch in rom_n:
            current_value = rom_n[ch]
            if current_value <= las_rom:
                numb += current_value
            else:
                numb += current_value - 2 * las_rom
            las_rom = current_value

    return (numb)
