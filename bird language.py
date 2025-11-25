def translation(text: str) -> str:
    vowels = "aeiouy"
    result = ""
    i = 0

    while i < len(text):
        x = text[i]
        result += x

        if x in vowels:
            i += 3      # samohláska → preskočíme dve rovnaké
        elif x == " ":
            i += 1      # medzera → normálne pokračujeme
        else:
            i += 2      # spoluhláska → preskočíme 1 náhodnú samohlásku

    return result


print("Example:")
print(translation("hieeelalaooo"))
print(translation("hoooowe yyyooouuu duoooiiine"))
print(translation("aaa bo cy da eee fe"))
print(translation("sooooso aaaaaaaaa"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"
