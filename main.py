# time_machine.py
# A very serious and scientifically accurate time machine. Definitely.
# (Warning: May only move you through time at a rate of 1 second per second.)

import time

class TimeMachine:
    def __init__(self):
        print("🕰️ Initializing Time Machine...")
        print("⚙️  Calibrating flux capacitor… (100% imaginary)")
        print("⚡ Charging time coils… Done!")
        print("🚀 Ready for time travel!")

    def travel(self, seconds):
        if seconds == 0:
            print("You chose to stay in the present. Bold!")
            return

        direction = "future" if seconds > 0 else "past"
        print(f"\nPreparing to travel {abs(seconds)} second(s) into the {direction}...")
        time.sleep(1)
        print("Engaging temporal thrusters...")

        # Yes, this is the joke.
        time.sleep(abs(seconds))
        print(f"✨ You have arrived {abs(seconds)} second(s) into the {direction}.")
        print("Hope nothing paradoxical happened!")

if __name__ == "__main__":
    tm = TimeMachine()
    print("\nWelcome, Time Traveler!")
    t = int(input("Enter seconds to travel (positive = future, negative = past): "))
    tm.travel(t)
