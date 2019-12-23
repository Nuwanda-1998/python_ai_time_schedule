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
    #this variable will hold the assigned teachers and lessons on the matrix
    assigned_teachers_and_lessons = []
    #the lessons that still need to execute
    remaining_lessons = []
    avoid_list = []
    all_lessons_title = []
    teachers_r_r_list = []
    #all the teachers name from the begining
    all_teachers_name = []


    def __init__(self):
        self.lessons_title = input('Enter the lessons name: ').split()
        print(self.lessons_title)
        self.remaining_lessons.append(self.lessons_title)
        self.all_lessons_title.append(self.lessons_title)
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
        #create a list of teachers name from begining
        self.all_teachers_name.append(techer_name)
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
    def days_matrix_getter(self):
        return self.weeks_day_matrix
    def get_total_lesson_and_time_req(self):
        return self.less_time
    def set_list_of_teachers(self, teachers_listc):
        self.teachers_list = teachers_listc
    def get_list_of_teachers(self):
        return self.teachers_list
    def get_lessons_list(self):
        return self.lessons_title
        #nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnneeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddd to create
    def set_list_of_remaining_teachers(self, teachers_r_list):
        self.teachers_r_r_list = teachers_r_list
    def get_list_of_remaining_teachers(self):
        return self.teachers_r_r_list
    def set_assigned_teacher_lesson(self, list_t_l):
        self.assigned_teachers_and_lessons.append([list_t_l])
    def get_assigned_teacher_lesson(self):
        return self.assigned_teachers_and_lessons
    def set_remainig_lessons(self):
        #self.remaining_lessons.append([x for x in (self.all_lessons_title) if x not in (self.avoid_list)])
        for x in range(len(self.teacher_and_lessons)):
            this_teacher_less = self.teacher_and_lessons[x][1].copy()
            self.teacher_and_lessons[x][1] = [k for k in (this_teacher_less) if k not in (self.avoid_list)]
        print('this is remaining list in db {}'.format(self.remaining_lessons))
    def get_remainig_lessons(self):
        return self.remaining_lessons
    def set_finished_lessons(self, lesson):#not sure about
        self.avoid_list.append(lesson)
        print('this is avoid list in main db {} '.format(self.avoid_list))
    def get_finished_lessons(self):
        return self.avoid_list
    #return the title of the lessons
    def get_all_lesson_title(self):
        return self.all_lessons_title
    #return the list of teachers that filled from the begining
    def get_all_teachers_name_init (self):
        return self.all_teachers_name
        
    




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
        need_list = self.main_database_object.get_all_total_time()
        for counter in need_list:
            totalliti = totalliti + counter[1]
        self.main_database_object.set_total_integer_time_needed(totalliti)
    def list_of_teachers(self):
        final_list = []
        the_list_1 = self.main_database_object.get_teachers_and_lessons()
        for counter in range(len(the_list_1)):
            final_list.append(the_list_1[counter][0])
        self.main_database_object.set_list_of_teachers(final_list)
    def remaining_teacher_calc(self):           ###     neeeeedddddddddddd toooooo     rrrruuuuuuuuu    nnnnnnnnnn
        the_teacher_list = []
        #this is total list of lessons and their needed time
        total_lesson_and_time = self.main_database_object.get_all_total_time()
        teacher_and_lessons = self.main_database_object.get_teachers_and_lessons()
        left_to_set = self.main_database_object.get_remainig_lessons()##################################################################
        lesson_list = left_to_set.copy()
        for counter in range(len(teacher_and_lessons)):
            if len(lesson_list) > 0:
                lesson = lesson_list.pop()
                if lesson in teacher_and_lessons[counter][1]:
                    the_teacher_list.append(teacher_and_lessons[counter][1])
            else:
                self.main_database_object.set_list_of_remaining_teachers(['none'])
                #self.main_database_object.set_list_of_remaining_teachers(the_teacher_list)
                return the_teacher_list 
        self.main_database_object.set_list_of_remaining_teachers(the_teacher_list)
        return the_teacher_list
    def remaining_class_calculator(self, lesson_title):
        #getting the lessons and their time     IM PREDICTING NOT SURE
        lessons_and_times = self.main_database_object.get_all_total_time()
        for counter in range(len(lessons_and_times)):
            if lesson_title == lessons_and_times[counter][0]:
                num = lessons_and_times[counter][1]
                print('in remaining class calculator before num-1 lesson {} wih time {}'.format(lessons_and_times[counter][0], lessons_and_times[counter][1]))# tttttttttttttttttttttttttteeeeeeeeeeeeeststttttttttttt
                num = num-1
                lessons_and_times[counter][1] = (num)
                print('in remaining class calculator after num-1 lesson {} wih time {}'.format(lesson_title, num))# tttttttttttttttttttttttttteeeeeeeeeeeeeststttttttttttt
                if (num) < 1:# it was num -1
                    self.main_database_object.set_finished_lessons(lesson_title)
                    print('{} added to avoid list'.format(lesson_title))
                    print('in remaining class calculator after and in if statement num-1 lesson {} wih time {}'.format(lesson_title, num))# tttttttttttttttttttttttttteeeeeeeeeeeeeststttttttttttt
    def check_for_end(self):
        all_list = self.main_database_object.get_all_lesson_title()
        avoid_list_c = self.main_database_object.get_finished_lessons()
        if len(all_list) == len(avoid_list_c):
            print('this is all list {} and this is avoid list {}'.format(all_list, avoid_list_c))
            return False
        else:
            return True
    def lesson_generator(self, teacher):
        avoid_list_t = self.main_database_object.get_finished_lessons()
        print('this is avid lessons in line 199 {}'.format(avoid_list_t))
        lessons_can_teach = []
        remaining_lessons_list = []
        final_lesson = ''
        #the list of teachers and that can make class with
        x = self.main_database_object.get_all_teach_less()
        #x = self.main_database_object.get_all_total_time()
        techers_and_lessons = x.copy()
        for counter in range(len(techers_and_lessons)):
            if techers_and_lessons[counter][0] == teacher:
                #lessons_can_teach = techers_and_lessons[counter][1]
                lessons_can_teach.append(techers_and_lessons[counter][1])#new change
                break
        remaining_lessons_list = [x for x in (lessons_can_teach) if x not in (avoid_list_t)]
        if len(remaining_lessons_list) > 0:
            #final_lesson = lessons_can_teach.pop(0)#big problem       ppppppppppppppppppppppppppppp
            print('this is remaining lesson in line 222 {}'.format(remaining_lessons_list))
            #final_lesson = remaining_lessons_list[0][0]#big problem       ppppppppppppppppppppppppppppp
            y = remaining_lessons_list.pop()
            if len(y)>0:
                final_lesson = y[0]
                return final_lesson
            else:
                return 'None'
        else:
            return 'None'
    def days_of_week_matrix_drawer(self):
        weeks_day = self.main_database_object.days_matrix_getter()
        for counter in range(len(weeks_day)):
            day = weeks_day[counter]
            for i in range(len(day)):
                for j in range(5):
                    print(day[i][j], end='')
                print('')
            print('')


    

        

        

