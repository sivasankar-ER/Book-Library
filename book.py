ids = [101, 102, 103, 104, 105]
Books = ["python", "java", "c++", "javascript"]
target = 103
for i in range(len(ids)):
    if ids[i] == target:
        print("book is found:", Books[i])
