x = input("What is your name? ")

o = open("output.txt", "w+")

for i in x:
  o.write(i + "\n")
o.write("\n")

for i in range(0, len(x), 2):
  o.write(x[i] + "\n")
o.write("\n")

for i in range(len(x) - 1, -1, -1):
  o.write(x[i] + "\n")
o.write("\n")

o.close()

"""
# Bonus: each of the above methods in a separate file

with open("output1.txt", "w+") as f:
  for i in x:
    f.write(i + "\n")

with open("output2.txt", "w+") as f:
  for i in range(0, len(x), 2):
    f.write(x[i] + "\n")

with open("output3.txt", "w+") as f:
  for i in range(len(x) - 1, -1, -1):
    f.write(x[i] + "\n")
"""