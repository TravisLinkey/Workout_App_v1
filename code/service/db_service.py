from flask_restful import Resource, Api

class Workout(Resource):
    workouts = []

    def get(self, name):
        for workout in self.workouts:
            if workout['name'] == name:
                return workout
        return {'message': "Workout with name '{}' does not exist".format(name)}, 404   # NOT FOUND

    def post(self, name):
        workout = {'name': name,
                   'exercises': [
                       ('Squat', 5, 5),
                       ('Bench_Press', 5, 5),
                       ('Barbell_Row', 5, 5),
                       ('Cardio', 15)
                   ]
        }
        self.workouts.append(workout)
        return workout, 201     # CREATED

class User(Resource):
    users = []

    def get(self):
        return {'users': self.users}
