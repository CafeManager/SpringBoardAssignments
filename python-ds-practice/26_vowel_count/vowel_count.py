def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = "aeiou"
    vowelDict = {}
    for letter in phrase:
        if letter.lower() in vowels:
            if letter.lower() in vowelDict.keys():
                vowelDict[letter.lower()] += 1  
            else:
                vowelDict[letter.lower()] = 1
    return vowelDict