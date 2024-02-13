# bowling_game_scoring

This my solution of the coding challenge.<br />
<br />
In this file you can find 3 python files. <br />
&emsp; 1. ui.py - This is the GUI scoring a game. <br />
&emsp; 2. BowlingGame.py - The scoring logic is implemented here. This is the quasi-backend.<br />
&emsp; 3. test.py - Here you can find some unit tests for BowlingGame.py. <br />
&emsp; This is not complete yet.<br />
&emsp; Only edge cases and  some custom cases are tested. <br />
<br />
For using this scoring UI, the mentioned .py files should be in the same folder.<br />
<br />
The UI  is implemented in a way, where the user is not able to write invalid or nonsense values.<br />
<br />
Some improvement points: <br />
Sofver-Side: <br />
&emsp; 1.1. The BowlingGame.py also should handle the invalid values.<br /> 
&emsp;&emsp; Eg.: The use type int a value on the UI. <br />
&emsp;&emsp; The BowlingGame class checks this value and returns a signal that indicates if the value is OK or not.<br />
&emsp;&emsp; If not the value should be deleted by the UI automatically. <br />
&emsp;&emsp; If the value is correct then shall be stored and calculated the score if possible. <br />
&emsp; 2.2. Implement the InputHandler class for validating the I/O values. Tipp: use regex! <br />
&emsp; 2.3. Rename and cut for shorter functions the handle_frames_1_to_9 and handle_frame_10 methods.<br />
<br /> 
Test-Side: <br />
&emsp; 2.1. Functional and test requirements: The software and the tests should have requirements. <br />
&emsp; 2.2. Test input and output should be stored in a .csv or xml file. <br />
&emsp; 2.3. Full coverage test: All methods shall be tested in valid and invalid ranges. <br />
&emsp; 2.4. Automated UI test: In pywinauto the UI (which is implemented using by Tkinter) can be tested. <br /> 
&emsp;&emsp; So after you have pywinauto you can create some scenarios for typing in invalid or nonsanse values into the UI. <br />
&emsp;&emsp; This could be implemeted in another class, like UI_test.py.



