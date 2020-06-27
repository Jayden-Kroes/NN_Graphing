import NNModel
import graph
import progress
from matplotlib import pyplot as plt

C_YES = 1
C_TOOK_TOO_LONG = 2
C_NO_PROGRESS = 3
C_GRADUATED = 4
C_UNENROLLED = 5

end_status = ""

class TrainingClass:
    def __init__(self, cohort, curriculum, 
                min_steps = 100, max_steps=None, 
                patience=10, improvement_ratio = 0.999, 
                graduation_value=0.0001, drop_failures=True, train_alumni=False, student_race=False,
                start_display_size=(20,20)):

        self._lesson_number = -1
        # curriculum is expected data
        self._curriculum = curriculum
        # cohort is list of models
        self._cohort = cohort

        # a list of every score for each student
        self._result_history = []

        self._official_highest_index = []

        # are they still being trained
        self._do_train_student = []
        # what output does the cohort produce
        self._cohort_displays = []


        for student in self._cohort:
            #add blank list for student
            self._result_history.append([])
            self._official_highest_index.append(-1)
            self._do_train_student.append(True)
            self._cohort_displays.append(
                graph.Model_Output(student.predict, start_display_size))
            progress.model_index +=1

        self._min_steps = min_steps
        self._max_steps = max_steps
        self._patience = patience
        self._improvement_ratio = improvement_ratio
        self._graduation_requirement = graduation_value

        self._do_drop_failures = drop_failures
        self._do_train_alumni = train_alumni
        self._do_have_student_race = student_race


    # train all students
    def run_lesson_training(self, graph_size = (20,20)):
        self._lesson_number += 1
        for index in range(len(self._cohort)):
            if self._do_train_student[index]:
                self._result_history[index].append(
                    self._cohort[index].train(
                        self._curriculum.get_data()[0], 
                        self._curriculum.get_data()[1]))
                
                progress.model_index = index
                #progress.model_loss = self._cohort[student].get_loss_history()[-1] if self._lesson_number >= 0 else 1.0
                progress.model_loss = self._result_history[index][-1] if self._lesson_number >= 0 else 1.0
                print()
                self._cohort_displays[index] = graph.Model_Output(self._cohort[index].predict, graph_size)
                


    # decide whether to continue training the class
    def do_continue_class(self):
        if self._lesson_number == -1:
            return True
        any_continue = False
        lesson_results = []

        # update student enrollment
        for studentId in range(len(self._cohort)):
            if self._do_train_student[studentId]:
                lesson_results.append(self.do_continue_student(studentId))
                if lesson_results[studentId] == C_YES:
                    any_continue = True
                elif lesson_results[studentId] == C_GRADUATED:
                    if not self._do_train_alumni:
                        self._do_train_student[studentId] = False
                elif lesson_results[studentId] == C_NO_PROGRESS or lesson_results[studentId] == C_TOOK_TOO_LONG:
                    if self._do_drop_failures:
                        self._do_train_student[studentId] = False
            else:
                lesson_results.append(C_UNENROLLED)

        if not any_continue:
            print()
            print(lesson_results)

        return any_continue
    
    # decide if a student should be continued
    def do_continue_student(self, index):

        # student has no recorded highest, but has started
        if self._official_highest_index[index] == -1 and len(self._result_history[index])> 0:
            self._official_highest_index[index] = 0
            return C_YES

        latest_acc = self._result_history[index][-1]
        prev_highest = self._result_history[index][self._official_highest_index[index]]

        # student has reached level of graduation
        if latest_acc <= self._graduation_requirement:
            self._official_highest_index[index] = len(self._result_history[index]) - 1
            return C_GRADUATED

        # student has attended the maximum possible classes
        above_max = (self._max_steps is not None and self._lesson_number >= self._max_steps)
        if above_max:
            return C_TOOK_TOO_LONG

        # update high score index
        if latest_acc <= prev_highest * self._improvement_ratio:
            self._official_highest_index[index] = len(self._result_history[index]) - 1
            return C_YES

        # student has not attended the minimum required classes
        below_min = (self._min_steps is not None and self._lesson_number < self._min_steps)
        if below_min:
            return C_YES
        
        # student has improved recently
        elif self._lesson_number <= self._official_highest_index[index] + self._patience:
                return C_YES

        # student is not making progress
        else:
            return C_NO_PROGRESS


    def display_class_results(self, file_name):
        plt.clf()
        figure, axes = plt.subplots(1, len(self._cohort), figsize=(16,9))
        figure.tight_layout(rect=[0, 0.03, 1, 0.85])
        # figure.subplots_adjust(top=0.8)
        title = 'Step ' + str(self._lesson_number+1) if self._lesson_number >= 0 else 'Start'
        figure.suptitle(title, fontsize=24, y=0.98)

        for student in range(len(self._cohort)):
            title = "Model " + str(student)+ (": " + str(self._result_history[student][-1]) if self._lesson_number >= 0 else " - Start")
            #graph.plot_model_output(positions, labels, self._cohort[student].predict, axes[student], x_parts=graph_detail, y_parts=graph_detail, title=title)
            graph.display_model_output(self._curriculum, self._cohort_displays[student], axes[student], title=title)
            
        
        if file_name is None:
            file_name = "plot.png"
        figure.savefig(file_name, dpi=(255))

        plt.close(figure)
        plt.clf()