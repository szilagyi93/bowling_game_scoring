# bowling_game_scoring

This is my solution of the coding challenge.<br />
<br />
In this folder, you can find 3+1 python files. <br />
&emsp; 1. ui.py - This is the GUI scoring a game. <br />
&emsp; 2. BowlingGame.py - The scoring logic is implemented here. This is the quasi-backend.<br />
&emsp; 3. test.py - Here you can find some unit tests for BowlingGame.py. <br />
&emsp; &emsp; This is not complete yet.<br />
&emsp; &emsp; Only edge cases and  some custom cases are tested. <br />
&emsp; +1. InputHandeler.py - Just for further improvements.... (currently out of usage ) <br />
<br />
For using this scoring UI, the mentioned .py files should be in the same folder.<br />
<br />
The UI is implemented in a way, where the user is not able to write invalid or nonsense values.<br />
<br />
HOW DOES IT WORKS: <br />
After you run the UI.py you can see the the 9+1 Frames for scoring a bowling game. <br />
Under each frame a 'Score:' can be found, where you can check your actual scores. <br />
The cursor is in the 1st Frame's 1st entry. Here you can type in your score which can be [0..9] or "/" or "x" or "X". <br />
If you type in an invalid value the UI going to delete that. <br />
The cursor is auto-advanced so after you type in your score, the cursor going to move to the next possible frame.<br />
So after you type in a valid value into the given entry, the BowlingGame.get_UI_input() reads the value and stores it into the BowlingGame.rolls[[][]] list. <br />
If possible, the BowlingGame.calc_scores() method calculates the actual scores and soter them into a list BowlingGame.score[].<br />
The UI displays your scores using the BowlingUI.update_ui_scores() method in a way that checks the length of the BowlingGame.score list and values.<br />
You can use the RESET button to clear the scores and the rolls. <br />

<br />
Some improvement points: <br />
Sofver-Side: <br />
&emsp; 1.1. The BowlingGame.py also should handle the invalid values.<br /> 
&emsp;&emsp; Eg.: The use type int a value on the UI. <br />
&emsp;&emsp; The BowlingGame class checks this value and returns a signal that indicates if the value is OK or not.<br />
&emsp;&emsp; If not the value should be deleted by the UI automatically. <br />
&emsp;&emsp; If the value is correct then shall be stored and calculated the score if possible. <br />
&emsp; 2.2. Implement the InputHandler class for validating the I/O values. Tipp: use regex! <br />
&emsp; 2.3. Rename and cut for shorter functions the handle_frames_1_to_9(), handle_frame_10 methods() and calc_scores() <br />
<br /> 
Test-Side: <br />
&emsp; 2.1. Functional and test requirements: The software and the tests should have requirements. <br />
&emsp; 2.2. Test input and output should be stored in a .csv or xml file. <br />
&emsp; 2.3. Full coverage test: All methods shall be tested in valid and invalid ranges. <br />
&emsp; 2.4. Automated UI test: In pywinauto the UI (which is implemented using by Tkinter) can be tested. <br /> 
&emsp;&emsp; So after you have pywinauto you can create some scenarios for typing in invalid or nonsense values into the UI. <br />
&emsp;&emsp; This could be implemeted in another class, like UI_test.py.



