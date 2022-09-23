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


  def fic(self) -> bool:
    """Front is Clear"""
    return Front_is_Clear

  def fib(self) -> bool:
    """Front is Block"""
    self.tr()
    if self.fic():
      self.tl()
      return True
    self.tl()
    return False
  
  def ric(self) -> bool:
    """Right is clear"""
    return ric_is_clear


  
  def rid(self) -> bool:
    """Right is Block"""
    return not self.ric()

  def mazemove(self):
    """Maze Move"""
    if self.fib():
      self.tl()
    else:   # Otherwise...
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
    pass


  def mm(self, num):
    """Move Multiple"""
    for number in range(num):
      self.m()

  def pickm(self, num):
    """Pick Multiple"""
    for i in range(num-1):
      self.pick()
      self.m()
    self.pick()

  def putm(self, num):
    """Put Multiple"""
    for _ in range(0, num-1):
      self.put()
      self.m()
    self.put()

  
def main():
    """ Karel code goes here! """
    kt = ktools()
  
    kt.m()
    kt.tl()
    kt.m()
    kt.put()
    kt.ta()
    kt.m()
    kt.tl()
    kt.m4()
    kt.m()
    kt.tl()
    kt.m()
    kt.put()
    kt.ta()
    kt.m()
    kt.tl()
    kt.m3()
   
    pass


if __name__ == "__main__":
    run_karel_program()