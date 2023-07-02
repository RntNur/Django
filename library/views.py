from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from library.forms import BookForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def home(request):
    return render(request, 'home.html')


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    extra_context = {'title': 'Cписок книг'}
    success_url = reverse_lazy('book_detail', 'pk')


class BookDetails(DetailView):
    model = Book
    template_name = 'book_detail.html'
    extra_context = {'title': 'Подробнее о книг'}
    context_object_name = 'book'

    def get_success_url(self):
        pk = self.kwargs.get('pk')

class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_update.html'
    context_object_name = 'book_edit'

    def form_valid(self, form):
        book = form.save(commit = False)
        file = self.request.FILES.get('poster')  # получаем объект файла из запроса
        if file:  # если файл был загружен
            file_name = default_storage.save(file.name, ContentFile(file.read()))  # сохраняем файл
            book.poster = file_name  # сохраняем путь к файлу в качестве значения поля poster
        book.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_edit'] = BookForm(instance=self.object)
        return context


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_add.html'

    def form_valid(self, form):
        book = form.save(commit = False)
        file = self.request.FILES.get('poster')  # получаем объект файла из запроса
        if file:  # если файл был загружен
            file_name = default_storage.save(file.name, ContentFile(file.read()))  # сохраняем файл
            book.poster = file_name  # сохраняем путь к файлу в качестве значения поля poster
        book.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs = {'pk': self.object.pk})








# Ниже первая версия функций вывода списка и деталей объектов

# def book_list(request):
#     books = Book.objects.all()
#     context = {'books': books}
#     return render(request, 'book_list.html', context)


# def book_detail(request, book_id):
#     book = Book.objects.values().get(pk=book_id)
#     context = {'title': book['title'],
#                'description': book['description'],
#                'price': book['price'],
#                'cover_type': book['cover_type'],
#                'dimensions': book['dimensions'],
#                'pub_date': book['pub_date'],
#                'poster': book['poster']
#                }
#     return render(request, 'book_detail.html', context)
