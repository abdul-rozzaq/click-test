from django.http import HttpResponse


def home_page(request):
    print("Salom dunyooooooooooooo")
    return HttpResponse("It Worrrrrrks")
