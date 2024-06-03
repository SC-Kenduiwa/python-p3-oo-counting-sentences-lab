#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("Input value must be a string")
        self.value = value
    
        def is_sentence(self):
         return self.value.endswith('.')
    
        def is_question(self):
         return self.value.endswith('?')
    
        def is_exclamation(self):
          return self.value.endswith('!')
    
        def count_sentences(self):
        # Replace all non-sentence-ending punctuation with a period
         punctuation = ['.', '!', '?']
         for p in punctuation:
            self.value = self.value.replace(p, '.')
        # Split the string into sentences
        sentences = self.value.split('.')
        # Remove empty strings from the list
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)

# Test the class
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())  # Output: 3
