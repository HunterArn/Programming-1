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

  def m2(self):
     self.m()
     self.m()


  def m3(self):
     self.m2()
     self.m()

  def m4(self):
     self.m2()
     self.m2()
  
  def pick2(self):
     self.pick()
     self.m()
     self.pick()

  def pick3(self):
     self.pick()
     self.m()
     self.pick()
     self.m()
     self.pick()
  
  
  def pick4(self):
     self.pick()
     self.m()
     self.pick()
     self.m()
     self.pick()
     self.m()
     self.pick()

  
  

  
def main():
    """ Karel code goes here! """
    kt = ktools()

    kt.tl()
    kt.m2()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m2()
    kt.tl()
    kt.tl()
    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.tl()
    kt.m()
    kt.tl()
    kt.m3()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m3()
    kt.tl()
    kt.m()
    kt.tl()
    kt.m2()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m2()
    kt.tl()
    kt.m()
    kt.tl()
    kt.m2()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m2()
    kt.tl()

  
    pass


if __name__ == "__main__":
    run_karel_program()