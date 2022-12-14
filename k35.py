from stanfordkarel import*


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
     self.m()
     self.m()
     self.m()
     self.m()
     
  def e(self):
    self.m()
    self.put()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.put()
    self.m()
    self.put()
    self.m()
    self.put()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.m()
    self.put()
    self.tr()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.m()


  def l(self):
    self.put()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.put2()
    self.tl()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.m()


  def o(self):
    self.put2()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()
    
 
def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.h()
    kt.e()
    kt.l()
    kt.l()
    kt.o()
    pass


if __name__ == "__main__":
    run_karel_program()