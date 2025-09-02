import tkinter as tk
import unittest
from unittest.mock import patch, MagicMock

# Import application class
from ACEest_Fitness import FitnessTrackerApp

class TestFitnessTrackerApp(unittest.TestCase):
    def setUp(self):
        """Set up a mock environment for each test."""
        # Patch the Tk and Entry classes before the app is instantiated.
        self.patcher_tk = patch('tkinter.Tk')
        self.MockTk = self.patcher_tk.start()
        
        self.patcher_entry = patch('tkinter.Entry')
        self.MockEntry = self.patcher_entry.start()
        
        self.app = FitnessTrackerApp(self.MockTk())
        
        # Now, correctly set the return value on the mocked entry instances.
        self.app.workout_entry.get.return_value = "Running"
        self.app.duration_entry.get.return_value = "30"

    def tearDown(self):
        """Stop the patches after each test."""
        self.patcher_tk.stop()
        self.patcher_entry.stop()

    @patch('tkinter.messagebox.showinfo')
    def test_add_workout_success(self, mock_info):
        """Test adding a workout with valid input."""
        # The return values are set in setUp, so we just call the method.
        self.app.add_workout()

        self.assertEqual(len(self.app.workouts), 1)
        self.assertEqual(self.app.workouts[0]["workout"], "Running")
        self.assertEqual(self.app.workouts[0]["duration"], 30)
        
        mock_info.assert_called_with("Success", "'Running' added successfully!")
        self.app.workout_entry.delete.assert_called_with(0, tk.END)
        self.app.duration_entry.delete.assert_called_with(0, tk.END)

    @patch('tkinter.messagebox.showerror')
    def test_add_workout_missing_input(self, mock_error):
        """Test adding a workout with missing input."""
        # Override the mock return value for this specific test.
        self.app.workout_entry.get.return_value = ""

        self.app.add_workout()

        self.assertEqual(len(self.app.workouts), 0)
        mock_error.assert_called_with("Error", "Please enter both workout and duration.")
        
    @patch('tkinter.messagebox.showerror')
    def test_add_workout_invalid_duration(self, mock_error):
        """Test adding a workout with a non-numeric duration."""
        # Override the mock return value for this specific test.
        self.app.duration_entry.get.return_value = "thirty"

        self.app.add_workout()
        self.assertEqual(len(self.app.workouts), 0)
        mock_error.assert_called_with("Error", "Duration must be a number.")

    @patch('tkinter.messagebox.showinfo')
    def test_view_workouts_empty(self, mock_info):
        """Test viewing workouts when the list is empty."""
        self.app.view_workouts()
        mock_info.assert_called_with("Workouts", "No workouts logged yet.")

    @patch('tkinter.messagebox.showinfo')
    def test_view_workouts_with_data(self, mock_info):
        """Test viewing workouts when the list contains data."""
        self.app.workouts.append({"workout": "Running", "duration": 30})
        self.app.workouts.append({"workout": "Lifting", "duration": 45})

        self.app.view_workouts()
        expected_message = "Logged Workouts:\n1. Running - 30 minutes\n2. Lifting - 45 minutes\n"
        mock_info.assert_called_with("Workouts", expected_message)

if __name__ == '__main__':
    unittest.main()
