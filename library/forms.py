from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'pages', 'price', 'cover_type', 'dimensions', 'pub_date', 'poster']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Название'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание'
                }
            ),
            'pages': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Кол-во страниц'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Стоимость'
                }
            ),
            'cover_type': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Тип обложки'
                }
            ),
            'dimensions': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Размеры'
                }
            ),
            'pub_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Дата публикации'
                }
            ),
            'poster': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file'
                }
            )

        }

        def clean_poster(self):
            poster = self.cleaned_data.get('poster')
            if poster:
                return poster.read()  # преобразование в байты
            return poster