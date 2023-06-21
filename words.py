def print_upper_words(words):
    """Prints a new word on separate line, uppercased.

        >>> print_upper_words(["hi", "hello", "world"])
        HI
        HELLO
        WORLD
        
    """

    for word in words:
        print(word.upper())


def print_upper_words_II(words):
    """Prints a new word on separate line, uppercased, only if it starts with E or e.

        >>> print_upper_words_II(["Earth", "egg", "Apple"])
        EARTH
        EGG
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words_III(words, must_start_with):
    """Print a new word on separate line, uppercased only if it starts with one of given letters.

        >>> print_upper_words_III(["egg", "Earth", "Apple", "tree"],
        ...                   must_start_with=["T", "E"])
        EGG
        EARTH
        TREE
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
