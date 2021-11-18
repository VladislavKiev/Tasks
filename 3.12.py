"""
Write a function that accepts text as input and returns a dictionary in which the keys will be the words from the string. and the values will be the number of occurrences of the word in the string
         Call example
             count_words ("some text some") => {"some": 2, "text": 1}
"""
import re


def text_blender(text):
    regex = re.compile('[^a-zA-Z ]')
    supfluorus = regex.sub('', text)
    words = supfluorus.split()
    word_dict = {i: words.count(i) for i in words}
    return word_dict


res = text_blender(" some text some some text some!!! some text som?")
print(res)
