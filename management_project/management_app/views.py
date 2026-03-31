from django.shortcuts import render, redirect
from .form import userDataForm, bookDataForm

def addbook(request):
    if request.method == 'POST':
        form = bookDataForm(request.POST)
        print("Form Submited!")

        if form.is_valid():
            print("from is valid!")
        
            try:
                form.save()
                return redirect('books')
            except Exception as e:
                print(f"Database Error:{e}")
        else:
            print("ERROR!")
    else:
        form=bookDataForm()
    return render(request, 'addbook.html', {'form':form})