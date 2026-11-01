import os
import time

os.system("")  # lets Windows terminals understand the cursor-moving codes below

WIDTH = 20

print("Loading...")
print()

for i in range(WIDTH + 1):
    filled = "█" * i
    empty = "░" * (WIDTH - i)
    percent = i * 5

    print("    ┌" + "─" * WIDTH + "┐")
    print("   ╱" + " " * WIDTH + "╱│")
    print("  ┌" + "─" * WIDTH + "┐ │")
    print("  │" + filled + empty + "│ │")
    print("  └" + "─" * WIDTH + "┘╱")
    print("   " + str(percent) + "%")

    if i < WIDTH:
        print("\033[6A", end="")  # move the cursor up 6 lines to redraw
    time.sleep(0.15)

print()
print("Welcome!")