from django.shortcuts import render
 
def test(request):
    context = {}
    context['a'] = 'apple'
    return render(request, 'test.html', context)