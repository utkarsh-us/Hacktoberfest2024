def reverse_words(sentence: str) -> str:
    """Reverses the order of words in the sentence."""
    # Split the sentence into words, reverse the list of words, and join them back into a string
    return ' '.join(sentence.split()[::-1])

def main():
    """Main function to demonstrate the reverse words functionality."""
    user_input = input("Enter a sentence to reverse the words: ")
    reversed_sentence = reverse_words(user_input)
    print(f"Reversed sentence: {reversed_sentence}")

if __name__ == "__main__":
    main()
