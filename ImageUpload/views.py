from django.shortcuts import render, redirect
from .models import FoodImage

from static.util import image_predict
from static.util import Recommend
import pandas
from static.util.cal import *

# Create your views here.


def todayFood(request):

    dayNut = {
        'cal': 2435,
        'pro': 82,
        'fat': 54,
        'car': 380,
        'nat': 2000,
    }

    import datetime
    user = request.user
    currentDay = datetime.datetime.today()

    todayMeals = FoodImage.objects.filter(uploaded__date=currentDay)

    eatIdxList = []
    eatServingList = []

    for data in todayMeals.values():
        eatIdxList.append(data['imageIdx'])

    nut = get_total(eatIdxList)

    context = {
        'todayMeals': todayMeals,
        'nut': nut,
        'daynut': dayNut,
    }
    print(context['todayMeals'])
    return render(request, 'ImageUpload/todayFood.html', context)


def upload(request):
    # if(request.method == 'POST'):
    food = FoodImage()
    # food.pub_date = timezone.datetime.now() model func으로 대체
    food.user = request.user
    # # # Ai model

    food.photo = request.FILES['imgs']
    food.imageIdx = image_predict.image_predict(food.photo)
    print(request.POST['serving'], type(request.POST['serving']))
    food.serving = request.POST['serving']
    # food.imageIdx = 0  # ->   row index
    # # #
    food.save()
    # name 속성이 imgs인 input 태그로부터 받은 파일들을 반복문을 통해 하나씩 가져온다
    return redirect('ImageUpload:detail', food.id)
    # else:
    #     return render(request, 'new.html')


def detail(request, pk):
    food = FoodImage.objects.get(pk=pk)

    nut = get_nut(food.imageIdx)
    context = {
        'food': food,
        'nut': nut
    }
    return render(request, 'ImageUpload/FoodDetail.html', context)


def uploadForm(request):
    return render(request, 'ImageUpload/uploadForm.html')


def recommend(request):
    import datetime
    user = request.user
    currentDay = datetime.datetime.today()
    todayMeals = FoodImage.objects.filter(uploaded__date=currentDay).values()

    eatIdxList = []
    eatServingList = []

    for data in todayMeals:
        eatIdxList.append(data['imageIdx'])
        eatServingList.append(data['serving'])

    output = Recommend.recommend(eatIdxList, eatServingList)
    # label, price *3
    output2 = [(i, _, get_nut_haksik(i)) for i, _ in output]

    context = {
        'recommendMeals': output2
    }

    return render(request, 'ImageUpload/recommend.html', context)
