#2 kedi ve faremiz var. Eğer ilk kedi yakın ise a ikinci kedi fareye daha yakın ise b eğer eşit uzaklıkta ise c yi yazdıracak.

def catAndMosue(x,y,z):
    if abs(x-z) < abs(y-z):
        print("Cat A")
        
    elif abs(y-z) < abs(x-z):
        print("Cat B")
        
    else:
        print("Mouse C")
        
catAndMosue(1,3,2)