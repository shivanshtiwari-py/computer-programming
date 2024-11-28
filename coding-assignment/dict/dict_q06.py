#  Write a function that counts the occurrences of each word in a given sentence and returns a dictionary where the keys are words and the values are the counts.
def word_count(sentence):
    words = sentence.split()
    return {word: words.count(word) for word in set(words)}

sentence = "this is a test this is only a test"
print(word_count(sentence))
