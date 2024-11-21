#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #: w0414211
#Student Name: niklaus guenther 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    while True:
        #Ask for a sentence
        sentence = input("Enter a sentence or phrase (or type 'quit' to exit): ")
        if sentence.lower() == 'quit':
            print("Goodbye!")
            break

        #Ask for a comma-separated list of letters to remove
        lettersToRemove = input("Enter letters to remove (comma-separated): ").split(',')

        #variables to track changes
        redactedSentence = ""
        removalCount = 0

        #Replace letters with underscores
        for char in sentence:
            if char.lower() in [letter.strip().lower() for letter in lettersToRemove]:
                redactedSentence += "_"
                removalCount += 1
            else:
                redactedSentence += char
        print(f"Redacted Sentence: {redactedSentence}")
        print(f"Number of letters removed: {removalCount}")
    # YOUR CODE ENDS HERE

main()