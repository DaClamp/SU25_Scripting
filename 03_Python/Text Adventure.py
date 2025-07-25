# Author: Anthony
# Description: A small text adventure game where the player explores a mysterious forest.
# The player makes choices at each stage to survive and uncover secrets.
# Includes a minimum of 10 prompts for user interaction.

def intro():
    print("🌲 Welcome to 'The Whispering Woods' 🌲")
    print("You are a brave explorer venturing into a mysterious forest.")
    print("Make careful choices — your survival depends on it!\n")

def prompt1():
    print("1. You arrive at the edge of the forest. Do you:")
    print("   a) Enter the forest.")
    print("   b) Turn back.")
    return input("Your choice: ").strip().lower()

def prompt2():
    print("\n2. The forest is dark and quiet. You see a path split. Do you:")
    print("   a) Go left toward a glowing mushroom patch.")
    print("   b) Go right toward the sound of water.")
    return input("Your choice: ").strip().lower()

def prompt3():
    print("\n3. You find a strange book on the ground. Do you:")
    print("   a) Pick it up.")
    print("   b) Ignore it and keep walking.")
    return input("Your choice: ").strip().lower()

def prompt4():
    print("\n4. A talking fox appears. It offers to guide you. Do you:")
    print("   a) Follow the fox.")
    print("   b) Run away.")
    return input("Your choice: ").strip().lower()

def prompt5():
    print("\n5. The fox leads you to a hidden cave. Do you:")
    print("   a) Enter the cave.")
    print("   b) Stay outside.")
    return input("Your choice: ").strip().lower()

def prompt6():
    print("\n6. Inside the cave, you find a glowing sword. Do you:")
    print("   a) Take the sword.")
    print("   b) Leave it alone.")
    return input("Your choice: ").strip().lower()

def prompt7():
    print("\n7. A troll blocks your path. Do you:")
    print("   a) Fight the troll.")
    print("   b) Offer the troll food.")
    return input("Your choice: ").strip().lower()

def prompt8():
    print("\n8. The troll lets you pass. You find a treasure chest. Do you:")
    print("   a) Open it.")
    print("   b) Walk past it.")
    return input("Your choice: ").strip().lower()

def prompt9():
    print("\n9. A storm begins outside. You see shelter nearby. Do you:")
    print("   a) Run for shelter.")
    print("   b) Keep moving through the rain.")
    return input("Your choice: ").strip().lower()

def prompt10():
    print("\n10. You see a glowing portal. Do you:")
    print("   a) Enter the portal.")
    print("   b) Stay in the forest.")
    return input("Your choice: ").strip().lower()

def ending():
    print("\n🌟 Your adventure ends here. Whatever choices you made...")
    print("...you lived to tell the tale (or did you?). Thanks for playing!")

def main():
    intro()
    prompt1()
    prompt2()
    prompt3()
    prompt4()
    prompt5()
    prompt6()
    prompt7()
    prompt8()
    prompt9()
    prompt10()
    ending()

if __name__ == "__main__":
    main()
