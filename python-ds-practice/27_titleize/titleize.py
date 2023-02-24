def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    newPhrase = ""
    firstLetter = True
    for word in phrase.split(" "):
        for letter in word:
            if firstLetter:
                newPhrase += letter.upper()
                firstLetter = False
            else:
                newPhrase += letter.lower()
        firstLetter = True
        newPhrase += " "
    return newPhrase[0:len(newPhrase)-1]

