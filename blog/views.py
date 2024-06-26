from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
from .forms import CategoryForm , ArticleForm
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article,Category  # Import your Article model

def blog(request):
    # Query all articles from your database
      # Query all articles from your database
    articles_list = Article.objects.all()
    categories =Category .objects.all()
    # Configure pagination for three articles per page
    page = request.GET.get('page')
    paginator = Paginator(articles_list, 3)  # Show 3 articles per page

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results
        articles = paginator.page(paginator.num_pages)

    context = {
        'articles': articles,
        'categories':categories,
    }

    return render(request, 'blog/index.html', context)


def blog_details(request, article_id):
    # Retrieve the specific article by its ID
    article = get_object_or_404(Article, pk=article_id)
    categories =Category .objects.all()
    context = {
        'article': article,
        'categories':categories,
    }

    return render(request, 'blog/blog_details.html', context)

def search_articles(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles, 'query': query})

def category_articles(request, category_id):
    categories =Category .objects.all()
    category = Category.objects.get(pk=category_id)
    articles = Article.objects.filter(category=category)
    page = request.GET.get('page')
    paginator = Paginator(articles, 3)  # Show 3 articles per page

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results
        articles = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'category': category, 'categories':categories, 'articles': articles})



def editor(request):
    if request.method == 'POST':
        if 'category_form' in request.POST:
            # Process the category form
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
        elif 'article_form' in request.POST:
            # Process the article form
            article_form = ArticleForm(request.POST, request.FILES)
            if article_form.is_valid():
                article_form.save()
        # Redirect to the editor page after submitting the form
        return redirect('editor')
    else:
        category_form = CategoryForm()
        article_form = ArticleForm()
    
    categories = Category.objects.all()
    context = {'categories': categories, 'category_form': category_form, 'article_form': article_form}
    
    return render(request, 'blog/editor.html', context)
