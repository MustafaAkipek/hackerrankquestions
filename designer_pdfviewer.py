def designerPdfViewer(h, word):
    difference = 0
    
    for i in word:
        difference = max(difference, h[ord(i) - ord('a')]) # ord = ASCII number
    
    return difference*len(word)
    
print(designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5], "torn"))