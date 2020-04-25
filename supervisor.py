class Supervisor:
    def __init__(self, min_steps = 100, max_steps=None, patience=10, improvement_ratio = 0.999, graduation_value=0.0001):
        self._smallest_loss = 1.0
        self._smallest_loss_index = -1
        self._current_index = -1

        self.min_steps = min_steps
        self.max_steps = max_steps
        self.patience = patience
        self.improvement_ratio = improvement_ratio
        self.graduation_value = graduation_value

        self.end_status = ''

    def do_continue(self, new_loss):
        self._current_index += 1
        if new_loss < self._smallest_loss * self.improvement_ratio:
            self._smallest_loss = new_loss
            self._smallest_loss_index = self._current_index

        if new_loss <= self.graduation_value:
            print("\nReached high accuracy")
            self.end_status = "Success"
            return False

        below_min = self.min_steps is not None and self._current_index < self.min_steps 
        if below_min:
            return True
        
        above_max = self.max_steps is not None and self._current_index >= self.max_steps
        if above_max:
            print("\nMax steps reached")
            self.end_status = "Failed - took too long"
            return False

        if self._smallest_loss_index == self._current_index:
            return True

        else:
            if self._current_index <= self._smallest_loss_index + self.patience:
                return True
            else:
                print("\nNo progress made")
                self.end_status = "Failed - no progress"
                return False

