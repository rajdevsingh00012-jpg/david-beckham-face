from PIL import Image
import numpy as np

# Load image
img = Image.open("chomsky.png").convert("L")
img = img.resize((100,130))

pixels = np.array(img)

# Convert grayscale to binary (0/1)
binary = (pixels < 140).astype(int)   # dark = 1, light = 0

# Draw in terminal
for row in binary:
    print("".join(map(str, row)))

# Save to file also
with open("binary_portrait.txt","w") as f:
    for row in binary:
        f.write("".join(map(str,row)) + "\n")

print("\nSaved as binary_portrait.txt")














# from PIL import Image
# import numpy as np
# from colorama import init, Fore, Style
# init()

# # Dark to light characters
# DENSITY = "@#W$9876543210?!abc;:+=-,._ "

# # Load image
# img = Image.open("chomsky.png").convert("L")
# img = img.resize((90,120))

# pixels = np.array(img)

# ascii_art = ""

# for row in pixels:
#     line = ""
#     for px in row:
#         ch = DENSITY[int(px / 255 * (len(DENSITY)-1))]
#         line += Fore.GREEN + ch
#         ascii_art += ch
#     print(line)
#     ascii_art += "\n"

# print(Style.RESET_ALL)

# # Save to file
# with open("terminal_portrait.txt","w") as f:
#     f.write(ascii_art)

# print("\nSaved as terminal_portrait.txt")
