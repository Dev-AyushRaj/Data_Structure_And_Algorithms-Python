# #Program to create Stack using list

# Stack_fruits =[]
# #push element
# Stack_fruits.append("Apple")
# Stack_fruits.append("Banana")
# Stack_fruits.append("Mango")
# Stack_fruits.append("Orange")
# print(Stack_fruits)

# #Poping elements
# ele = Stack_fruits.pop()
# print("POP:",ele)

# #Peek element
# Top = Stack_fruits[-1]
# print("Top ele:",Top)

# # Is empty stack
# is_empty = not bool(Stack_fruits)
# print("Is stack empty:",is_empty)

# # Use class to create a stack
# class stack:
#     def __init__(self):
#         self.stack_fruit = []

#     def add_fruits(self,data):
#         self.stack_fruit.append(data)

#     def pop_friuts(self):
#         if self.Is_empty():
#          print("Stack is empty")
#          return
#         fruit = self.stack_fruit.pop()
#         print(fruit)

#     def peek_fruits(self):
#         if self.Is_empty():
#          print("Stack is empty")
#          return
#         peek = self.stack_fruit[-1]
#         print(peek)

#     def Is_empty(self):
#         return len(self.stack_fruit) == 0


# fruit = stack()
# fruit.add_fruits("Apple")
# fruit.add_fruits("Orange")
# fruit.add_fruits("Mango")
# fruit.add_fruits("Banana")
# print("fruits in stack:",fruit.stack_fruit)
# fruit.peek_fruits()
# fruit.pop_friuts()
# fruit.peek_fruits()

# # question: if input is rahul than output should be reverse
# class Reverse:
#    def __init__(self):
#       self.stack = []

#    def push(self,data):
#       self.stack.append(data)
   
#    def pull(self):
#       if not self.is_empty():
#          return self.stack.pop()
      
   
#    def is_empty(self):
#       return len(self.stack) == 0


# input_string = input(str("Enter a String:"))
# str = Reverse()
# for chr in input_string:
#    str.push(chr) 

# return_string = ""
# while not str.is_empty():
#    return_string += str.pull()

# print("Reverse word:",return_string)


# #Revesring word in a sentance by using stack
# class Stack:
#    def __init__(self):
#       self.stack = []

#    def push(self,data):
#       self.stack.append(data)

#    def pull(self):
#       if not self.Is_empty():
#          return self.stack.pop()

#    def Is_empty(self):
#       return len(self.stack)==0
   
# input_string = input(str("Enter a sentence:"))
# words = input_string.split()
# item = Stack()

# for word in words:
#    item.push(word)

# reverse_sentance = ""
# while not item.Is_empty():
#    reverse_sentance += item.pull() + " "

# print("Reversed sentence:",reverse_sentance)

# Reversing th e latter in the string
class Reverse:
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)

    def pull(self):
        if not self.Is_empty():
            return self.items.pop()

    def Is_empty(self):
        return len(self.items)==0
    
string = input(str("Enter the string:"))
words = string.split()
final_list = []
for word in words:
    line = Reverse()
    for chr in word:
        line.push(chr)
    reverse_word = ""
    while not line.Is_empty():
         reverse_word += line.pull()
    final_list.append(reverse_word)

reversed_line = " ".join(final_list[::-1])
print(reversed_line)