class Which_day_to_assign:
    #this variable will store the matrix of each tday
    #matrix = [[['none'] for i in range(5)]for j in range(10)]
    def __init__ (self, db_obj, calc_obj):
        #self.matrix = [[[0,'none', 'teacher1', 'teacher2'] for i in range(5)]for j in range(10)]
        #self.matrix = [[['none'] for i in range(5)]for j in range(10)]#nnnnneeeewwwwww change
        # self.mon = self.matrix.copy()
        # self.tue = self.matrix.copy()
        # self.wed = self.matrix.copy()
        # self.thur = self.matrix.copy()
        # self.fri = self.matrix.copy()
        self.main_database_object = db_obj
        self.calculator_object = calc_obj
    #this func will create matrix for each day
    def days_setter(self):
        week_work_days_matrix = []
        week_work_days_matrix.append([[['none'] for i in range(5)]for j in range(10)])
        week_work_days_matrix.append([[['none'] for i in range(5)]for j in range(10)])
        week_work_days_matrix.append([[['none'] for i in range(5)]for j in range(10)])
        week_work_days_matrix.append([[['none'] for i in range(5)]for j in range(10)])
        week_work_days_matrix.append([[['none'] for i in range(5)]for j in range(10)])
        self.main_database_object.days_matrix_setter(week_work_days_matrix)
    #fine Till Here
    def backtraking_and_forwardchecking(self):
        #grab the list of all teachers avaliable
        all_teacher_name_list = self.main_database_object.get_all_teachers_name_init()
        #this is the list of teachers taht have lessons to teach right now and in here we are initialising it
        self.main_database_object.set_list_of_remaining_teachers(all_teacher_name_list)
        #this will get the matrix that generated before #fine till here
        week_day_mat = self.main_database_object.days_matrix_getter()
        #this is the maximum time req for each lesson
        list_of_lessons_and_max_time = self.main_database_object.get_each_lesson_time_predict()
        #this the list of teachers and lessons than can be tought
        list_of_teachers_and_lessons = self.main_database_object.get_all_teach_less()
        #this is the total hours of lessons that needed
        list_of_lessons_and_req_time = self.main_database_object.get_total_lesson_and_time_req()
        #it will be save the total hours needed
        max_total_time_needed = self.main_database_object.get_total_integer_time_needed()
        #print('the list of lessons and max time is {} and the list of teachers and lessons is : {} and the list of llessons time requierd is {} and finally the max total time needed is : {}'.format(list_of_lessons_and_max_time, list_of_teachers_and_lessons, list_of_lessons_and_req_time, max_total_time_needed))
        #this will save the number of teachers
        print('total hours needed in line 275 is {} '.format(max_total_time_needed))
        #the number of avaliable teachers #fine till here
        teachers_number = len(list_of_teachers_and_lessons)
        #this is the list of remaining teachers that initialised in above
        teachers_list = self.main_database_object.get_list_of_remaining_teachers()# potential for problem PPPPPPPPPPP
        #get list of lessons avalible title initializing
        #lessons_list = self.main_database_object.get_lessons_list() changed
        lessons_list = self.main_database_object.get_remainig_lessons()
        #this will find the maximum classes that can be hold each day
        maximum_hours_canbe_teach_each_day = (teachers_number) * 5
        print('teachers number in line 284 is {} '.format(teachers_number))#tttttttttteeeeeeeeeeeeesssssssstttttttt
        #this if statement will find the days needed to make classes work
        if_condition_holder = (max_total_time_needed) / maximum_hours_canbe_teach_each_day
        if  if_condition_holder < 1 :
            days_needed_to_make_everything_work = 1
            print('test 1')#tttttttttteeeeeeeeeeeeesssssssstttttttt
        else:
            days_needed_to_make_everything_work = math.ceil((max_total_time_needed) / maximum_hours_canbe_teach_each_day)
            print('test 2')#tttttttttteeeeeeeeeeeeesssssssstttttttt
        print('days needed to make eve.. in line 293 is {}'.format(days_needed_to_make_everything_work))
        if days_needed_to_make_everything_work > 5:
            print('you can not handle this much of classes with this number of physycal classes and the teacher you have, try to do SMT.')
            print('bye bye')
            exit()
        #fine till here
        for day_counter in range(days_needed_to_make_everything_work):
            day_matrix = week_day_mat[day_counter]
            print('test 3')#tttttttttteeeeeeeeeeeeesssssssstttttttt
            for row in range(5):#traversing in columns
                print('test 4')#tttttttttteeeeeeeeeeeeesssssssstttttttt
                #check for the end of the lessons(returns True or False)
                finish = self.calculator_object.check_for_end()#fine till here if get finished less is true
                # if finish == False:
                #     print('test 5')#tttttttttteeeeeeeeeeeeesssssssstttttttt
                #     print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
                #     #self.calculator_object.days_of_week_matrix_drawer()
                #     break
                #this is valid teachers domain for each column (this is the copy from all teachers)
                teach_list = teachers_list.copy()
                #ttttttttttttttttttttteeeeeeeeeeeeessssssssssstttttttttt
                print('this is valid teachers name{} '.format(teach_list))
                print('this is valid lessons name{} '.format(lessons_list))
                for column in range(10):#traversing in each row
                    self.main_database_object.set_remainig_lessons()
                    #check for the end of the lessons(returns True or False) #neewwwwww cchhhaaannngggeeee
                    finish = self.calculator_object.check_for_end()#neeeeeeeeeeeeeeeeeeeedddddddddddddd to creaaaaaaateeeeeeeeee    is created
                    if finish == False:
                        print('test 5')#tttttttttteeeeeeeeeeeeesssssssstttttttt
                        print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
                        #self.calculator_object.days_of_week_matrix_drawer()
                        break
                    print('test 6')#tttttttttteeeeeeeeeeeeesssssssstttttttt
                    if len(teach_list) > 0:#problem  it need to traverse till end not from teachers
                    #if 5 > 0:# made a new change to check the program
                        print('test 7')#tttttttttteeeeeeeeeeeeesssssssstttttttt
                        teacher = teach_list.pop()
                        lesson = self.calculator_object.lesson_generator(teacher)#neeeeeeeeeeeeeeeeeeeedddddddddddddd to fiiiiiiixxxxxxxxxxxxx
                        print('this is selected teacher {} and this is selected lesson {} '.format(teacher, lesson))
                        self.calculator_object.remaining_class_calculator(lesson)
                        if lesson != 'None':
                            day_matrix[column][row].pop()
                            day_matrix[column][row].append([teacher, lesson])
                            #self.calculator_object.lesson_discount(lesson)#neeeeeeeeeeeeeeeeeeeedddddddddddddd to creaaaaaaateeeeeeeeee
                            #self.calculator_object.remaining_class_calculator(lesson)
                            print('test 10')#tttttttttteeeeeeeeeeeeesssssssstttttttt
                            #self.calculator_object.remaining_teacher_calc()

                    else:
                        print('test 8')#tttttttttteeeeeeeeeeeeesssssssstttttttt
                        # self.calculator_object.remaining_teacher_calc()
                        # teach_list = teachers_list.copy()#new change made
                        if len(teach_list) > 0:
                            teach_list.pop()#new change
                        break

    def final_answer(self):
        print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
        self.calculator_object.days_of_week_matrix_drawer()
        




        #functional style coding guide ->:
        #dont use FOR in your code as possible : use MAP and FILTER Instead
        #use Immutability 
        #use Lamda functions and HOF 





b0 = Main_DB()
b1 = Teacher_DB(b0)
b2 = Teacher_DB(b0)
b2 = Teacher_Time_Calc(b0)
b2.each_lesson_calc()
b2.total_time_needed_calculator()
b3 = Which_day_to_assign(b0,b2)
b3.days_setter()
b3.backtraking_and_forwardchecking()
b3.final_answer()



#matrix = [[['teacher1', 'teacher2'] for i in range(5)]for j in range(10)]
# matrix = [[[0,'none', 'teacher1', 'teacher2'] for i in range(5)]for j in range(10)]
# for i in range(len(matrix)):
#     for j in range(5):
#         print(matrix[i][j], end='')
#     print('')

    
