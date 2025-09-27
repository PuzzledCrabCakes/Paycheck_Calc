print('')
print('-----------------------------------')
print('')
hours_worked_1 = float(input('How many hours did you work last week?\n'))
print('')
print('-----------------------------------')
print('')
hours_worked_2 = float(input('How many hours did you work this week?\n'))
print('')
print('-----------------------------------')
print('')
pay = float(input('How much do you get paid?\n'))
print('')
print('-----------------------------------')
print('')


def paycheck(hours_worked_1, hours_worked_2, pay):
    if hours_worked_1 <= 40:
        week_1 = (hours_worked_1 * pay)
    else:
        overtime = hours_worked_1 - 40
        overtime_wage = pay * 1.5
        week_1 = (40 * pay) + (overtime * overtime_wage)

    if hours_worked_2 <= 40:
        week_2 = (hours_worked_2 * pay)
    else:
        overtime = hours_worked_2 - 40
        overtime_wage = pay * 1.5
        week_2 = (40 * pay) + (overtime * overtime_wage)

    total = week_1 + week_2
    return round(total)

results = paycheck(hours_worked_1, hours_worked_2, pay)
print('')
print('-----------------------------------')
print('')
print(f'You should expect ${results} gross')
print('')
print('-----------------------------------')
