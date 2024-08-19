print("Welcome to the student management system")

name = input("Enter your name: ")
Roll_no = input("Enter your Roll no: ")

def subjects():
    print("Enter your subjects")
    sub1 = "maths"
    sub2 = "english"
    sub3 = "computer science"
    return  sub1, sub2, sub3


def marks():
    sub1, sub2, sub3 = map(int, input("Enter your marks for all three subjects: ").split())
    return sub1, sub2, sub3
    
available_subjects = subjects()
print("Available subjects are: " ,",".join(available_subjects))



sub1, sub2, sub3 = marks()


if sub1 >= 40:
        print("Passed")
        print(f"Maths marks {sub1}")
else:
        print("Fail in Maths")

if sub2 >= 40:
        print("Passed")
        print(f"English marks {sub2}")
else:
        print("Fail in English")

if sub3 >= 40:
        print("Passed")
        print(f"Computer Science marks {sub3}")
else:
        print("Fail in Computer Science")

# total_marks = "result is ".join(available_subjects)
# print(f"Total marks: {sub1, sub2 , sub3}")


