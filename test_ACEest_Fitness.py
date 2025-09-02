import tkinter as tk
import unittest
from unittest.mock import patch, MagicMock

# Import application class
from ACEest_Fitness import FitnessTrackerApp

class TestFitnessTrackerApp(unittest.TestCase):
    def setUp(self):
        """Set up a new Tkinter root and app instance for each test."""
        # Mock the entire tkinter module to prevent it from creating a GUI window.
        # The mock will simulate the behavior of tk.Tk() without needing a display.
        self.root = MagicMock()
        self.app = FitnessTrackerApp(self.root)

    def tearDown(self):
        """No need to destroy the root as it's a mock."""
        pass

    @patch('tkinter.messagebox.showinfo')
    def test_add_workout_success(self, mock_info):
        """Test adding a workout with valid input."""
        self.app.workout_entry.insert(0, "Running")
        self.app.duration_entry.insert(0, "30")

        self.app.add_workout()

        self.assertEqual(len(self.app.workouts), 1)
        self.assertEqual(self.app.workouts[0]["workout"], "Running")
        self.assertEqual(self.app.workouts[0]["duration"], 30)

        mock_info.assert_called_with("Success", "'Running' added successfully!")
        self.assertEqual(self.app.workout_entry.get(), "")
        self.assertEqual(self.app.duration_entry.get(), "")

    @patch('tkinter.messagebox.showerror')
    def test_add_workout_missing_input(self, mock_error):
        """Test adding a workout with missing input."""
        self.app.workout_entry.insert(0, "Running")

        self.app.add_workout()

        self.assertEqual(len(self.app.workouts), 0)
        mock_error.assert_called_with("Error", "Please enter both workout and duration.")

    @patch('tkinter.messagebox.showerror')
    def test_add_workout_invalid_duration(self, mock_error):
        """Test adding a workout with a non-numeric duration."""
        self.app.workout_entry.insert(0, "Running")
        self.app.duration_entry.insert(0, "thirty")

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
