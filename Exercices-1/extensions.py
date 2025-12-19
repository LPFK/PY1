extention = input("Enter a file name : ")
extention = extention.lower()
extention = extention.strip()
if extention.endswith(".gif"):
    print("image/gif")
elif extention.endswith(".jpg"):
    print("image/jpeg")
elif extention.endswith(".jpeg"):
    print("image/jpeg")
elif extention.endswith(".png"):
    print("image/png")
elif extention.endswith(".pdf"):
    print("application/pdf")
elif extention.endswith(".txt"):
    print("text/plain")
elif extention.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")