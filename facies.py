class Facies():
  i = 0
  facies = []


  def __init__(self, por=0, permI=0, so=1, sw=0, relnum=0, label=""):
    self.label=label
    self.code = Facies.i
    self.por = por
    self.permI = permI
    self.relnum = relnum
    self.so = so
    self.sw = sw
    Facies.facies.append(self)
    Facies.i += 1


  @classmethod
  def __repr__(cls):
    return cls.facies



