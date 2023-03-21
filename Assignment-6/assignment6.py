import re

regex = re.compile(r"""
^\s*
(      # Floating point    
  (?:\+|\-)?     # Optional sign
  (?:[1-9]\d*|0) # String of digits or '0'
  (?:\.\d+)      # decimal point then a string of digits
)
\s+
((?:\+|\-)?[1-9]\d*|0)  # Integer: possibly signed string
                        #   of digits or '0'
\s+
([xyzXYZ]{3}) # String: 3 of 'x', 'y', 'z', 'X', 'Y', 'Z'
\s*$
""", re.X)

#initialize variables
float_sum = 0
int_sum = 0
let_count = {'x': 0, 'y': 0, 'z': 0}


with open('data.txt', 'r') as data:
    for line in data:
        #
        match = regex.search(line)
        
        if match:
            
            float_val = float(match.group(1))
            int_val = int(match.group(2))
            letts = match.group(3).lower()
            float_sum += float_val
            int_sum += int_val
            
            #letts is assumed to be a list of length 3 so thats why we are iterating over range(3)
            #letts[i] retrives the corresponding key (either x,y or z)
            for i in range(3):
                let_count[letts[i]] += 1
        else:
            print("No match with", line)


print(f"Float sum: {float_sum:.3f}, Integer sum: {int_sum}")
print(f"{let_count['x']} xs, {let_count['y']} ys, {let_count['z']} zs")

