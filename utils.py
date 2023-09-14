class Utils:
  def reversed(number: int) -> int:
    str_number = str(number)
    return int(str_number[::-1])
    
  def formatter(number: int, base: int) -> int:
    if base not in (2, 8):
      return "Not compatible base formattor."
    if base == 2:
      return bin(number)
    elif base == 8:
      return oct(number)
