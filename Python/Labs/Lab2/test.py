"""
Shared by one of the student

def doubleChar(word):
 for i in range(len(word)):
  print(i)
  print(chr(i))
doubleChar('The')




def end_other(str1, str2):
    string1 = str1.lower()
    string2 = str2.lower()
    if(len(string1) < len(string2)):
        string1[:len(string1)]== string2[len(string2)-len(string1):]
        return True
print(end_other('AbC', 'HiaBc'))



i = 0
while i < 6:
  i += 1
  if i == 3:
     break
  print(i)

"""

class Book():
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s, authoer:%s, pages:%s " %(self.title, self.author, self.pages)
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book is destroyed")
    
book = Book("Python", "Joh Andersson", 180)
print(book)