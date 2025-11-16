# Python 3.x
import sys

def analyze_text(text):
    vowels = consonants = digits = spaces = specials = words = sentences = 0
    in_word = False

    for ch in text:
        if ch.isalpha():
            lower = ch.lower()
            if lower in 'aeiou':
                vowels += 1
            else:
                consonants += 1
            if not in_word:
                words += 1
                in_word = True
        else:
            if ch.isdigit():
                digits += 1
            elif ch.isspace():
                spaces += 1
                in_word = False
            else:
                specials += 1
                if ch in '.!?':
                    sentences += 1
                in_word = False

    return {
        "Words": words,
        "Vowels": vowels,
        "Consonants": consonants,
        "Digits": digits,
        "Spaces": spaces,
        "Specials": specials,
        "Sentences": sentences
    }

if __name__ == "__main__":
    print("Paste your text and press Ctrl+D (Linux/Mac) or Ctrl+Z Enter (Windows).")
    text = sys.stdin.read()
    result = analyze_text(text)
    
    print("\n--- Result ---")
    for key, value in result.items():
        print(f"{key}: {value}")
