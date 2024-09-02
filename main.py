import random
try: import pyperclip
except ModuleNotFoundError: pass

def generate_natural_string(length):
    cat_sounds = ["mrrp", "meow", "meow", "nya", "mreow", "meoww", "mrew"]
    emojis = ["^_^", ":3", ";3", ":3c", ">.< ", ">~<", "O~o", "UwU", "=^.^=", "^-^", "OwO", ">w<", "^w^", "nya~", "=^_^=", "^o^", ">.<", ">///<", "^-.-^", "=^ω^=", "=OwO=", "(=^･ω･^=)"]
    
    # Basic patterns to simulate natural sound sequences
    patterns = [
        ["mrrp", "nya", "meow"],
        ["meow", "mreow", "mrrp"],
        ["nya", "mrrp", "mreow"],
        ["meow", "nya", "mrrp"]
    ]
    
    # Create a string with occasional random sounds
    result = []
    for i in range(length):
        if random.random() < 0.2:  # 20% chance to pick a random sound
            result.append(random.choice(cat_sounds))
            if random.random() < 0.15:  # Extra 15% chance to pick an emoji
                result.append(random.choice(emojis))
        else:
            pattern = random.choice(patterns)
            result.append(pattern[i % len(pattern)])
    
    # Join the result list into a single string with spaces and append ":3"
    return ' '.join(result) + ' :3'

def main():
    try:
        length = int(input("Enter the number of cat sounds: "))
        if length < 1:
            print("Please enter a positive integer.")
            return
        
        result = generate_natural_string(length)
        
        print("Generated cat sound string:")
        print(result)
        
        # Copy the result to the clipboard
        try:
            pyperclip.copy(result)
            print("\nThe string has been copied to the clipboard.")
        except NameError:
            print("\nUnable to copy to clipboard. 'pyperclip' module not found.")
        except pyperclip.PyperclipException:
            print("\nUnable to copy to clipboard. Clipboard access denied.")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
