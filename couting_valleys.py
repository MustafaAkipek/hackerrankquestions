# steps: yürüyüşteki adım sayısı
# path: yolu tanımlayan bir dize

def countingValleys(steps, path):

    level = 0  # deniz yüksekliğine göre seviyemiz
    valleys = 0  #deniz seviyesine gelme sayımız
    
    for step in path:
    
        if step == 'U':
            level+=1
            
            if level == 0:
                valleys+=1
                
        else:
            level-=1
    
            
    print (valleys)

countingValleys(8, "UDDDUDUU")

#adım sayımız var ve adımlar bitene kadar yürümemiz lazım eğer up "u" gelirse karşımıza "/" kullanmamız lazım, ama down "d" gelirse "\" kullanmamız
#lazım aşağı indiğimizi göstermek için. Başlangıç ve bitişte "-" kullanmamız lazım.