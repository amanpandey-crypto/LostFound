from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,HttpResponse,redirect
from .forms import SignUpForm, EditProfileForm
from .models import UserProfile, ItemData, LostItem
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            objt = UserProfile(user=user, UID=request.POST.get('UID'), branch=request.POST.get('Branch'),
                               year=request.POST.get('Year'), contactno=request.POST.get('ContactNo'), 
                               user_image=request.POST.get('user_image'), designation=request.POST.get('designation'))

            print(objt)

            objt.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('login')


def editprofile(request):

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        user_obj=UserProfile.objects.get(user=request.user)
        if form.is_valid():
            form.save()
            image=request.POST.get('user_image')
            desgn=request.POST.get('designation')
            user_obj.user_image=image
            user_obj.designation=desgn
            user_obj.save()
            return redirect('profile')
        else:
            print('not saved')
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/editprofile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            logout(request)
            return redirect('login')
        else:
            return redirect('accounts/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


def claim(request, id):
    item = ItemData.objects.get(pk=id)
    email = item.UserID.email
    first = item.UserID.first_name
    last = item.UserID.last_name
    username = item.UserID.username
    description = item.Description
    location = item.Location

    send_mail(
        'Trying to claim',
        f'Someone wants to claim the item(maybe owner) {request.user.email}',
        'lostfoundiiitdm@gmail.com',
        [email],
        fail_silently=False,
    )
    item.active = False
    messages.success(request, 'Mail has been sent to ' + username)
    item.save()
    return render(request, 'accounts/claim.html', {'email': email, 'first': first,
                                                   'last': last, 'username': username, 'description':description,
                                                    'location':location})


def found(request):
    item_data = ItemData.objects.filter(active=True)
    data = {
        'item_data': item_data
    }
    return render(request, 'accounts/found.html', context=data)


def requestItem(request):

    submitButton = request.POST.get('Submit')
    if submitButton == 'Submit':
        obj = ItemData(UserID=request.user, author=request.user.username,
                       Description=request.POST.get('Description'),
                       Location=request.POST.get('Location'),
                       item_image=request.POST.get('item_image'))
        obj.save()
        return redirect('found')
    return render(request, 'accounts/requestitem.html')


def lost(request):
    lost = LostItem.objects.filter(active=True)
    data = {
        'lost': lost
    }
    return render(request, 'accounts/lost.html', context=data)


def lostItem(request):

    submitButton = request.POST.get('Submit')
    if submitButton == 'Submit':
        obj = LostItem(UserID=request.user, author=request.user.username,
                       title=request.POST.get('title'), description=request.POST.get('Description'),
                       lost_image=request.POST.get('lost_image'))

        obj.save()
        return redirect('lost')
    return render(request, 'accounts/postitem.html')



def profile(request):
    obj = UserProfile.objects.get(user_id=request.user.id)
    args = {'UID': obj.UID, 'contactno': obj.contactno, 'branch': obj.branch, 'year': obj.year,
    'designation':obj.designation, 'image': obj.user_image}
    return render(request, 'accounts/profile.html', args)


def mail(request, id):
    obj = LostItem.objects.get(pk=id)
    email = obj.UserID.email
    first = obj.UserID.first_name
    last = obj.UserID.last_name
    username = obj.UserID.username
    description = obj.description
    obj.active=False
    
    send_mail(
        'Item found',
        f'the item has been found by {request.user.email}',
        'lostfoundiiitdm@gmail.com',
        [email],
        fail_silently=False,
    )
    obj.save()
    messages.success(request, 'Mail has been sent to ' + username)
    return render(request, 'accounts/postuser.html',{'email': email, 'first': first,
                                                     'last': last, 'username': username, 'description':description})


def resfound(request):
    item_data = ItemData.objects.filter(active=False)
    data = {
        'item_data': item_data
    }
    return render(request, 'accounts/resolvedfound.html', context=data)


def reslost(request):
    lost = LostItem.objects.filter(active=False)
    data = {
        'lost': lost
    }
    return render(request, 'accounts/resolvedlost.html', context=data)



def contact(request):
    if request.method=='POST':
        message_name=request.POST['message_name']
        message_email=request.POST['message_email']
        message=request.POST['message']
        
        send_mail(
            'Feedback from' +' ' + message_name,
            message,
            message_email,
            ['lostfoundiiitdm@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'accounts/home.html', {'message_name': message_name})
    else:
        return render(request, 'accounts/home.html')
