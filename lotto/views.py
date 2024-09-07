from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    return render(request, 'lotto/default.html', {})
   


def hello(request):
        
        # data = GuessNumbers.objects.all()
        # data = GuessNumbers.objects.get(id=1)

        return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


 # user_input_name = request.POST['name']
    # user_input_text = request.POST['text']
    # new_row = GuessNumbers(name=user_input_name, text=user_input_text)
    # print(new_row.num_lotto)
    # print(new_row.name)
    # new_row.name = new_row.name.upper() # WIN THE PRIZE!
    # new_row.lottos = [ np.randint(1, 50) for i in range(6) ]
    # new_row.save() # db에 덮어씌우기
