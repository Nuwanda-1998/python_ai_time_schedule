class Teacher_DB:
    #parameters that nedds to be fill during the proccess
    hours = 0
    hours_lessons = 0

    def __init__ (self):
        self.teacher_name = input('Please enter the teacher name: ')
        self.lesson_cteach = input('Please enter the lesson that can be tought by this teacher: ').split()
    def test_show(self):
         print('the name is {} and the lessons are {}'.format(self.teacher_name, self.lesson_cteach))


class Main_DB:
    #Total number of classes
    physical_classes = 10
    def __init__(self):
        self.lessons_title = input('Enter the lessons name: ').split()
        print(self.lessons_title)
        self.lessons_time = input('Enter the lessons time req: ').split()
        for conv in len(self.lessons_time):
            print(type(conv))
            print(conv)

b1= Main_DB()
print(b1.lessons_time)

# class Teacher_Time_Calc:

#example function
def add(value):
    return value+2

