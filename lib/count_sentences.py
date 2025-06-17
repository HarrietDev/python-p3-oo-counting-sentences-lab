#!/usr/bin/env python3

class MyString:
  def __init__(self,value=""):
    self._value = ""
    self.value=value
  
  @property
  def value(self):
    return self._value
  @value.setter
  def value(self, new_value):
    if not isinstance(new_value,str):
      print("The value must be a string.")
    else:
      self._value = new_value

  def is_sentence(self):
    return self._value.endswith(".")
  def is_question(self):
    return self._value.endswith("?")
  def is_exclamation(self):
    return self._value.endswith("!")
  def count_sentences(self):
    temp =self._value.replace("!",".").replace("?",".")
    parts = temp.split(".")

    sentence =[s.strip() for s in parts if s.split()]
    
    return len(sentence)

string = MyString()
string.value = "This is, a string! It has three. sentences. Right?"
print(string.is_sentence())
print(string.is_question())
print(string.is_exclamation())
print(string.count_sentences())