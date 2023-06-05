class List:
  ''' Implements an abstract list data structure '''
  def __init__(self):
    self.list = []
    self.pos  = 0
    self.listSize = 0

  def clear(self):
    ''' Clears all the elements from the list '''
    self.list = []
    self.listSize = 0

  def __str__(self):
    ''' Return a string representation of a list '''
    return ','.join(self.list)
  
  def getElement(self):
    ''' Returns the element at the current position '''
    return self.list[self.pos]
  
  def find(self, element):
    ''' Locates the index of an element in the list '''
    index = self.list.index(element)
    if(index >= 0):
      return index
    
    return -1
  
  def insert(self, element, after):
    ''' Inserts new element after existing element '''
    foundAt = self.find(after)
    if(foundAt >= 0):
      self.list.insert(foundAt+1, element)
      return True
    
    return False
  
  def append(self, element):
    ''' Adds new element to the end of the list '''
    self.list.append(element)
    self.listSize += 1

  def remove(self, element):
    ''' Removes element from the list '''
    index = self.find(element)
    if(index >= 0):
      del self.list[index]
      self.listSize -= 1
      return True
    
    return False
  
  def front(self):
    ''' Sets the current position to the first element of the list '''
    self.pos = 0

  def end(self):
    ''' Sets the current position to the last element of the list '''
    self.pos = self.listSize - 1

  def prev(self):
    ''' Moves the current position back one element '''
    if self.pos > 0:
      self.pos -= 1

  def next(self):
    ''' Moves the current position foward one element '''
    if self.pos < self.listSize:
      self.pos += 1

  def currPos(self):
    ''' Returns the current position in the list '''
    return self.pos
  
  def moveTo(self, position):
    ''' Moves the current position to the specified position '''
    self.pos = position

  def hasNext(self):
    ''' Checks if list has an element to print out '''
    return self.pos < self.listSize
  