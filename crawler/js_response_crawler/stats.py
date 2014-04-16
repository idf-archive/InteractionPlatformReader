import os
import subprocess
def stats():
  """
  stats of json files
  """
  stock_dict = {}
  r_dict = {}
  total = 0
  for root, dirs, files in os.walk("./json_raw/"):
    for name in files:
      if name.endswith((".json")):
        stock_code, rid, page = name.split("-")
        total += 1
        try:
          stock_dict[stock_code] += 1
          r_dict[rid] += 1
        except KeyError: 
          stock_dict[stock_code] = 1
          r_dict[rid] = 1
        
  print len(stock_dict)
  print len(r_dict)
  print total

if __name__=="__main__":
  stats()