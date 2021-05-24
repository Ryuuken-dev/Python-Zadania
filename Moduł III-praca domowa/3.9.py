"""
Przygotuj funkcję, która odbierze od użytkownika procent zdobytych punktów, a w odpowiedzi
zwróci ocenę jaką otrzymał użytkownik.
"""
users_points = int(input('Podaj liczbę zdobytych punktów (%): '))


def rating_from_points(points: int) -> list:
    rating_1 = 'niedostateczny' if points < 45 else 0
    rating_2 = 'dopuszczający' if 45 <= points < 55 else 0
    rating_3 = 'dostateczny' if 55 <= points < 80 else 0
    rating_4 = 'dobry' if 80 <= points < 90 else 0
    rating_5 = 'bardzo dobry' if 90 <= points < 95 else 0
    rating_6 = 'celujący' if 95 <= points <= 100 else 0
    rating_list = [rating_1, rating_2, rating_3, rating_4, rating_5, rating_6]
    return [rating for rating in rating_list if rating != 0]


print(rating_from_points(users_points))




