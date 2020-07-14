from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from mainApp.models import Account, Article, Comments, ArticleAccountLiked
from django.http import QueryDict
import json

# Create your views here.

#method used to check login - decorator method
def loggedin(f):
    def test(request):
        if 'username' in request.session:
            return f(request)
        else:   
            return HttpResponse("Not Logged in")
    return test

#loads home page
def index(request):
    if 'username' in request.session:
        u = request.session['username']
        account = Account.objects.get(pk=u)        
        context = {
            'username': u,
            'loggedin': True
        }
        return render(request, 'mainApp/index.html', context)
    else:
        return render(request, 'mainApp/index.html')

#loads sign up page
def signup(request):
    return render(request, 'mainApp/signup.html')

#when signing up user, add account infointo database
def addUser(request):
    if request.method == 'POST':
        data = QueryDict(request.body)
        e = request.POST['email']
        f = request.POST['fName']
        l = request.POST['lName']
        pN = request.POST['phoneNum']
        p = request.POST['password']
        account = Account(email=e, password=p, firstName=f, lastName=l, phoneNum=pN)
        account.save()
        return render(request, 'mainApp/index.html')

#return sign in page
def signin(request):
    return render(request, 'mainApp/signin.html')
"""
def login(request):
    if request.method == 'POST':
        data = QueryDict(request.body)
        u = request.POST['username']
        p = request.POST['password']
        try:
            account = Account.objects.get(pk=u)
        except Account.DoesNotExist:
            return HttpResponse("<span class='taken'>&nbsp;&#x2718; Unknown username</span>")
        if p == account.password:
            request.session['username'] = u;
            request.session['password'] = p;
            #return HttpResponse("<span class='available'>&nbsp;&#x2714; Valid </span>")
            return render(request, 'mainApp/index.html', {
                'username': u,
                'loggedin': True}
            )
        else:
            return HttpResponse("<span class='taken'>&nbsp;&#x2718; Wrong Password</span>")
"""
#when logging in, takes in username and password and cross references with database 
def login(request):
    u = request.POST['username']#passes username from user
    p = request.POST['password']#passes password from user
    try:
        account = Account.objects.get(pk=u)#checks if username is in database
    except Account.DoesNotExist:
        return HttpResponse("User does not exist Page")#if not reutrns user does not exist page
    if p == account.password:
        request.session['username'] = u;#checks password with username to give user access to their website account
        request.session['password'] = p;
        context = {
            'username': u,#passes username as variable to html page
            'loggedin': True #passes boolean to check if page is already logged in
        }
        return render(request, 'mainApp/index.html', context)
    else:
        return HttpResponse("Wrong password Page")

#can only call method if loggedin
@loggedin
def edit(request):
    u = request.session['username']
    account = Account.objects.get(pk=u)
    return render(request, 'mainApp/editprofile.html',{
        'username': u,
        'loggedin': True}
    )
#can only call if loggedin (calls decorator method first)
@loggedin
def editProfile(request):#updates user information in database
    if request.method == 'PUT':
        if 'username' in request.session:
            e = request.session['username']#get data from html
            data = QueryDict(request.body)#get data from Ajax
            uf = data.get('fName')#get variable fName from ajax file
            ul = data.get('lName')#same fro below
            upN = data.get('phoneNum')
            up = data.get('password')
            
            instance = Account.objects.get(pk=e)#get variable with pk = e (with the same email)
            instance.firstName = uf
            instance.lastName = ul
            instance.phoneNum = upN
            instance.password = up #update database attributes
            instance.save()
            return HttpResponse("Good job")

