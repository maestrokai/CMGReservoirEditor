import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def reverseContraction(line):
  '''
  purpose: reverse CMG contracted formate of props
  input: string, CMG contracted form of petrophysical input
  output: list of floats/integer, that reversed the contraction,
  e.g. input = "2*3.15 6.12 1*3.14", output = [3.15, 3.15, 6.12, 3.14]
  '''
  result = []
  array = line.split(" ")
  for ele in array:
    if ele == "":
      continue
    elif "*" not in ele:
        result.append(number(ele))
    else:
        a, b = ele.split("*")
        result += [number(b)]*int(a)
  return result

def readFile(fname):
  # read file line by line, if encounter keyword, add new result
  file = open(fname, 'r')
  carryon = False
  i = 0
  result = []
  while(True):
    line = file.readline()
    if not line or line[0] == "\n":
      break
    result.append(line)

  arr = []
  for line in result:
    arr += reverseContraction(line)
  file.close()
  return arr

def number(string):
  '''
  purpose: convert string to number
  input: string that is a number
  output: number, either integer or a float
  '''
  if "." in string:
      return float(string)
  else:
      return int(string)


def prop_mapper(codingArr, map):
  '''
  purpose:
    map facies coding with properties
  input:
    codingArr: list of facies coding (int) for CMG, arranged in CMG prop order
    map: a facies coding to prop map
  output:
    list of props, same size as codingArr, all values replaced with mapped value
  '''
  res = [0]*len(codingArr)
  err = []
  for i in range(len(codingArr)):
    if codingArr[i] in map:
      res[i] = map[codingArr[i]]
    else:
      res[i] = -1
      err.append(codingArr[i])
  if len(err) > 0:
    print(">> Error when mapping: these codings do not exist.", err)
    return
  return res


def visualizer(arr, nrow=1, ncol=1, ratio=1.0):
  '''
  purpose:
    given a CMG prop array, visualize it on a 2D color map
  input:
    arr - a list of CMG properties
    nrow - number of rows (in vertical direction)
    ncol - number of columns (in horizontal direction)
    ratio - aspect ratio horizontal/vertical
  '''
  if nrow*ncol != len(arr):
    print(">> Error when visualizing: dimensions do not match.", len(arr), nrow, ncol)
    return

  codes = list(set(arr))
  codes.sort()

  print(codes, len(arr))
  colors = ["red", "navy","lime","orange",]
  colormap = {}
  i = 0
  for code in codes:
    colormap[code] = colors[i]
    i += 1

  fig, ax = plt.subplots()
  for x in range(nrow):
    # if x%5 == 0:
    print(x)
    for y in range(ncol):

      code = arr[x*ncol + y]
      rect = Rectangle((-y,x), 1, 1,
                            facecolor=colormap[code])
      ax.add_patch(rect)
  plt.xlim([0,-ncol])
  plt.ylim([0,nrow])
  fig.savefig("reservoir_2D_map.png")

  return


