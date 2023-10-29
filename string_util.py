def reverse_words(s: str) -> str:
    print(s)
    print(len(s))

    if len(s) < 2:
        return s

    out_sentence = ""
    word_start = 0
    word_end = 0

    while word_start < len(s):

        while  word_start < len(s) and s[word_start] == " ":
            word_start = word_start + 1

        if word_start >= len(s):
            break

        print("word_start = ", word_start)
        word_end = word_start
        print("1. word_end = ", word_end)
        while  word_end < len(s) and s[word_end] != " ":
            word_end = word_end + 1

        print("2. word_end = ", word_end)
        word = s[word_start: word_end]
        print("Word = ", word)

        word_start = word_end

        out_sentence = word + " " + out_sentence
        print(out_sentence)
        print("=======================")

    return out_sentence


out_sentence = reverse_words("The quick brown fox jumped over the lazy dog")
print("output  = ", out_sentence)

out_sentence = reverse_words("They always need to have things explained.")
print("output  = ", out_sentence)

out_sentence = reverse_words("        They always need to have things explained.        ")
print("output  = ", out_sentence)
