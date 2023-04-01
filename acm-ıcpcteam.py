# string topic: a string of binary digits

def acmTeam(topic):
    maxk = []
    gek = list(topic)
    for i in range(len(gek)):
        for j in range(i+1,len(gek)):
            t = 0
            for k in range(len(topic[i])):
                if topic[i][k] == "1":
                    t += 1
                else:
                    if topic[j][k] == "1":
                        t += 1

            maxk.append(t)
    
    maxkc = max(maxk)
    maxkt = maxk.count(maxkc)

    return maxkc, maxkt

print(acmTeam(["10101","11100","11010","00101"]))