class WorkoutTracker:
    """Handles the business logic for tracking workouts, independent of the UI."""

    def __init__(self):
        self.workouts = []

    def add_workout(self, workout, duration_str):
        """Validates and adds a workout. Returns a tuple (bool, str) for success and a message."""
        if not workout or not duration_str:
            return False, "Please enter both workout and duration."

        try:
            # Ensure duration is treated as a number for validation
            duration = int(duration_str)
            if duration <= 0:
                return False, "Duration must be a positive number."

            self.workouts.append({"workout": workout, "duration": duration})
            return True, f"'{workout}' added successfully!"
        except (ValueError, TypeError):
            return False, "Duration must be a valid number."

    def get_workouts(self):
        """Returns the list of workouts."""
        return self.workouts