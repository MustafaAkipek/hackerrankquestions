# int n: the number of chapters
# int k: the maximum number of problems per page
# int arr[n]: the number of problems in each chapter

def workbook(n, k, arr):
    special = 0
    page = 1

    for quesitons in arr:
        for index in range(1, quesitons+1):
            if index == page:
                special += 1

            if index == quesitons or index % k == 0:
                page += 1

    return special

print(workbook(5, 3, [4,2,6,1,10]))