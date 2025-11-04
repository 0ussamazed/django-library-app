from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.db.models import Count, Q
from django.utils.dateparse import parse_date
# Create your views here.
def clients_info(request):
    query = request.GET.get('q')  # اسم العميل
    date_query = request.GET.get('date')  # التاريخ

    books = Book.objects.exclude(status='availble')

    if query:
        books = books.filter(Q(client_name__icontains=query))

    if date_query:
        try:
            parsed_date = parse_date(date_query)
            if parsed_date:
                books = books.filter(created_at__date=parsed_date)
        except:
            pass

    books = books.order_by('-created_at')
    return render(request, 'pages/clients_info.html', {
        'books': books,
        'query': query or '',
        'date_query': date_query or '',
    })





def best_selling_days(request):
    # أفضل الأيام
    days = (
        Book.objects.filter(status__in=['sold', 'rental'])
        .annotate(day=TruncDate('created_at'))
        .values('day')
        .annotate(total=Count('id'))
        .order_by('-total')[:10]
    )

    # ✅ جميع التصنيفات (مرتبة من الأكثر إلى الأقل طلباً)
    all_categories = (
        Category.objects.annotate(
            total=Count('book', filter=Q(book__status__in=['sold', 'rental']))
        )
        .order_by('-total')
    )

    # ✅ أعلى 5 كتب طلباً (مرتبين تنازلياً)
    top_books = (
        Book.objects.filter(status__in=['sold', 'rental'])
        .values('title')
        .annotate(total=Count('id'))
        .order_by('-total')[:5]
    )

    context = {
        'days': days,
        'top_categories': all_categories,
        'top_books': top_books,
    }

    return render(request, 'pages/best_selling_days.html', context)


def index(req):
    if req.method == 'POST':
        add_book = BookForm(req.POST, req.FILES)
        if add_book.is_valid():
            add_book.save()
            return redirect(req.path)
        add_category = CategoryForm(req.POST)
        if add_category.is_valid():
            add_category.save()
            return redirect(req.path)
    
    context = {
        'category' : Category.objects.all(),
        'books' : Book.objects.all(),
        'form' : BookForm(),
        'formcat': CategoryForm(),
        'allbooks' : Book.objects.filter(isActive=True).count(),
        'booksold' : Book.objects.filter(status='sold').count(),
        'bookrental' : Book.objects.filter(status='rental').count(),
        'bookavailble' : Book.objects.filter(status='availble').count(),
    }
    return render(req,'pages/index.html',context)


def books(req):
    search = Book.objects.all()
    title = None
    if  "search_name" in req.GET:
        title = req.GET["search_name"]
        if title:
            search = search.filter(title__icontains = title)
    
    
    
    context = {
        'category' : Category.objects.all(),
        'books' : search ,
        'formcat': CategoryForm(),
    }
    return render(req,'pages/books.html',context)


def delete(req, id):
    book_delete = get_object_or_404(Book, id = id)
    if req.method == 'POST':
        book_delete.delete()
        return redirect('/')
    
    
    return render(req,'pages/delete.html')


def update(req, id):
    book_id = Book.objects.get(id=id)
    if req.method == 'POST':
        book_save = BookForm(req.POST, req.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)
        
    context= {
        'formup' : book_save
    }
    
    
    return render(req,'pages/update.html',context)