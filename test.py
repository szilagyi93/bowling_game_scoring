import unittest
from BowlingGame import BowlingGame 

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

class ExtremalTestCase(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def test_zero(self):
        Rolls = [0,1]
        Frames = [0,1,2,3,4,5,6,7,8,9]
        self.game.rolls= [  [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],[]]
        for frame in Frames:
            for roll in Rolls:
                self.game.calc_scores(roll,frame)
        self.assertEqual(self.game.score, [0, 0, 0, 0, 0, 0,0, 0, 0, 0], "Zero score test faild")
        
    def test_max(self):
            Rolls = [0,1]
            Frames = [0,1,2,3,4,5,6,7,8,9]
            self.game.rolls= [  ['X','_'],
                                ['X','_'],
                                ['X','_'],
                                ['X','_'],
                                ['X','_'],
                                ['X','_'],
                                ['X','_'],
                                ['X','_'],
                                ['X','_'],
                                ['X','X','X']]
            #10x2 Rolls
            for frame in Frames:
                for roll in Rolls:
                    self.game.calc_scores(roll,frame)
            #Extra roll 10x2+1 
            self.game.calc_scores(Rolls[-1]+1,Frames[-1])
            self.assertEqual(self.game.score, [30, 60, 90, 120, 150, 180, 210, 240, 270, 300], "Maximum score test failed")

class CustomTestCase(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()  
    
    def test_one_to_ten(self):
        Rolls = [0,1]
        Frames = [0,1,2,3,4,5,6,7,8,9]
        self.game.rolls= [  [0,1],
                            [0,1],
                            [0,1],
                            [0,1],
                            [0,1],
                            [0,1],
                            [0,1],
                            [0,1],
                            [0,1],
                            [0,1],[]]
        for frame in Frames:
            for roll in Rolls:
                self.game.calc_scores(roll,frame)
        self.assertEqual(self.game.score, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Scores 1-10 test case failed!")  
    
    def test_mix_strike_and_spare(self):
        self.game.rolls = [
            ['X', '_'],   # Strike
            [9, '/'],     # Spare
            [5, 4],       # Open
            ['X', '_'],   # Strike
            [0, '/'],     # Spare after 0
            [3, 2], 
            [0, 0], 
            [0, 0],
            [0, 0], 
            [0, 0]]
        for frame_index in range(10):
            for roll_index in [0, 1]:
                self.game.calc_scores(roll_index, frame_index)
        expected_score = [20, 35, 44, 64, 77, 82, 82, 82, 82, 82]
        self.assertEqual(self.game.score, expected_score, "Mix of strikes and spares failed")


class TenthFrameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()
             
    def test_10th_frame_xxx(self):
        self.game.rolls= [  
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            ['X','X','X']]
            #10x2 Rolls
        for frame in range(10):
            for roll in [0, 1]:
                self.game.calc_scores(roll,frame)
            #Extra roll 10x2+1 
        self.game.calc_scores(2,9)
        expected_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 30]
        self.assertEqual(self.game.score, expected_score, "The 10th [X,X,X] failed")
    
    def test_10th_frame_xx_6(self):
        self.game.rolls= [  
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            ['X','X',6]]
            #10x2 Rolls
        for frame in range(10):
            for roll in [0, 1]:
                self.game.calc_scores(roll,frame)
            #Extra roll 10x2+1 
        self.game.calc_scores(2,9)
        expected_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 26]
        self.assertEqual(self.game.score, expected_score, "The 10th [X,X,6] failed")
    
    def test_10th_frame_x6_spare(self):
        self.game.rolls= [  
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            ['X',6,'/']]
            #10x2 Rolls
        for frame in range(10):
            for roll in [0, 1]:
                self.game.calc_scores(roll,frame)
            #Extra roll 10x2+1 
        self.game.calc_scores(2,9)
        expected_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 20]
        self.assertEqual(self.game.score, expected_score, "The 10th [X,6,/] failed")
        
    def test_10th_frame_6_spare_x(self):
        self.game.rolls= [  
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [6,'/','X']]
            #10x2 Rolls
        for frame in range(9):
            for roll in [0, 1]:
                self.game.calc_scores(roll,frame)
            #Extra roll 10x2+1 
        self.game.calc_scores(2,9)
        expected_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 20]
        self.assertEqual(self.game.score, expected_score, "The 10th [6,/,X] failed")

    def test_10th_frame_6_spare_2(self):
        self.game.rolls= [  
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [0,0],
                            [6,'/',2]]
            #10x2 Rolls
        for frame in range(9):
            for roll in [0, 1]:
                self.game.calc_scores(roll,frame)
            #Extra roll 10x2+1 
        self.game.calc_scores(2,9)
        expected_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 12]
        self.assertEqual(self.game.score, expected_score, "The 10th [6,/,2] failed")

if __name__ == '__main__':
    unittest.main()