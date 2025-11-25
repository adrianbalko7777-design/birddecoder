#Samohláska (a, e, i, o, u, y) sa v jazyku vtákov zapíše 3× (a → aaa).
#Spoluhláska má po sebe jednu náhodnú samohlásku naviac (b → ba alebo be).
#Medzery ostávajú rovnaké.

def decode_bird(text: str) -> str:
    vowels = "aeiouy"
    result = ""
    i = 0

    while i < len(text):
        char = text[i]

        # Ak je to samohláska -> v bird language je zapísaná 3x
        if char in vowels:
            result += char
            i += 3  # preskočíme ďalšie dve duplicitné samohlásky

        # Ak je to spoluhláska -> za ňou je 1 samohláska navyše
        elif char.isalpha():
            result += char
            i += 2  # preskočíme tú jednu vtáčiu samohlásku

        # Ak je to medzera alebo čokoľvek iné
        else:
            result += char
            i += 1

    return result


# Testy
print(decode_bird("hieeelalaooo"))        # hello
print(decode_bird("hoooowe yyyooouuu duoooiiine"))  # how you doin
print(decode_bird("aaa bo cy da eee fe"))  # a b c d e f
print(decode_bird("sooooso aaaaaaaaa"))    # sos aaa
