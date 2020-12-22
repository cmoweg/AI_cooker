def recommend(today, eat, h=182, w=74, m=2):
    import pandas as pd
    ft = pd.read_excel('C:/dev/AI_Cooker/static/util/food_pre.xlsx')
    ht = pd.read_excel('C:/dev/AI_Cooker/static/util/haksik.xlsx')
    h = h
    w = w
    m = m
    hr = (h-100)*0.9
    if m == 1:
        cal_rec = 25 * hr
    elif m == 2:
        cal_rec = 33 * hr
    else:
        cal_rec = 40 * hr

    cal = 0
    pro = 0
    fat = 0
    car = 0
    nat = 0
    for i in range(len(today)):
        cal += ft.iloc[today[i], 1]*eat[i]  # 칼로리 calorie
        pro += ft.iloc[today[i], 2]*eat[i]  # 단백질 protein
        fat += ft.iloc[today[i], 3]*eat[i]  # 지방 fat
        car += ft.iloc[today[i], 4]*eat[i]  # 탄수화물 carbohydrate
        nat += ft.iloc[today[i], 5]*eat[i]  # 나트륨 natrium
        i += 1
    pro_rec = 0.135 * cal_rec / 4    # 단백질 권장 섭취량
    fat_rec = 0.200 * cal_rec / 9    # 지방 권장 섭취량
    car_rec = 0.625 * cal_rec / 4    # 탄수화물 권장 섭취량
    nat_rec = 2000                  # 나트륨 권장 섭취량, 단위 mg
    cal_lack = cal_rec - cal
    pro_lack = pro_rec - pro
    fat_lack = fat_rec - fat
    car_lack = car_rec - car
    nat_lack = nat_rec - nat
    for i in range(len(ht)):
        cal_rest, pro_rest, fat_rest, car_rest, nat_rest = 0, 0, 0, 0, 0
        cal_rest = abs(cal_lack - ht.iloc[i, 1])  # 남은 칼로리
        pro_rest = abs(pro_lack - ht.iloc[i, 2])  # 남은 단백질
        fat_rest = abs(fat_lack - ht.iloc[i, 3])  # 남은 지방
        car_rest = abs(car_lack - ht.iloc[i, 4])  # 남은 탄수화물
        nat_rest = abs(nat_lack - ht.iloc[i, 5])  # 남은 나트륨
        ht.loc[i, 'score'] = cal_rest + pro_rest+fat_rest+car_rest+nat_rest
    ht['rank_by_min'] = ht['score'].rank(method='min')
    # 종합지표 계산
    for i in range(len(ht)):
        cal_rest_per, pro_rest_per, fat_rest_per, car_rest_per, nat_rest_per = 0, 0, 0, 0, 0
        cal_rest_per = (cal_lack - ht.iloc[i, 1]) / cal_rec  # 남은 칼로리
        pro_rest_per = (pro_lack - ht.iloc[i, 2]) / pro_rec  # 남은 단백질
        fat_rest_per = (fat_lack - ht.iloc[i, 3]) / fat_rec  # 남은 지방
        car_rest_per = (car_lack - ht.iloc[i, 4]) / car_rec  # 남은 탄수화물
        nat_rest_per = (nat_lack - ht.iloc[i, 5]) / nat_rec  # 남은 나트륨
        ht.loc[i, 'com_indicater'] = abs(
            cal_rest_per + pro_rest_per + fat_rest_per + car_rest_per + nat_rest_per)
        ht.loc[i, 'test'] = abs(cal_rest_per) + abs(pro_rest_per) + \
            abs(fat_rest_per) + abs(car_rest_per) + abs(nat_rest_per)

    ht['com_indicater_min'] = ht['com_indicater'].rank(method='min')
    # 종합지표 계산
    ht_com = ht.sort_values(by='com_indicater_min')
    k = 0
    lis = []
    lis2 = []
    for i in range(len(today)):
        lis2.append(ft.iloc[today[i], 0])

    for i in range(len(ht)):
        if(ht.loc[[i], ['test']].values < ht['test'].quantile(0.25) and ht.iloc[i, 0] not in lis2):
            lis.append((i, int(ht.iloc[i, 6])))
            k = k + 1
        if(k > 2):
            break
    return(lis)
