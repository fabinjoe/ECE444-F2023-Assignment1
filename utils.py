class Utils:
  def reversed(number: int) -> int:
    if type(number) != int:
      raise TypeError("Wanted an integer.")
      
    str_number = str(number)
    return int(str_number[::-1])
    
  def formatter(number: int, base: int) -> int:
    if type(number) != int:
      raise TypeError("Wanted an integer.")
    if base not in (2, 8):
      raise TypeError("base = 2 or 8")
    if base == 2:
      return bin(number)
    elif base == 8:
      return oct(number)
