# int n: the number of chapters
# int k: the maximum number of problems per page
# int arr[n]: the number of problems in each chapter

def workbook(n, k, arr):
    chapter = 1
    page = 1
    special = 0
    question = 0
    loop = 0

    for i in range(n):
        while(arr[i] > 0):
            arr[i] -= 1
            question += 1
            loop += 1
            if question == page:
                special += 1
            elif loop == k:
                page += 1
                loop = 0
        else:
            question = 0
            chapter += 1
            page += 1
            loop = 0

    return special


print(workbook(5, 3, [4,2,6,1,10]))