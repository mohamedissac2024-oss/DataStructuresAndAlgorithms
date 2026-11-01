def how_much_i_love_you(nb_petals):
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    position = nb_petals % 6
    if position == 0:
        return phrases[5]
    return phrases[position - 1]

print(how_much_i_love_you(3))
