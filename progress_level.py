lst_level = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
start_level = 0
start_progress = 0
class User:
    def __init__(self):
        self.lst_level = lst_level
        self.start_level = start_level
        self.progress_level = start_progress
    

    def rank(self):
        self.level = self.lst_level[self.start_level]
        return print(self.level)


    def progress(self):
        if self.progress_level >= 100:
            repeat = self.progress_level
            repeat = str(repeat)
            repeat = repeat[0]
            for i in range(int(repeat)):
                self.start_level += 1
                self.progress_level -= 100
                return print(self.progress_level)
        else:
            return print(self.progress_level)
        


    def inc_progress(self, level_task):

        ind_task = None
        ind_lvl = None

        for i in range(15):
            if level_task == self.lst_level[i]:
                ind_task = i
            if self.lst_level[start_level] == self.lst_level[i]:
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
        
        
        

user1 = User()
user = User()
user.rank() # => -8
user.progress() # => 0
user.inc_progress(-7)
user.progress() # => 10
user.inc_progress(-5) # will add 90 progress
user.progress() # => 0 # progress is now zero
user.rank() # => -
