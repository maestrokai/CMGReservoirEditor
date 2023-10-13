class reservoir():
  '''
  reservoir dataclass, contains 1D array of coding, nrows, and ncols in CMG input formmating
  '''
  def __init__(self, coding=[], nrow=0, ncol=0):
    self.coding = coding
    self.nrow = nrow
    self.ncol = ncol
    self.prev = [coding, nrow, ncol]
    self.proto = [coding, nrow, ncol]
    self.__dimensionalize()

  def deleteRow(self, start=0, end=0):
    res = []
    for x in range(self.nrow):
      if not start-1 <= x < end:
        res += self.twoD[x]
    self.coding = res
    self.nrow = self.nrow - (end-start+1)
    self.__dimensionalize()
    return

  def deleteCol(self, start=0, end=0):
    res = []
    for x in range(self.nrow):
      res += self.twoD[x][0:start-1] + self.twoD[x][end:]
    print(len(self.twoD[x][0:start-1]),len(self.twoD[x][end:]), self.ncol-end+start-1)
    self.coding = res
    self.ncol = self.ncol - (end-start+1)
    self.__dimensionalize()
    return

  def copyTo(self,copy=[[0,0],[0,0]],to=[[0,0],[0,0]]):
    if not(copy[0][1] -copy[0][0] == to[0][1] -to[0][0] and copy[1][1] -copy[1][0] == to[1][1] -to[1][0]):
      print(">>> Error when copy region from A to B: two regions have different sizes")
      return
    nrow = copy[0][1] -copy[0][0] +1
    ncol = copy[1][1] -copy[1][0] +1

    region = []
    for row in range(copy[0][0]-1, copy[0][1]):
      region.append(self.twoD[row][(copy[1][0]-1):copy[1][1]])
    # print(region)
    i = 0
    for row in range(to[0][0]-1, to[0][1]):
      self.twoD[row] = self.twoD[row][0:to[1][0]-1] + region[i] + self.twoD[row][to[1][1]:]
      # print(len(self.twoD[row]), len(region[i]))
      i += 1
    self.__flatten()
    return

  def repeteRow(self, start=0, end=0, at=0):
    self.__save()
    return

  def repeteCol(self, start=0, end=0, at=0):
    self.__save()
    return

  def addRow(self, start=0, end=0, at=0):
    self.__save()

    return

  def addCol(self, start=0, end=0, at=0):
    self.__save()
    return

  def reset(self):
    # reset to original reservoir
    self = reservoir(self.proto[0], self.proto[1], self.proto[2])
    return

  def undo(self):
    # Undo one step
    self.coding = self.prev[0]
    self.nrow = self.prev[1]
    self.ncol = self.prev[2]
    return

  def __save(self):
    # private object meethod to make a copy of previous step
    self.prev = [self.coding.copy(), self.nrow, self.ncol]
    return

  def __dimensionalize(self):
    res = []
    for i in range(self.nrow):
      res.append(self.coding[i*self.ncol:(i+1)*self.ncol])
    self.twoD = res
    return

  def __flatten(self):
    res = []
    for row in self.twoD:
      res += row
    self.coding = res
    return

