from django.shortcuts import render, redirect
from .models import FoodImage

from static.util.image_predict import image_predict
from static.util import Recommend
# Create your views here.


def todayFood(request):

    import datetime
    user = request.user
    currentDay = datetime.datetime.today()
    context = {
        'todayMeals': FoodImage.objects.filter(uploaded__date=currentDay)
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
    food.imageIdx = image_predict(food.photo)
    print(request.POST['serving'], type(request.POST['serving']))
    food.serving = request.POST['serving']
    # food.imageIdx = 0  # ->   row index
    # # #
    food.save()
    # name 속성이 imgs인 input 태그로부터 받은 파일들을 반복문을 통해 하나씩 가져온다
    return redirect('detail', food.id)
    # else:
    #     return render(request, 'new.html')


def detail(request, pk):
    context = {
        'food': FoodImage.objects.get(pk=pk)
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

    context = {
        'recommendMeals': output
    }

    return render(request, 'ImageUpload/recommend.html', context)
