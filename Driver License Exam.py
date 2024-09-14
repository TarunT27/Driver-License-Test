
AnswerKey = ["A","C","A","A","D","B","C","A","C","B","A","D","C","A","D","C","B","B","D","A"]
LowerCase = ["a","c","a","a","d","b","c","a","c","b","a","d","c","a","d","c","b","b","d","a"]
digit =[0,1,2,3,4,5,6,7,8,9]
end = []


file_name = "Driver_exam.txt" 
out_file = open(file_name, "w") 

#program validates input and records answers in 
for i in range(1,20+1):
    if len(end) == 1:
        print("Please restart the program")
        break
    print("Question #",i)
    Answer = input("Enter an uppercase letter for Answer: ")
    for element in digit:
        if Answer == str(element):
            print(element,"Is not a letter")
            print("Enter a Letter not a number, Thank you")
            end.append(element)
            break  
    print("Q"+str(i),"Answer:",Answer)
    out_file.write(Answer+'\n')
    
while i ==20:
    print("Your Answers have been recorded in", file_name)
    break

out_file.close()

print("\n") 
index = 0
Answers = []
Wrong = []

in_file = open(file_name, "r")

for i in range(1,20+1):
    lines = in_file.readline()
    lines = lines.rstrip('\n')
    print("#" + str(i),lines)
    if lines == AnswerKey[index]:
        Answers.append(lines)
        print("correct")
    else:
        print("Incorrect")
        Wrong.append(lines)
        
    index = index + 1
    #print(lines, i)

print("\n")
if len(Answers) >= 15:
    print("CONGRADULATIONS, You passed")
else:
    print("SORRY, you did not passed. Better luck next time :)")
    
print("Total of Right Answers: ", len(Answers))
print(Answers)
print("Total of Wrong Answers: ", len(Wrong))
print(Wrong)
     

in_file.close()

