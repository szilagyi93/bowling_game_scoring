class BowlingGame:
    def __init__(self):
        self.rolls= [[[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[],[]]]
        self.score = []
        self.is_valid_input = False
        self.after_strike_marker = '_' # The '_' represents the skipped roll after a Strike

    def get_UI_input(self, input_val, entry_index ,current_frame_index):
        is_valid_entry_index = (entry_index >= 0 and entry_index <= 2) 
        is_valid_current_frame_index = (current_frame_index >= 0 and current_frame_index <= 9)
        #Validity checking
        if is_valid_entry_index and is_valid_current_frame_index:
            #For 1.-9. Frames
            if current_frame_index < 9 and current_frame_index >= 0:
                self.handle_frames_1_to_9(input_val,entry_index, current_frame_index)
            #For 10. Frame
            else:
                self.handle_frame_10(input_val,entry_index, current_frame_index)
                
    def handle_frames_1_to_9(self, input_val, entry_index,current_frame_index):
        #For Numbers
        if input_val.isdigit():
            input_val = int(input_val)
            is_input_val_in_range = (input_val >= 0 and input_val <= 9)
            if not is_input_val_in_range:
                self.is_valid_input = False
            else:
                self.is_valid_input = True
                #First Roll in a Frame
                if entry_index == 0:
                    self.rolls[current_frame_index][entry_index] = input_val
                #Secound Roll in a Frame 
                if entry_index == 1:
                    self.rolls[current_frame_index][entry_index] = input_val
                                
        #For Spare               
        elif input_val.upper() == "/":
            is_after_strike =  (self.rolls[-1] == self.after_strike_marker)
            is_from_secound_roll = (entry_index == 1) 
            if [is_from_secound_roll and not is_after_strike]:
                self.is_valid_input = True
                self.rolls[current_frame_index][entry_index] = input_val     
 
        #For STRIKE
        elif input_val.upper() == "X":
            is_from_first_roll = (entry_index == 0) 
            if is_from_first_roll:
                self.rolls[current_frame_index][entry_index] = input_val
                self.rolls[current_frame_index][entry_index+1] = self.after_strike_marker 
                self.is_valid_input = True 
        else:
            self.is_valid_input = False
        #print(self.rolls)  
    
    def handle_frame_10(self, input_val, entry_index,current_frame_index):
        self.rolls[9][int(entry_index)] = input_val

    def calc_scores(self,current_roll_index,current_frame_index):
        #1.Frame
        if current_frame_index == 0: 
            #1.Roll
            if current_roll_index == 0:
                if self.is_open_frame(current_roll_index,current_frame_index):  #|8, |
                    pass
                if self.is_spare(current_roll_index,current_frame_index):       #|N/A,|
                    pass
                if self.is_strike(current_roll_index,current_frame_index):      #|X, |
                    pass
            #2.Roll    
            if current_roll_index == 1:
                if self.is_open_frame(current_roll_index,current_frame_index):  #|2,4|
                    sc = self.frame_sum(current_frame_index)
                    self.score.append(sc)
                if self.is_spare(current_roll_index,current_frame_index):       #|5,N/A|
                    pass
                if self.is_strike(current_roll_index,current_frame_index):      #|2,/|
                    pass
        #2.Frame     
        elif current_frame_index == 1:
            #1.Roll
            if current_roll_index == 0:                     #|2,5|2, |       
                if self.is_spare(1,current_frame_index-1):  
                    prev_frame_score = 10
                    curr_roll = self.rolls[current_frame_index][0]
                    if str(curr_roll).lower() == 'x':       #|2,/|x,_|
                        curr_roll = 10
                        sc = prev_frame_score + curr_roll
                        self.score.append(sc)
                    else:
                        sc = prev_frame_score + curr_roll  #|2,/|6, |
                        self.score.append(sc)
                if self.is_strike(current_roll_index,current_frame_index-1):  #|x,_|6, |
                    None 
            #2.Roll       
            if current_roll_index == 1: 
                if self.is_strike(0,current_frame_index-1):  #|x,_|,| , |
                    if self.is_spare(current_roll_index,current_frame_index):#|x,_|,|6,/|
                        sc = 20                                                     
                        self.score.append(sc)
                    if self.is_open_frame(current_roll_index,current_frame_index): #|x,_|,|6,2|
                        sc_prev_roll = 10
                        sc_curr_frame = self.frame_sum(current_frame_index) 
                        sc = sc_prev_roll + sc_curr_frame                                              
                        self.score.append(sc)
                        self.score.append(sc+sc_curr_frame)
                    if self.is_strike(current_roll_index,current_frame_index-1): #|x,_|,|x,_|
                        pass                                                
                    
                elif self.is_open_frame(current_roll_index,current_frame_index): 
                    if self.is_open_frame(current_roll_index,current_frame_index-1): #|2,3|,|2,6|
                        sc = self.frame_sum(current_frame_index) 
                        self.score.append(sc + self.score[-1])

        #2 < N < 10 Frames
        if current_frame_index >1 and current_frame_index < 9:
            #Roll 1
            if current_roll_index == 0:
                if self.is_strike(0,current_frame_index-2):    #|x,_||?,?||?,?|
                    if self.is_strike(0,current_frame_index-1): 
                        curr_roll = self.rolls[current_frame_index][current_roll_index] 
                        if str(curr_roll).lower() == 'x':       #|x,_||x,_||x,_|
                            sc_curr_roll = 10
                            sc_prev_prev_roll = self.frame_sum(current_frame_index-2)
                            sc_prev_roll = self.frame_sum(current_frame_index-1)
                            sc = sc_curr_roll + sc_prev_roll + sc_prev_prev_roll
                            if len(self.score) < 1:
                                self.score.append(sc)
                            else:
                                self.score.append(sc + self.score[-1])  
                        else:                                   #|x,_||x,_||5,_|
                            sc_curr_roll = self.rolls[current_frame_index][current_roll_index]
                            sc_prev_prev_roll = self.frame_sum(current_frame_index-2)
                            sc_prev_roll = self.frame_sum(current_frame_index-1)      
                            sc = sc_curr_roll + sc_prev_roll + sc_prev_prev_roll 
                            if len(self.score) < 1:
                                self.score.append(sc)
                            else:
                                self.score.append(sc + self.score[-1]) 
                if self.is_spare(1,current_frame_index-1):   #|?,?||2,/||?,?|
                        prev_frame_score = 10
                        curr_roll = self.rolls[current_frame_index][current_roll_index]
                        if str(curr_roll).lower() == 'x':      
                            curr_roll = 10
                            sc = prev_frame_score + curr_roll
                            self.score.append(sc+self.score[-1])
                        else:
                            sc = prev_frame_score + curr_roll 
                            self.score.append(sc+self.score[-1])
                   
            #Roll 2       
            if current_roll_index == 1:  
                if self.is_strike(0,current_frame_index-1):
                    if self.is_spare(current_roll_index,current_frame_index):#|x,_|,|6,/|
                        sc = 20                                                     
                        self.score.append(sc+self.score[-1])
                    if self.is_open_frame(current_roll_index,current_frame_index): #|x,_|,|6,2|
                        sc_prev_roll = 10
                        sc_curr_frame = self.frame_sum(current_frame_index) 
                        sc = sc_prev_roll + sc_curr_frame                                              
                        self.score.append(self.score[-1] + sc)
                        self.score.append(self.score[-1] + sc_curr_frame)
                    if self.is_strike(current_roll_index,current_frame_index): #|x,_|,|x,_|
                        pass                               
                elif self.is_open_frame(current_roll_index,current_frame_index-1):
                    if self.is_open_frame(current_roll_index,current_frame_index):
                        sc_curr_frame = self.frame_sum(current_frame_index) 
                        self.score.append(self.score[-1] + sc_curr_frame)   
                    if self.is_spare(current_roll_index,current_frame_index):
                        pass
                    if self.is_strike(current_roll_index,current_frame_index-1):
                        pass
                elif self.is_spare(current_roll_index,current_frame_index-1):
                    if self.is_open_frame(current_roll_index,current_frame_index):
                        sc_curr_frame = self.frame_sum(current_frame_index) 
                        self.score.append(self.score[-1] + sc_curr_frame)  

        #Frame 10th
        if current_frame_index == 9:
            #Roll 1
            if current_roll_index == 0:
                if self.is_strike(0,current_frame_index-2):    #|x,_||x,_||?,?,?|
                    if self.is_strike(0,current_frame_index-1): #|x,_||x,_||?,?,?|
                        curr_roll = self.rolls[current_frame_index][current_roll_index] 
                        if str(curr_roll).lower() == 'x':       #|x,_||x,_||x,?,?|
                            sc_curr_roll = 10
                            sc_prev_prev_roll = self.frame_sum(current_frame_index-2)
                            sc_prev_roll = self.frame_sum(current_frame_index-1)
                            sc = sc_curr_roll + sc_prev_roll + sc_prev_prev_roll
                            if len(self.score) < 1:
                                self.score.append(sc)
                            else:
                                self.score.append(sc + self.score[-1])  
                        else:                                   #|x,_||x,_||3,?,?|
                            sc_curr_roll = int(self.rolls[current_frame_index][current_roll_index])
                            sc_prev_prev_roll = self.frame_sum(current_frame_index-2)
                            sc_prev_roll = self.frame_sum(current_frame_index-1)      
                            sc = sc_curr_roll + sc_prev_roll + sc_prev_prev_roll 
                            if len(self.score) < 1:
                                self.score.append(sc)
                            else:
                                self.score.append(sc + self.score[-1]) 
                if self.is_spare(1,current_frame_index-1):   #|2,/||?,?,?|
                        prev_frame_score = 10
                        curr_roll = self.rolls[current_frame_index][current_roll_index]
                        if str(curr_roll).lower() == 'x':   #|2,/||x,?,?|   
                            curr_roll = 10
                            sc = prev_frame_score + curr_roll
                            self.score.append(sc+self.score[-1])
                        else:
                            sc = prev_frame_score + curr_roll #|2,/||3,?,?|
                            self.score.append(sc+self.score[-1])            
            #Roll 2       
            if current_roll_index == 1:  
                if self.is_strike(0,current_frame_index-1):  
                    if str(self.rolls[current_frame_index][0]).lower() == 'x':#|x,_||x, ,?|
                        if str(self.rolls[current_frame_index][current_roll_index]).lower() == 'x': #|x,_||x,x,?|
                            sc = 30 #|x,_||x,x,?|
                            self.score.append(sc+self.score[-1])
                        else: 
                            sc_curr = self.rolls[current_frame_index][current_roll_index]         #|x,_||x,3,?|
                            sc_prev = 10
                            sc_prev_prev  = 10
                            sc = sc_prev_prev + sc_prev + int(sc_curr)
                            self.score.append(sc+self.score[-1])      
                    if self.is_spare(current_roll_index,current_frame_index):                      #|x,_|,|6,/,?|
                        sc = 20                                                     
                        self.score.append(sc+self.score[-1])
                        
                    if self.is_open_frame(current_roll_index,current_frame_index):                 #|x,_|,|6,2,N/A|
                        sc_prev_roll = 10
                        sc_curr_frame = self.frame_sum(current_frame_index) 
                        sc = sc_prev_roll + sc_curr_frame                                              
                        self.score.append(self.score[-1] + sc)
                        self.score.append(self.score[-1] + sc_curr_frame)
                    if self.is_strike(current_roll_index,current_frame_index): #|x,_|,|x,_|
                        pass                               
                elif self.is_open_frame(current_roll_index,current_frame_index-1):
                    if self.is_open_frame(current_roll_index,current_frame_index):
                        sc_curr_frame = self.frame_sum(current_frame_index) 
                        self.score.append(self.score[-1] + sc_curr_frame)   
                    if self.is_spare(current_roll_index,current_frame_index):
                        pass
                    if self.is_strike(current_roll_index,current_frame_index-1):
                        pass
                elif self.is_spare(current_roll_index,current_frame_index-1):
                    if self.is_open_frame(current_roll_index,current_frame_index):
                        sc_curr_frame = self.frame_sum(current_frame_index) 
                        self.score.append(self.score[-1] + sc_curr_frame)
            #Roll 3
            if current_roll_index == 2:
                if self.rolls[9][0] == 'X' and self.rolls[9][1] == 'X' and self.rolls[9][2] == 'X':
                    sc = 30
                    self.score.append(sc+self.score[-1])
                elif self.rolls[9][0] == 'X' and self.rolls[9][1] == 'X' and str(self.rolls[9][2]).isdigit():
                    sc = 10 + 10 + int(self.rolls[9][2])
                    self.score.append(sc+self.score[-1])
                elif self.rolls[9][0] == 'X' and str(self.rolls[9][1]).isdigit():
                    sc_0 = 10
                    sc_1 = int(self.rolls[9][1])
                    if self.rolls[9][2] == "/":
                        sc_3 = 10 - sc_1
                    else:
                        sc_3 = int(self.rolls[9][2])
                    sc = sc_0+sc_1+sc_3
                    self.score.append(sc+self.score[-1])
                elif str(self.rolls[9][0]).isdigit() and self.rolls[9][1] == '/':
                    sc_1 = 10
                    if  self.rolls[9][2] == 'X':
                        sc_2 = 10 
                    else:
                        sc_2 = int(self.rolls[9][2])
                    sc = sc_1+sc_2
                    self.score.append(sc+self.score[-1])

    def reset_socore(self):
        self.pp_rolls = [[]]
        self.rolls= [[[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[]],
                     [[],[],[]]]
        self.score = []
        self.is_valid_input = False
        self.after_strike_marker = '_'
        return True

    def is_spare(self,roll_index,frame_index):
        if roll_index == 1:
            return self.rolls[frame_index][1] == '/'
        else:
            return False
    
    def is_strike(self,roll_index,frame_index):
        if roll_index == 0:
            roll1 = self.rolls[frame_index][0]
            #roll2 = self.rolls[frame_index][1]
            #return str(roll1).lower() == 'x' and str(roll2).lower('_')
            return str(roll1).lower() == 'x' 
        else:
            return False
        
    def is_open_frame(self,roll_index,frame_index):
        if roll_index == 1:
            roll1 = self.rolls[frame_index][0]
            roll2 = self.rolls[frame_index][1]
            return (str(roll1).isdigit() and str(roll2).isdigit())
        else:
            return False
    
    def frame_sum(self,frame_index):
        roll1 = self.rolls[frame_index][0]
        roll2 = self.rolls[frame_index][1]
        if str(roll1).lower() == 'x':
            return 10
        if str(roll2).lower() == '/':
            return 10
        if (str(roll1).isdigit() and str(roll2).isdigit()): 
            return int(roll1)+int(roll2)
