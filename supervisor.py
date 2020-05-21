import NNModel

C_YES = 1
C_TOOK_TOO_LONG = 2
C_NO_PROGRESS = 3
C_GRADUATED = 4
C_UNENROLLED = 5

class TrainingClass:
    def __init__(self, cohort, curriculum, min_steps = 100, max_steps=None, patience=10, improvement_ratio = 0.999, graduation_value=0.0001, drop_failures=True, train_alumni=True, student_race=False):
        self._lesson_number = -1
        self.curriculum = curriculum
        self.cohort = cohort
        self.mark_list = []
        self.is_enrolled = []
        for student in cohort:
            self.mark_list.append({"lesson": -1, "mark": 1.0})
            self.is_enrolled.append(True)
        self.min_steps = min_steps
        self.max_steps = max_steps
        self.patience = patience
        self.improvement_ratio = improvement_ratio
        self.graduation_value = graduation_value

        self.drop_failures = drop_failures
        self.train_alumni = train_alumni
        self.student_race = student_race

        self.end_status = ''

    def begin_new_lesson(self):
        self._lesson_number += 1
        for index in range(len(self.cohort)):
            if self.is_enrolled[index]:
                self.cohort[index].teach(self.curriculum.get_data()[0], self.curriculum.get_data()[1])
                print('\rLesson', self._lesson_number, 'Student', index,'\r')
        print()

    def continue_class(self):
        if self._lesson_number == -1:
            return True
        any_continue = False
        lesson_results = []
        for studentId in range(len(self.cohort)):
            if self.is_enrolled:
                lesson_results.append(self.do_continue(studentId))
                if lesson_results[studentId] == C_YES:
                    any_continue = True
            else:
                lesson_results.append(C_UNENROLLED)
        for studentId in range (len(self.cohort)):
            if lesson_results[studentId] == C_YES:
                pass
            elif lesson_results[studentId] == C_GRADUATED:
                if not self.train_alumni:
                    self.is_enrolled = False
            elif self.drop_failures:
                self.is_enrolled = False

        print (any_continue)   
        return any_continue
             


    def do_continue(self, index):
        new_loss = self.cohort[index].get_loss_history()[-1]
        if new_loss < self.mark_list[index]["mark"] * self.improvement_ratio:
            self.mark_list[index]["mark"] = new_loss
            self.mark_list[index]["lesson"] = self._lesson_number

        if new_loss <= self.graduation_value:
            print("\nReached high accuracy")
            self.end_status = "Success"
            return C_GRADUATED

        below_min = self.min_steps is not None and self._lesson_number < self.min_steps 
        if below_min:
            return C_YES
        
        above_max = self.max_steps is not None and self._lesson_number >= self.max_steps
        if above_max:
            print("\nMax steps reached")
            self.end_status = "Failed - took too long"
            return C_TOOK_TOO_LONG

        if self.mark_list[index]["lesson"] == self._lesson_number:
            return C_YES

        else:
            if self._lesson_number <= self.mark_list[index]["lesson"]+ self.patience:
                return C_YES
            else:
                print("\nNo progress made")
                self.end_status = "Failed - no progress"
                return C_NO_PROGRESS

