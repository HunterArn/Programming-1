from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for move"""
    move()

  def tl(self):
    """Turn Left"""
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()

  def pick(self):
    """pick_beeper"""
    pick_beeper()

  def put(self):
   """put_beeper"""
    put_beeper()

   def put2(self):
     """put 2 beepers in a line"""
     self.put()
     self.m()
     self.put()
     
   def put5(self):
     """put 5 beepers in a line"""
     self.put2()
     self.m()
     self.put2()
     self.m()
     self.put()
     
   def h(self):
     """Print H using beepers"""
     self.tl()
     self.put5()
     self.tr()
     self.m()
     self.m()
     self.m()
     self.tr()
     self.put5()
     self.ta()
     self.m()
     self.m()
     self.tl()
     self.m()
     self.put2()
     self.tl()
     self.m()
     self.m()
     self.tl()
     self.m2()
     self.m2()
     
    
     
     


   def m2(self):
     """Move 2 Spaces"""
     self.m()
     self.m()
     
    

def main():
    """ Karel code goes here! """
    
    pass


if __name__ == "__main__":
    run_karel_program()