from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Sentence, SentenceForm
from django.contrib.auth.models import User, auth

def index(request):
    sentences = Sentence.objects.all()
    return render(request, 'index.html', {'sentences': sentences})
#For table

def save_rating(request):
    if request.method == 'POST':
        sno = request.POST.get('sno')
        rating = request.POST.get('rating')
        # Update rating in the database
        sentence = Sentence.objects.get(sno=sno)
        sentence.rating = rating
        sentence.save()
        return HttpResponseRedirect('/')  # Redirect to the index page after saving rating
#for saving each rating

def sort_table(request):
    column = request.GET.get('column')
    order = request.GET.get('order')
    if column in ['SNO', 'SOURCE', 'TARGET', 'RATING'] and order in ['asc', 'desc']:
        if column == 'RATING':
            sentences = Sentence.objects.all().values
            print(sentences)
            sentences = sentences.order_by(('' if order == 'asc' else '-') + 'rating')
        else:
            sentences = Sentence.objects.all().order_by(('' if order == 'asc' else '-') + column.lower() + ('' if column in ['SOURCE', 'TARGET'] else '_asc'))
        return render(request, 'index.html', {'sentences': sentences})
    else:
        # Handle invalid sorting request
        return HttpResponseRedirect('/')

def add_sentence(request):
    form = SentenceForm()
    if request.method == 'POST':
        form = SentenceForm(request.POST)
        if form.is_valid():
            # Get the last loaded sentence
            last_sentence = Sentence.objects.last()
            sno = last_sentence.sno + 1 if last_sentence else 1  # Calculate sno for the new sentence
            form.instance.sno = sno  # Assign the calculated sno to the form instance
            form.save()  # Save the form
            return redirect('/')  # Redirect to the index page
    return render(request, 'add_sentence.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Your other views...

def signupfunction(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error': 'Username already exists'})

            # Create user if username is unique and passwords match
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            return redirect('/loginpage/')  # Redirect to login page
        else:
            # Handle password mismatch error
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

    # If request method is not POST, render the signup form
    return render(request, 'signup.html')

def loginfunction(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')  # Redirect to index page after successful login
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    # If request method is not POST, render the login form
    return render(request, 'login.html')


# admin user:
# username: adminuser
# password: adminuser
# email: adminuser@gmail.com
