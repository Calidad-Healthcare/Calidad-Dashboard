from django.shortcuts import render, redirect

def main(request):
    if request.user.is_authenticated:
        return render(request,'board/index.html')
    else:
        return redirect('login/')