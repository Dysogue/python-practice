import time

print("Loading...")

for i in range(21):
    bar = "█" * i + "-" * (20 - i)
    percent = i * 5
    print("\r[" + bar + "] " + str(percent) + "%", end="")
    time.sleep(0.15)

print()
print("Done! Welcome!")