#!/usr/bin/env python3

import re

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance (value, str):
      self._value = value
    else:
      print("The value must be a string.")
      self._value = None
      return 0

  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False
    
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
  
  def count_sentences(self):

    # if not self.value: checks if self.value is an empty string. If self.value is indeed an empty string, the condition not self.value becomes True and the code inside the if block is executed. In this case, it returns 0.
    if not self.value:
      return 0

    if isinstance(self.value, str):
    #An example regex to match sentences by the definition: "A sentence is a series of 
    # characters, starting with at lease one whitespace character, that ends in one of ., ! or ?"
      regex = "(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"
      m = re.split(regex, self.value)
      return len(m)
    else:
      print("The value must be a string.")
      self._value = None
      return 0

    

# Quiz_question = MyString(value="Response ?")
# print(Quiz_question)
# print(Quiz_question.is_sentence())
# print(Quiz_question.is_question())
# print(Quiz_question.is_exclamation())
string = MyString()
string.value = 1
string.count_sentences()


