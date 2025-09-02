import unittest
from unittest.mock import patch, Mock
from ACEest_Fitness import FitnessTrackerApp

class TestFitnessTrackerApp(unittest.TestCase):

    def setUp(self):
        # We need to mock the Tkinter Tk object to prevent it from trying to create a GUI
        # This patch will replace the tk.Tk class with a Mock object
        self.patcher = patch('tkinter.Tk')
        self.MockTk = self.patcher.start()
        
        # Instantiate the app with the mocked Tk object
        self.app = FitnessTrackerApp(self.MockTk())

    def tearDown(self):
        # Stop the patcher to restore the original Tk class
        self.patcher.stop()

    def test_add_workout_success(self):
        """Test adding a workout with valid input."""
        with patch('tkinter.Entry.get', side_effect=['Running', '30']), \
             patch('tkinter.messagebox.showinfo'):
            self.app.add_workout()
            self.assertEqual(len(self.app.workouts), 1)
            self.assertEqual(self.app.workouts[0]['workout'], 'Running')
            self.assertEqual(self.app.workouts[0]['duration'], 30)

    def test_add_workout_missing_fields(self):
        """Test adding a workout with missing input."""
        with patch('tkinter.Entry.get', side_effect=['', '']), \
             patch('tkinter.messagebox.showerror') as mock_error:
            self.app.add_workout()
            mock_error.assert_called_with("Error", "Please enter both workout and duration.")
            self.assertEqual(len(self.app.workouts), 0)

    def test_add_workout_invalid_duration(self):
        """Test adding a workout with a non-integer duration."""
        with patch('tkinter.Entry.get', side_effect=['Cycling', 'forty']), \
             patch('tkinter.messagebox.showerror') as mock_error:
            self.app.add_workout()
            mock_error.assert_called_with("Error", "Duration must be a number.")
            self.assertEqual(len(self.app.workouts), 0)

    def test_view_workouts_empty(self):
        """Test viewing workouts when the list is empty."""
        with patch('tkinter.messagebox.showinfo') as mock_info:
            self.app.view_workouts()
            mock_info.assert_called_with("Workouts", "No workouts logged yet.")

    def test_view_workouts_with_data(self):
        """Test viewing workouts with a populated list."""
        self.app.workouts = [
            {"workout": "Pushups", "duration": 15},
            {"workout": "Stretching", "duration": 10}
        ]
        expected_message = "Logged Workouts:\n1. Pushups - 15 minutes\n2. Stretching - 10 minutes\n"
        with patch('tkinter.messagebox.showinfo') as mock_info:
            self.app.view_workouts()
            mock_info.assert_called_with("Workouts", expected_message)

if __name__ == '__main__':
    unittest.main()
