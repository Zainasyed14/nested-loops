word = input("Enter your word : ")
char = input("Enter the character you want to check : ")
i=0
count=0
while(i<len(word)):
    if(word[i]==char):
     count= count+1
    i=i+1
print("The total number of characters = " , count)
