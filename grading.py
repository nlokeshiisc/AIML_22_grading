import os
os.chdir("Lab2-Grading")
import shutil
from tqdm import tqdm

root = "./extracted"
grades_file = open('grades.csv','w')

grades_file.write("Roll Number, Name, Q1 marks, Q2_1 marks, Q2_2 marks, Q2_3 marks, Q2_4 marks, Q2_5 marks, Total Marks, Q1 comments, Q2_1 comments, Q2_2 comments, Q2_3 comments, Q2_4 comments, Q2_5 comments, \n")

grades_file.close()

target = "./assignment.py"

for submission_name in tqdm(os.listdir(root)):
    path = os.path.join(root, submission_name)
    student_name = submission_name[0:submission_name.index('_')]
    roll_no = None
    for rollno in os.listdir(path):
        # print(rollno[-3:])
        roll_dir = os.path.join(path, rollno)
        if rollno[-3:] == "_L1" and os.path.isdir(roll_dir) and os.path.exists(os.path.join(roll_dir, "assignment.py")):
            roll_no = rollno[:-3]
            original = os.path.join(roll_dir, "assignment.py")
            shutil.copyfile(original, target)
        if rollno[-3:] == "_L2" and os.path.isdir(roll_dir) and os.path.exists(os.path.join(roll_dir, "assignment.py")):
            roll_no = rollno[:-3]
            original = os.path.join(roll_dir, "assignment.py")
            shutil.copyfile(original, target)

    if roll_no == None:
        print(student_name)
        continue
    
    # print("check.py \"" + roll_no + "\" " + "\"" + student_name + "\"")
    os.system("python3 check.py \"" + roll_no + "\" " + "\"" + student_name + "\"")
    os.remove("./assignment.py")
    # break
    # print(roll_no)
    
    # os.system("check.py ")
