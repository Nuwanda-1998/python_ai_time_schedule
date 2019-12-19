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
    less_time = []
    def __init__(self):
        self.lessons_title = input('Enter the lessons name: ').split()
        print(self.lessons_title)
        self.lessons_time = input('Enter the lessons time req: ').split()
        #convert string to integer
        for conv in range(len(self.lessons_time)):
            self.lessons_time[conv] = int(self.lessons_time[conv])
        #make tuples of lessons and needed time
        for i in range(len(self.lessons_time)):
            self.less_time.append([self.lessons_title[i], self.lessons_time[i]])
        print('this is the tuples : {}'.format(self.less_time))
    




 class Teacher_Time_Calc:
     
