#!/usr/bin/python
def test():
   try:
      fh = open("testfile", "w")
      try:
         #raise IOError
         raise Exception
      finally:
         print("Going to close the file")
         fh.close()

   except IOError:
      print("Error: can\'t find file or read data")
      pass

   #not goto exception below
   except Exception as e:
      print('inexcept')
      print(e)
      raise Exception #instead exit()

   return 1

print(test())