from django.shortcuts import render, redirect
from .models import FoodImage
# Create your views here.


def todayFood(request):
    return render(request, 'ImageUpload/todayFood.html', {})


def upload(request):
    # if(request.method == 'POST'):
    food = FoodImage()
    # food.pub_date = timezone.datetime.now() model func으로 대체
    food.user = request.user
    # # # Ai model
    food.photo = request.FILES['imgs']
    food.imageIdx = 0
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
