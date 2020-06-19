from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Page
from facebook.models import Comment

# Create your views here.

def play(request):
    return render(request, 'play.html')

count = 0
def play2(request):
    shin = '신정훈'
    age = 30
    global count # 바깥영역의 변수 사용
    count = count + 1 # 접속할 때마다 1증가

    if age > 19:
        status = '성인'
    else:
        status = '비성인'

    diary = ['오늘은 날씨가 맑았다. - 4월 3일', '미세머지가 너무 심하다. (4월 2일)', '비가 온다. 4월 1일에 작성']

    return render(request, 'play2.html', { 'name': shin, 'diary': diary, 'cnt': count, 'age': status })

def my_profile(request):
    return render(request, 'profile.html')


def event(request):
    shin = '신정훈'
    age = 30
    global count  # 바깥영역의 변수 사용
    count = count + 1  # 접속할 때마다 1증가

    if age > 19:
        status = '성인'
    else:
        status = '비성인'

    if count is 7:
        lottery = '당첨!'
    else:
        lottery = '꽝...'

    return render(request, 'event.html',
                  {'name': shin, 'cnt': count, 'age': status, 'lottery': lottery})

def myFail(request):
    message = '비정상적인 접근입니다.'
    return render(request, 'fail.html', { 'message': message })

def myHelp(request):
    message = '무엇을 도와드릴까요?'
    return render(request, 'help.html', { 'message': message })

def myWarn(request):
    message = '다시 확인해주세요.'
    return render(request, 'warn.html', { 'message': message })

def newsFeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles': articles})

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['nickname'] != '' and request.POST['reply'] != '' and request.POST['password'] != '':
            Comment.objects.create(
                article=article,
                author=request.POST['nickname'],
                text=request.POST['reply'],
                password=request.POST['password']
            )

            return redirect(f'/feed/{ article.pk }')

    return render(request, 'detail_feed.html', {'feed': article})

def remove_comment(request, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == comment.password:
            comment.delete()
            return redirect('/')
        else:
            return redirect('/fail/')

    return render(request, 'remove_comment.html', { 'comment': comment })

def pages(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html', { 'pages': pages })

def new_page(request):
    if request.method == 'POST':
        new_page = Page.objects.create(
            master=request.POST['master'],
            name=request.POST['name'],
            text=request.POST['text'],
            category=request.POST['category']
        )
        # 새 페이지 개설 완료
        return redirect('/pages/')

    return render(request, 'new_page.html')

def remove_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.delete()
        return redirect('/pages/')

    return render(request, 'remove_page.html', { 'page': page })

def edit_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.master = request.POST['master']
        page.name = request.POST['name']
        page.category = request.POST['category']
        page.text = request.POST['text']
        page.save()
        return redirect('/pages/')

    return render(request, 'edit_page.html', { 'page': page })

def new_feed(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 코드 실행
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            text = request.POST['content']
            text = text + ' - 추신: 감사합니다.'

            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=text,
                password=request.POST['password']
            )
            return redirect(f'/feed/{ new_article.pk }')

    return render(request, 'new_feed.html')

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/')
        else:
            return redirect('/fail/')

    return render(request, 'remove_feed.html', { 'feed': article })

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{article.pk}')
        else:
            return redirect('/fail/')

    return render(request, 'edit_feed.html', {'feed': article})
