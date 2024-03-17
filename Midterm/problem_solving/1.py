def search_word(lexicon, word):
 return lexicon.get(word, "Word not found in Lexicon.")
# Sample usage:
lexicon = {
 "abracadabra": "A word uttered to perform a magical act.",
 "enchantment": "The act of casting spells or charms.",
 "mystic": "Relating to mysteries or mystical powers."
}
word = "enchantment"
print(search_word(lexicon, word))