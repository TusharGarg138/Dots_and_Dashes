import tkinter as tk
from tkinter import font

# Morse code dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

# Functions
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT.get(letter.upper(), '') + ' '
        else:
            cipher += ' '
    return cipher

def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    space_count = 0

    for letter in message:
        if letter != ' ':
            space_count = 0
            citext += letter
        else:
            space_count += 1
            if space_count == 2:
                decipher += ' '
            elif citext:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher

def encode_text():
    input_text = entry.get()
    result = encrypt(input_text)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, result)

def decode_text():
    input_text = entry.get()
    result = decrypt(input_text)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, result)

# GUI setup
root = tk.Tk()
root.title("Morse Code Converter")
root.geometry("500x400")
root.configure(bg="#1e1e2f")  # Dark background

# Fonts
title_font = font.Font(family="Helvetica", size=20, weight="bold")
btn_font = font.Font(family="Arial", size=12, weight="bold")

# Title
title = tk.Label(root, text="Morse Code Converter", font=title_font, fg="#00ffd5", bg="#1e1e2f")
title.pack(pady=20)

# Input Field
entry = tk.Entry(root, width=45, font=("Arial", 12), bg="#2d2d44", fg="#ffffff", insertbackground='white', borderwidth=2, relief="solid")
entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack()

encode_btn = tk.Button(btn_frame, text="Encrypt 🔐", font=btn_font, bg="#007acc", fg="white", padx=20, pady=5, bd=0, relief="ridge", command=encode_text)
encode_btn.grid(row=0, column=0, padx=10)

decode_btn = tk.Button(btn_frame, text="Decrypt 🔓", font=btn_font, bg="#5c2d91", fg="white", padx=20, pady=5, bd=0, relief="ridge", command=decode_text)
decode_btn.grid(row=0, column=1, padx=10)

# Output Box
output_box = tk.Text(root, height=6, width=55, font=("Arial", 12), bg="#2d2d44", fg="#ffffff", wrap="word", borderwidth=2, relief="solid")
output_box.pack(pady=20)