#load sports page
def sports(request):
    if 'username' in request.session:#if logged in do these methods 
        if 'erase' in request.GET:
            c = request.GET['erase']#get value of erase from html and store in c
            Comments.objects.get(pk=c).delete()#delete object with from comment with id passed from html
        if 'like' in request.GET:
            str = request.GET['like']#get values from str
            mylist = str.split(',')#split str into 2 strings as it passes article id and username id
            art = Article.objects.get(pk=mylist[0])#article id
            acc = Account.objects.get(pk=mylist[1])#username id
            try:
                liked = ArticleAccountLiked.objects.get(article=art,user=acc)
                n = liked.id#try method to check if ArticleAccountLiked exists, catch if it doesn't
                ArticleAccountLiked.objects.get(pk=n).delete()
                art.likes = art.likes - 1#if exists -1 to likes (dislike)
                art.save()
            except ArticleAccountLiked.DoesNotExist:
                art.likes = art.likes + 1#if does not exist + 1 to likes (like)
                art.save()
                AAL = ArticleAccountLiked(article=art, user=acc)
                AAL.save()#only exists if user preiously liked article
        u = request.session['username']
        account = Account.objects.get(pk=u)#get info to pass to html page
        comments = Comments.objects.all()
        articles = Article.objects.all()
        AAL = ArticleAccountLiked.objects.all()
        context = {
            'username': u,#pass username
            'loggedin': True,#pass loggedin boolean
            'comments':comments,#all comments fro db
            'articles':articles,#all articles from db
            'AAL':AAL#articles to likes db info
        }
        return render(request, 'mainApp/sports.html', context)
    else:#if not logged in, do notreturn context, just return page
        return render(request, 'mainApp/sports.html')

#load business page, same theory as sports
def business(request):
    if 'username' in request.session:
        if 'erase' in request.GET:
            c = request.GET['erase']
            Comments.objects.get(pk=c).delete()
        if 'like' in request.GET:
            str = request.GET['like']
            mylist = str.split(',')
            art = Article.objects.get(pk=mylist[0])
            acc = Account.objects.get(pk=mylist[1])
            try:
                liked = ArticleAccountLiked.objects.get(article=art,user=acc)
                n = liked.id
                ArticleAccountLiked.objects.get(pk=n).delete()
                art.likes = art.likes - 1
                art.save()
            except ArticleAccountLiked.DoesNotExist:
                art.likes = art.likes + 1
                art.save()
                AAL = ArticleAccountLiked(article=art, user=acc)
                AAL.save()
        u = request.session['username']
        account = Account.objects.get(pk=u)
        comments = Comments.objects.all()
        articles = Article.objects.all()
        AAL = ArticleAccountLiked.objects.all()
        context = {
            'username': u,
            'loggedin': True,
            'comments':comments,
            'articles':articles,
            'AAL':AAL
        }
        return render(request, 'mainApp/business.html', context)
    else:
        return render(request, 'mainApp/business.html')

#load technology page, same theory as sports
def technology(request):
    if 'username' in request.session:
        if 'erase' in request.GET:
            c = request.GET['erase']
            Comments.objects.get(pk=c).delete()
        if 'like' in request.GET:
            str = request.GET['like']
            mylist = str.split(',')
            art = Article.objects.get(pk=mylist[0])
            acc = Account.objects.get(pk=mylist[1])
            try:
                liked = ArticleAccountLiked.objects.get(article=art,user=acc)
                n = liked.id
                ArticleAccountLiked.objects.get(pk=n).delete()
                art.likes = art.likes - 1
                art.save()
            except ArticleAccountLiked.DoesNotExist:
                art.likes = art.likes + 1
                art.save()
                AAL = ArticleAccountLiked(article=art, user=acc)
                AAL.save()
        u = request.session['username']
        account = Account.objects.get(pk=u)
        comments = Comments.objects.all()
        articles = Article.objects.all()
        AAL = ArticleAccountLiked.objects.all()
        context = {
            'username': u,
            'loggedin': True,
            'comments':comments,
            'articles':articles,
            'AAL':AAL
        }
        return render(request, 'mainApp/technology.html', context)
    else:
        return render(request, 'mainApp/technology.html')

