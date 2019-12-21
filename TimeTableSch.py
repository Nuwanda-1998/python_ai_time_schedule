from collections import Counter
import math
# lissti = [0,0,0,4,4,'11','11',11,'b']
# checker = dict(Counter(lissti))
# print(type(checker))
# print(checker)

class Teacher_DB:
    #parameters that nedds to be fill during the proccess
    hours = 0
    hours_lessons = 0

    def __init__ (self, db_obj):
        self.teacher_name = input('Please enter the teacher name: ')
        self.lesson_cteach = input('Please enter the lesson that can be tought by this teacher: ').split()
        #this function store the new teacher data to the main database
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
        self.teacher_and_lessons.append([techer_name, lesson_cteach])
    def get_all_teach_less(self):
        return self.teacher_and_lessons
    def get_all_total_time(self):
        return self.less_time
    def set_each_lesson_time(self, th_dict):
        self.each_lesson_time = th_dict
    def set_each_lesson_time_predict(self, th_pr_list):
        self.each_lesson_time_predict = th_pr_list
    def set_all_predicted_time(self, th_pr_list):
        self.total_predicted_time_list = th_pr_list
    def get_each_lesson_time_predict(self):
       return self.each_lesson_time_predict
    def set_time_needed(self, tt):
        self.time_needed = tt
    def set_total_integer_time_needed(self, t_i_t):
        self.total_time = t_i_t
    def get_total_integer_time_needed(self):
        return self.total_time
    def show_test(self):
        print('total time needed is {} and each lesson time requierment is {}'.format(self.time_needed, self.each_lesson_time_predict))
    def get_teachers_and_lessons(self):
        return self.teacher_and_lessons
    #this function will store the main matrix for each day in week
    def days_matrix_setter(self, weeks_m):
        self.weeks_day_matrix = weeks_m
    def get_total_lesson_and_time_req(self):
        return self.less_time
        
    




class Teacher_Time_Calc:
    #store the number of each lessons that how many teacher can handle them
    no_teachers_cteach = {}
    def __init__ (self, db_lessAndTime_obj):
    #def eachlesson_calc(self, db_lessAndTime_obj):
        self.all_list_teachers_and_lessons = db_lessAndTime_obj.get_all_teach_less()
        self.total_lessons_time = db_lessAndTime_obj.get_all_total_time()
        self.main_database_object = db_lessAndTime_obj
        print('all list teacher is {} and the total lesson time is : {}  '.format(self.all_list_teachers_and_lessons, self.total_lessons_time))
    
    def each_lesson_calc(self):
        #this will save the each lesson time requierd for each teacher
        each_lesson_time_needed = []
        just_time = []
        #this value will storeall teachers lessons
        lessons_a = []
        #this loop will count the number of teachers that can teach each lesson
        for i in range(len(self.all_list_teachers_and_lessons)):
            lessons_a.extend(self.all_list_teachers_and_lessons[i][1])
        #this value will store the dict of the number of teachers that can teach each lesson
        number_teachers_cteach = dict(Counter(lessons_a))
        self.main_database_object.set_each_lesson_time(number_teachers_cteach)
        #this loop will predict the what time each lesson takes from the teacher that are trying to teach it
        for c in range(len(self.total_lessons_time)):
            search_key = self.total_lessons_time[c][0]
            search_value = self.total_lessons_time[c][1]
            if search_key in number_teachers_cteach.keys():
                devider_um = math.ceil(search_value / number_teachers_cteach[search_key])
                each_lesson_time_needed.append([search_key, devider_um])
                just_time.append(devider_um)        
        self.main_database_object.set_each_lesson_time_predict(each_lesson_time_needed)
        self.main_database_object.set_all_predicted_time(just_time)
        print('this is each lesson time needed{}'.format(each_lesson_time_needed))
                
    def total_time_needed_calculator(self):
        totalliti = 0
        for counter in self.main_database_object.get_all_total_time():
            totalliti = totalliti + counter[1]
        self.main_database_object.set_total_integer_time_needed(totalliti)
        

class Which_day_to_assign:
    #this variable will store the matrix of each tday

    def __init__ (self,db_obj):
        self.matrix = [[[0,'none', 'teacher1', 'teacher2'] for i in range(5)]for j in range(10)]
        self.mon = self.matrix.copy()
        self.tue = self.matrix.copy()
        self.wed = self.matrix.copy()
        self.thur = self.matrix.copy()
        self.fri = self.matrix.copy()
        self.main_database_object = db_obj
    #this func will create matrix for each day
    def days_setter(self):
        week_work_days_matrix = []
        week_work_days_matrix.append(self.mon)
        week_work_days_matrix.append(self.tue)
        week_work_days_matrix.append(self.wed)
        week_work_days_matrix.append(self.thur)
        week_work_days_matrix.append(self.fri)
        self.main_database_object.days_matrix_setter(week_work_days_matrix)
    def backtraking_and_forwardchecking(self):
        #this is the maximum time req for each lesson
        list_of_lessons_and_max_time = self.main_database_object.get_each_lesson_time_predict()
        #this the list of teachers and lessons than can be tought
        list_of_teachers_and_lessons = self.main_database_object.get_all_teach_less()
        #this is the total hours of lessons that needed
        list_of_lessons_and_req_time = self.main_database_object.get_total_lesson_and_time_req()
        #it will be save the total hours needed
        max_total_time_needed = self.main_database_object.get_total_integer_time_needed()
        print('the list of lessons and max time is {} and the list of teachers and lessons is : {} and the list of llessons time requierd is {} and finally the max total time needed is : {}'.format(list_of_lessons_and_max_time, list_of_teachers_and_lessons, list_of_lessons_and_req_time, max_total_time_needed))



    
        





b0 = Main_DB()
b1 = Teacher_DB(b0)
b2 = Teacher_DB(b0)
b2 = Teacher_Time_Calc(b0)
b2.each_lesson_calc()
b2.total_time_needed_calculator()
b3 = Which_day_to_assign(b0)
b3.backtraking_and_forwardchecking()



#matrix = [[['teacher1', 'teacher2'] for i in range(5)]for j in range(10)]
# matrix = [[[0,'none', 'teacher1', 'teacher2'] for i in range(5)]for j in range(10)]
# for i in range(len(matrix)):
#     for j in range(5):
#         print(matrix[i][j], end='')
#     print('')

    
