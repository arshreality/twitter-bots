f = open("script.txt", "r")
script = f.read().splitlines()
i = 0

g = open("testing.txt", "w")

while i < len(script) - 1:
    if ":" not in script[i].split(' ')[0]:
        g.write(script[i])
        g.write(script[i+1])
        i += 1
    
    else:
        g.write(script[i])

    g.write("\n")
    i += 1

f.close()
g.close()