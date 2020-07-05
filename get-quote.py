import random

def primary():
  #print("Keep it logically awesome.")

   f = open("quotes.txt")
   quotes = f.readlines()
   f.close()
   lst = len(quotes)-1
   rnd = random.randint(0,lst)

   print(quotes[rnd])

if __name__== "__main__":
  primary()
