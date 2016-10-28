def number_of_lines(contents):
  count = contents.splitlines()
  return len(count)

def wordOccurance(contents):
  return contents.count("impossible")

def replaceString(contents):
  contents = contents.replace("father","temp")
  contents = contents.replace("mother","father")
  contents = contents.replace("temp","mother")
  print contents

def main():
  file = open('flash.txt', 'r')
  contents = file.read()

  print "\nNumber of lines: %d" % number_of_lines(contents)

  print "Impossible count: % d" % wordOccurance(contents)
  replaceString(contents)
  file.close()

if __name__ == '__main__':
    main()
