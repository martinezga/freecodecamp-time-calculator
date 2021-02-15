def add_time(start_time, duration, start_day=None):
    initial_values = {'start time': ['', '', ''],
                      'time to add': ['', ''],
                      'start day': '',
                     }
    final_values =   {'final time': ['', '', ''],
                      'final day': '',
                      'num days later': 0,
                      'flag': False
                      }
    hours_from_minutes = 0
    days = 0
    days_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    initial_values['start time'] = split_time(start_time)
    initial_values['time to add'] = split_time(duration)
    if start_day is not None:
        initial_values['start day'] = start_day[0].upper() + start_day[1:].lower()

    # Calculate minutes
    sum_minutes = int(initial_values['start time'][1]) + int(initial_values['time to add'][1])
    if sum_minutes >= 60:
        real_minutes = sum_minutes % 60
        hours_from_minutes = sum_minutes // 60
        final_values['final time'][1] = format_num(real_minutes)
    else:
        final_values['final time'][1] = format_num(sum_minutes)

    # Calculate hours
    sum_hours = int(initial_values['start time'][0]) + int(initial_values['time to add'][0]) + hours_from_minutes       
    if sum_hours >= 12:
        real_hours = sum_hours % 12
        if real_hours == 0:
            final_values['final time'][0] = format_num(12)
        else:
            final_values['final time'][0] = str(real_hours)
    else:
        final_values['final time'][0] = str(sum_hours)

    # Calculate time period
    half_days = sum_hours // 12
    if half_days % 2 == 0:
        if initial_values['start time'][2] == 'AM':
            final_values['final time'][2] = 'AM'
        else:
            final_values['final time'][2] = 'PM'
    else:
        if initial_values['start time'][2] == 'AM':
            final_values['final time'][2] = 'PM'
        else:
            final_values['final time'][2] = 'AM'

    # Calculate days
    days = round(sum_hours / 24)
    if initial_values['start time'][2] == 'AM' and half_days <= 1:
        final_values['final day'] = initial_values['start day']
    elif initial_values['start time'][2] == 'PM' and half_days == 0:
        final_values['final day'] = initial_values['start day']
    elif initial_values['start time'][2] == 'PM' and half_days == 1:
        final_values['final day'] = get_final_day(initial_values['start day'], half_days, days_week)
        final_values['num days later'] = '(next day)'
        final_values['flag'] = True
    elif initial_values['start time'][2] == 'AM' and half_days > 1:
        final_values['num days later'] = '(' + str(days) + ' days later)'
        final_values['flag'] = True
    elif initial_values['start time'][2] == 'PM' and half_days > 1:
        final_values['final day'] = get_final_day(initial_values['start day'], days, days_week)
        final_values['num days later'] = '(' + str(days) + ' days later)'
        final_values['flag'] = True
    else:
        print('error')
    
    # Format output
    new_time = f"{final_values['final time'][0]}:{final_values['final time'][1]} {final_values['final time'][2]}"
    if start_day is not None and final_values['flag'] == True:
        print(new_time + ',' , final_values['final day'], final_values['num days later'])
    elif start_day is None and final_values['flag'] == True:
        print(new_time + ',', final_values['num days later'])
    else:
        print(new_time)
    return new_time

def split_time(time):
    final_time = []
    first_split = time.split(' ')
    if len(first_split) > 1:
        second_split = first_split[0].split(':')
        for item in second_split:
            final_time.append(item)
        final_time.append(first_split[1])
    else:
        second_split = time.split(':')
        for item in second_split:
            final_time.append(item)
    return final_time

def format_num(number):
    if number < 10:
        new_num = '0' + str(number)
    else:
        new_num = str(number)
    return new_num

def get_final_day(start_day, half_days, days_week):
    for i in range(len(days_week)):
        if start_day == days_week[i]:
            aux = (i + half_days) % len(days_week)
            return days_week[aux]

add_time("11:30 AM", "2:32", "Monday")
