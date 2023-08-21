from app.models.tasks import TaskWeekday
from datetime import datetime


def attribute_from_taksweekday_about_current_day():

    current_day = datetime.now().strftime('%A').lower()

    match current_day:
        case 'sunday':
            return TaskWeekday.sunday
        case 'monday':
            return TaskWeekday.monday
        case 'tuesday':
            return TaskWeekday.tuesday
        case 'wednesday':
            return TaskWeekday.wednesday
        case 'thursday':
            return TaskWeekday.thursday
        case 'friday':
            return TaskWeekday.friday
        case 'saturday':
            return TaskWeekday.saturday
