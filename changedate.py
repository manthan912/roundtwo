li = []
# selecting the sample input file
with open("C:\\Users\\MANTHAN\\PycharmProjects\\untitled\\Q2_SampleInput.txt", "r") as reader:
    for line in reader.readlines():
        li.append(line)

updateYesterday = []
removeToday = []
updatetoday = []
newfile = []
# replace yesterday with 0n 01-06-2021
for wrds in li:
    replacedWords = wrds.replace("Yesterday", "On 01-06-2021")
    updateYesterday.append(replacedWords)

# replace Today with 0n 02-06-2021
for wrds in updateYesterday:
    replacedWords = wrds.replace("Today", "On 02-06-2021")
    removeToday.append(replacedWords)

# replace today with 0n 02-06-2021
for wrds in removeToday:
    replacedWords = wrds.replace("today", "On 02-06-2021")
    updatetoday.append(replacedWords)

# replace Tomorrow with 0n 03-06-2021
for wrds in updatetoday:
    replacedWords = wrds.replace("Tomorrow", "On 03-06-2021")
    newfile.append(replacedWords)
#a new blank .txt file was created in the same location as the .py file and updated content is being stored in it
with open("C:\\Users\\MANTHAN\\PycharmProjects\\untitled\\Q2opANS.txt", "w") as finalans:
    for i in newfile:
        finalans.write(i)