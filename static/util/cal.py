def get_neut(idx):
    import pandas
    ft = pandas.read_excel('C:/dev/AI_Cooker/static/util/food_pre.xlsx')
    cal = ft.iloc[idx, 1]  # 칼로리 calorie
    pro = ft.iloc[idx, 2]  # 단백질 protein
    fat = ft.iloc[idx, 3]  # 지방 fat
    car = ft.iloc[idx, 4]  # 탄수화물 carbohydrate
    nat = ft.iloc[idx, 5]  # 나트륨 natrium
    return {'cal': cal, 'pro': pro, 'fat': fat, 'car': car, 'nat': nat}


def get_name_haksik(idx):
    import pandas
    ft = pandas.read_excel('C:/dev/AI_Cooker/static/util/haksik.xlsx')
    name = ft.iloc[idx, 0]  # 나트륨 natrium
    return name


def get_name_meal(idx):
    import pandas
    ft = pandas.read_excel('C:/dev/AI_Cooker/static/util/food_pre.xlsx')
    name = ft.iloc[idx, 0]  # 나트륨 natrium
    return name


def get_total(lst):
    import pandas
    ft = pandas.read_excel('C:/dev/AI_Cooker/static/util/food_pre.xlsx')
    cal, pro, fat, car, nat = 0, 0, 0, 0, 0
    for meal in lst:
        cal += ft.iloc[meal, 1]  # 칼로리 calorie
        pro += ft.iloc[meal, 2]  # 단백질 protein
        fat += ft.iloc[meal, 3]  # 지방 fat
        car += ft.iloc[meal, 4]  # 탄수화물 carbohydrate
        nat += ft.iloc[meal, 5]  # 나트륨 natrium
    return {'cal': cal, 'pro': pro, 'fat': fat, 'car': car, 'nat': nat}