#load science page, same theory as sports
def science(request):
    if 'username' in request.session:
        if 'erase' in request.GET:
            c = request.GET['erase']
            Comments.objects.get(pk=c).delete()
        if 'like' in request.GET:
            str = request.GET['like']
            mylist = str.split(',')
            art = Article.objects.get(pk=mylist[0])
            acc = Account.objects.get(pk=mylist[1])
            try:
                liked = ArticleAccountLiked.objects.get(article=art,user=acc)
                n = liked.id
                ArticleAccountLiked.objects.get(pk=n).delete()
                art.likes = art.likes - 1
                art.save()
            except ArticleAccountLiked.DoesNotExist:
                art.likes = art.likes + 1
                art.save()
                AAL = ArticleAccountLiked(article=art, user=acc)
                AAL.save()
        u = request.session['username']
        account = Account.objects.get(pk=u)
        comments = Comments.objects.all()
        articles = Article.objects.all()
        AAL = ArticleAccountLiked.objects.all()
        context = {
            'username': u,
            'loggedin': True,
            'comments':comments,
            'articles':articles,
            'AAL':AAL
        }
        return render(request, 'mainApp/science.html', context)
    else:
        return render(request, 'mainApp/science.html')

#load travel page, same theory as sports
def travel(request):
    if 'username' in request.session:
        if 'erase' in request.GET:
            c = request.GET['erase']
            Comments.objects.get(pk=c).delete()
        if 'like' in request.GET:
            str = request.GET['like']
            mylist = str.split(',')
            art = Article.objects.get(pk=mylist[0])
            acc = Account.objects.get(pk=mylist[1])
            try:
                liked = ArticleAccountLiked.objects.get(article=art,user=acc)
                n = liked.id
                ArticleAccountLiked.objects.get(pk=n).delete()
                art.likes = art.likes - 1
                art.save()
            except ArticleAccountLiked.DoesNotExist:
                art.likes = art.likes + 1
                art.save()
                AAL = ArticleAccountLiked(article=art, user=acc)
                AAL.save()
        u = request.session['username']
        account = Account.objects.get(pk=u)
        comments = Comments.objects.all()
        articles = Article.objects.all()
        AAL = ArticleAccountLiked.objects.all()
        context = {
            'username': u,
            'loggedin': True,
            'comments':comments,
            'articles':articles,
            'AAL':AAL
        }
        return render(request, 'mainApp/travel.html', context)
    else:
        return render(request, 'mainApp/travel.html')

#add comment using ajax
def addComment(request):
    if request.method == 'POST':
        data = QueryDict(request.body)#gets data fro ajax file
        e = request.session['username']#gets ajax data with variable name username and stores in e
        u = Account.objects.get(pk=e)#gets account object with username taken from webpage using ajax
        c = request.POST['comment']#get comment text
        art = request.POST['article']#get article id
        a = Article.objects.get(pk=art)#get article ojecy with artilce id taken from webpage using ajax
        comment = Comments(user=u, article=a, time=timezone.now(), text=c)#create new comment instance 
        comment.save()#save new comment instance
        context = {
            'username': u,
            'loggedin': True
        }
        return render(request, 'mainApp/index.html', context)

def logCheckUser(request):
    if 'username' in request.POST:
        u = request.POST['username']
        try:#checks if username exists in databse, if not throws exception and...
            account = Account.objects.get(pk=u)
            return HttpResponse("<span class='available'>&nbsp;&#x2714; Valid username</span>")#prompts user username exists in database
        except Account.DoesNotExist:
            return HttpResponse("<span class='taken'>&nbsp;&#x2718; Unknown username</span>")#prompts user this username does not exist
    else:
        return HttpResponse("")

#method to log out user, only occurs if user is logged in 
@loggedin
def logout(request):
    if 'username' in request.session:
        u = request.session['username']#checks if username is stroed in html, if not, user is not logged in (as username is always passed to every new page when logged in)
        request.session.flush()        
        return render(request, 'mainApp/index.html')
    else:
        raise HttpResponse("Can't logout, you are not logged in")
