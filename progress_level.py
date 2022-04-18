lst_level = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
start_level = 0

level_g = lst_level[start_level]
start_progress = 0
class User:
    def __init__(self, level = -8, progress_level = 0):
        self.lst_level = lst_level
        self.start_level = start_level
        
        self.level = level

        progress_level = start_progress
        self.progress_level = progress_level

    def rank(self):
        if self.progress_level >= 100:
            repeat = self.progress_level
            repeat = str(repeat)
            repeat = repeat[0]
            for i in range(int(repeat)):
                self.start_level += 1
                self.level = self.lst_level[self.start_level]
                self.progress_level -= 100
            print(self.level)
            print(self.progress_level)
        else:
            print(self.level)
            print(self.progress_level)

    def inc_progress(self, level_task):
        ind_task = 0
        ind_lvl = 0

        for i in range(15):
            if level_task == self.lst_level[i]:
                ind_task = i
            if self.level == self.lst_level[i]:
                ind_lvl = i
            
        if ind_lvl > ind_task:
            if ind_lvl - ind_task == 1:
                self.progress_level += 1
            else:
                print('слишком легкая задача')

        elif ind_lvl == ind_task:
            self.progress_level += 3 

        elif ind_lvl < ind_task:
            d = ind_task - ind_lvl
            progress = 10 * d * d
            self.progress_level += progress