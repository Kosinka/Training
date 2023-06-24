# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

expenses_in_year = expenses
expenses_in_month = expenses
educational_grant_in_year = educational_grant * 10
for i in range(9):
    expenses_in_month *= 1.03
    expenses_in_year += expenses_in_month

print('Студенту надо попросить ', round(educational_grant_in_year - expenses_in_year) * -1, ' рублей.')
