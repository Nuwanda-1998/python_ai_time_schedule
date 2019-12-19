class Teacher_DB:
    #parameters that nedds to be fill during the proccess
    hours = 0
    hours_lessons = 0

    def __init__ (self, db_obj):
        self.teacher_name = input('Please enter the teacher name: ')
        self.lesson_cteach = input('Please enter the lesson that can be tought by this teacher: ').split()
        db_obj.techer_lesson(self.teacher_name, self.lesson_cteach)#need to create in db class


class Main_DB:
    #Total number of classes
    physical_classes = 10
    #this is total lessons time
    less_time = []
    #this is teachers name and the lessons that can teach
    teacher_and_lessons = []



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
        #it gonna store all teachers name as id and the lessons that can be teach in tuples(tuples means list in here)
    def techer_lesson(self, techer_name, lesson_cteach):
        self.teacher_and_lessons.append([self.techer_name, self.lesson_cteach])
    def get_all_teach_less(self):
        return self.teacher_and_lessons

        
    




 class Teacher_Time_Calc:
     def eachlesson_calc(self,db_lessAndTime_obj):
        self.all_list_teachers_and_lessons = db_lessAndTime_obj.get_all_teach_less()

