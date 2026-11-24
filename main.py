"""Dad Joke Showdown — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a single dad joke, at most 200 characters.
"""
import os

LINE = "I told my computer I needed a break, and now it won't stop sending me KitKat ads."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
