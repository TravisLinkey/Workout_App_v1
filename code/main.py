from __future__ import print_function
from service.calendar_service import Service

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    # Logs the user in
    service = Service()
    service.login()
    service.log_workout('Extra Special Workout')

if __name__ == '__main__':
    main()