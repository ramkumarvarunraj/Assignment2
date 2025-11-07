from flask import Flask, request, jsonify
from workout_tracker import WorkoutTracker

# Initialize the Flask app and the workout tracker
app = Flask(__name__)
tracker = WorkoutTracker()

@app.route('/')
def index():
    """A simple welcome message for the root URL."""
    return "Welcome to the ACEestFitness API!"

@app.route('/workouts', methods=['GET'])
def get_workouts():
    """Returns the list of all logged workouts."""
    return jsonify(tracker.get_workouts())

@app.route('/workouts', methods=['POST'])
def add_workout():
    """Adds a new workout. Expects a JSON payload with 'workout' and 'duration'."""
    data = request.get_json()
    workout = data.get('workout')
    duration = data.get('duration')

    success, message = tracker.add_workout(workout, str(duration))

    if success:
        return jsonify({"message": message}), 201
    else:
        return jsonify({"error": message}), 400

if __name__ == '__main__':
    # Run the app on all available network interfaces, port 8080
    app.run(host='0.0.0.0', port=8080)