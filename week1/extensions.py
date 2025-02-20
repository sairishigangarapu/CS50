files = {"gif":"image/gif",
         "jpg":"image/jpeg",
         "jpeg":"image/jpeg",
         "png":"image/png",
         "pdf":"application/pdf",
         "txt":"text/plain",
         "zip":"application/zip",
         "bin":"application/octet-stream"}
filename = str(input("file name:"))
filename1 = filename.strip().lower().split(".")
filename2 = filename1[::-1]
if "." not in filename:
    print("application/octet-stream")
else :
    for i in files :
        if i == filename2[0]:
            print(files[i])
