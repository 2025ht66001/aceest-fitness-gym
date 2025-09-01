from prog1 import FitnessTrackerApp

import tkinter as tk
import unittest
from unittest.mock import patch
from your_app_file import FitnessTrackerApp # Assuming the class is in a file named your_app_file.py

class TestFitnessTrackerApp(unittest.TestCase):
    def setUp(self):
        """Set up a new Tkinter root and app instance for each test."""
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window for testing
        self.app = FitnessTrackerApp(self.root)

    def tearDown(self):
        """Destroy the Tkinter root after each test."""
        self.root.destroy()

    def test_add_workout_success(self):
        """Test adding a workout with valid input."""
        # Set values in the entry widgets
        self.app.workout_entry.insert(0, "Running")
        self.app.duration_entry.insert(0, "30")

        # Mock the messagebox.showinfo call to prevent it from popping up
        with patch('tkinter.messagebox.showinfo') as mock_info:
            self.app.add_workout()
            # Assert that the workout was added to the list
            self.assertEqual(len(self.app.workouts), 1)
            self.assertEqual(self.app.workouts[0]["workout"], "Running")
            self.assertEqual(self.app.workouts[0]["duration"], 30)

            # Assert that the success message was shown
            mock_info.assert_called_with("Success", "'Running' added successfully!")

            # Assert that the entry fields were cleared
            self.assertEqual(self.app.workout_entry.get(), "")
            self.assertEqual(self.app.duration_entry.get(), "")


if __name__ == '__main__':
    unittest.main()
