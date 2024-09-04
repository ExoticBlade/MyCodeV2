def typewriter_effect(sentence, type_delay, delete_delay):
    # Loop through each character and print the sentence
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(type_delay)

    time.sleep(1)