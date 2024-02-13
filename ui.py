import tkinter as tk
from BowlingGame import BowlingGame 

class BowlingUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frames = []  # Store frame entries, labels, and frame instances
        self.init_ui()
        self.game = BowlingGame()
        
    def init_ui(self):
        self.title("Bowling Score Tracker")
        for frame_number in range(1, 11):
            frame = tk.LabelFrame(self, text=f"Frame {frame_number}", padx=5, pady=5)
            frame.grid(row=0, column=frame_number-1, padx=10, pady=10, sticky='nsew')
            entries = [self.create_entry(frame) for _ in range(2)] if frame_number < 10 else [self.create_entry(frame) for _ in range(3)]
            for i, entry in enumerate(entries):
                entry.grid(row=0, column=i, padx=5, pady=2)
            score_label = tk.Label(frame, text="Score: 0")
            score_label.grid(row=1, column=0, columnspan=3 if frame_number == 10 else 2, pady=2)
            self.frames.append(entries + [score_label])
        reset_button = tk.Button(self, text="RESET", command=self.reset_scores)
        reset_button.grid(row=1, column=0, columnspan=10, pady=20)
        if self.frames:
            self.frames[0][0].focus_set()
            
    def create_entry(self, parent):
        entry = tk.Entry(parent, width=2)
        entry.bind("<KeyRelease>", lambda event, e=entry: self.validate_entry(e))
        return entry

    def validate_entry(self, entry):
        val = entry.get().upper()
        current_frame_index = self.find_focused_frame()
        current_frame = self.frames[current_frame_index]
        if current_frame_index < 9:  # Handling for frames 1-9
            self.handle_frames_1_to_9(entry, val, current_frame, current_frame_index)
        else:  # Handling for frame 10
            self.handle_frame_10(entry, val, current_frame)

    def handle_frames_1_to_9(self, entry, val, current_frame, current_frame_index):
        index = current_frame.index(entry)
        entries = current_frame[:2]
        first_val = entries[0].get().upper()
        # Numeric input handling
        if val.isdigit():
            val_int = int(val)
            if index == 0:
                # Ensure the first entry in [0-9]
                if val_int < 0 or val_int > 9:
                    entry.delete(0, tk.END)
                else:
                    #Get the value from UI
                    self.game.get_UI_input(entry.get(), index,current_frame_index)
                    self.game.calc_scores(index,current_frame_index)
                    #print(self.game.score)
                    self.update_ui_scores() 
                    entries[1].focus_set()
            elif index == 1:
                if first_val.isdigit() and (val_int <= (9-int(first_val)) ):
                    #Get the value from UI
                    self.game.get_UI_input(entry.get(), index,current_frame_index)
                    self.game.calc_scores(index,current_frame_index)
                    #print(self.game.score)
                    self.update_ui_scores() 
                    #Move kurzor
                    self.frames[current_frame_index + 1][0].focus_set()             
                else:
                    entry.delete(0, tk.END)
        #Spare input handling
        elif val == "/":
            # Spare handling for the second entry only, ensuring the first entry is not a strike
            if index == 1 and first_val.isdigit() and 0 <= int(first_val) < 10:
                if current_frame_index + 1 <= len(self.frames) - 1:
                    self.game.get_UI_input(entry.get(), index,current_frame_index)
                    self.game.calc_scores(index,current_frame_index)
                    #print(self.game.score)
                    self.update_ui_scores()    
                    self.frames[current_frame_index + 1][0].focus_set()
            else:
                entry.delete(0, tk.END)
        # Strike handling for the first entry
        elif index == 0 and val == "X":
            entry.delete(0, tk.END)
            entry.insert(0, "X")
            if len(entries) > 1:
                entries[1].delete(0, tk.END)
            if current_frame_index + 1 < len(self.frames):  # Ensure we're not at the last frame
                self.game.get_UI_input(entry.get(), index,current_frame_index)
                self.game.calc_scores(index,current_frame_index)
                #print(self.game.score)
                self.update_ui_scores()    
                self.frames[current_frame_index + 1][0].focus_set()
            return
        else:
            # Clear invalid input
            entry.delete(0, tk.END)
        
    def handle_frame_10(self, entry, val, current_frame):
        index = current_frame.index(entry)
        entries = current_frame[:3]  # In the 10th Frame are 3 rolls
        first_val = entries[0].get().upper()
        second_val = entries[1].get().upper() if len(entries) > 1 else ""
        third_val = entries[2].get().upper() if len(entries) > 2 else ""

        # Strike handling for the first and second entries
        if val == "X":
            entry.delete(0, tk.END)
            entry.insert(0, "X")
            if index <= 2:  
                self.game.get_UI_input(entry.get(), index,9)
                self.game.calc_scores(index,9)
                self.update_ui_scores()
                #print(self.game.rolls)
                if index == 1:
                    if first_val != 'X':
                        entry.delete(0, tk.END)
                        return
                if index == 2:
                    entries[index].focus_set()
                    self.update_ui_scores()
                else:
                    entries[index + 1].focus_set()
            self.update_ui_scores()
            return

        # Numeric input handling for all three shots
        if val.isdigit():
            val_int = int(val)
            # [0..9]
            if val_int < 0 or val_int > 9:
                entry.delete(0, tk.END)
            elif index < 2:  # For the 1. and 2. rolls (in 10th Frame)
                #eg.:|2|| || |
                if index == 0:
                    self.game.get_UI_input(entry.get(), index,9)
                    self.game.calc_scores(index,9)
                    entries[1].focus_set()
                #eg.:|2||1|| | or |X||1|| | or |2||/|| | 
                elif index == 1:
                    self.game.get_UI_input(entry.get(), index,9)
                    self.game.calc_scores(index,9)
                    if (first_val == "X" or (second_val == '/')):
                        entries[2].focus_set()
            # eg.:|X||X||2| or |X||0||2| or  |1||/||2|              
            elif index == 2 and (second_val== "/" or second_val == "X" or first_val == "X"):
                self.game.get_UI_input(entry.get(), index,9) 
                self.game.calc_scores(index,9)            
            self.update_ui_scores()
            return
        
        # Spare handling for the second shot, enabling third shot
        # eg.:|2||/||enable|
        elif val == "/" and index == 1:
            if first_val.isdigit():
                    self.game.get_UI_input(entry.get(), index,9)  
                    entries[2].focus_set()
            else:
                entry.delete(0, tk.END)
            return
        # eg.:|X||2|/|
        elif val == "/" and index == 2:
            if second_val.isdigit():
                if first_val == "X":
                    entry.delete(0, tk.END)
                    entry.insert(0, "/")
                    self.game.get_UI_input(entry.get(), index,9)
                    self.game.calc_scores(index,9)
                    self.update_ui_scores()
            else:
                # Clear invalid input
                entry.delete(0, tk.END) 
        else:
            # Clear invalid input
            entry.delete(0, tk.END) 

    def reset_scores(self):
        for frame_widgets in self.frames:
            for entry in frame_widgets[:-1]:  # We exclude the score label
                entry.delete(0, tk.END)
            frame_widgets[-1].config(text="Score: 0")
        self.game.reset_socore()    
        self.frames[0][0].focus_set()  # Focus on the first entry of Frame 1 after reset

    def find_focused_frame(self):
        for i, frame_data in enumerate(self.frames):
            entry_widgets = frame_data[:-1]  # Exclude the score label
            for entry in entry_widgets:
                if entry == self.focus_get():
                    return i
        return None

    def update_ui_scores(self):
        for i, score in enumerate(self.game.score):
            if i < len(self.frames):
                frame_widgets = self.frames[i]
                score_label = frame_widgets[-1]  
                score_label.config(text=f"Score: {score}")
            else:
                break
if __name__ == "__main__":
    app = BowlingUI()
    app.mainloop()
