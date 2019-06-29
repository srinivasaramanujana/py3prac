def compress(s):
  """ (str) -> (str)
  
  Given a string in the form 'AAAABBBBCCCCCDDEEEE' , compress it to become 'A4B4C5D2E4'
  
  >>> compress('AAAAABBBBCCCc')
  >>> 'A5B4C3c1'
  """
  counter = {}
  
  for i in s:
    if i not in counter:
        counter[i] = 1
    else:
        counter[i] += 1
        
# print(counter)
  
  result = ''
  
  for j in counter:
      result += j + str(counter[j])
  
  return result
