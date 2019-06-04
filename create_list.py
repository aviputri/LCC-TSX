#creating sorted list

#data = """1467153  12309  
#1466231  21300  
#1478821  10230
#"""

l = sorted([list(map(int, line.split())) # convert each pair to integers
            for line                     # iterate over lines in input
            in data.split("\n")          # split on linebreaks
            if line],                    # ignore empty lines
    key=lambda x: x[0])                  # sort by firt element of pair
print(l)