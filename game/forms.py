from django import forms
from django.contrib.auth import get_user_model
from .models import Game
from datetime import date, timedelta, datetime

User = get_user_model()


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError(
                f'Пользователь с логином {username} не найден в системе')
        if not user.check_password(password):
            raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    first_name = forms.CharField()
    email = forms.EmailField()
    message_to_santa = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['phone'].label = 'Номер телефона'
        self.fields['address'].label = 'Адрес'
        self.fields['email'].label = 'Почта'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['message_to_santa'].label = 'Письмо Санте'

    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['net', 'xyz']:
            raise forms.ValidationError(
                f'Регистрация для домена {domain} невозможна')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Данный почтовый адрес уже зарегистрирован')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f'Имя {username} занято. Попробуйте другое.')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name',
                  'last_name', 'address', 'phone', 'email']


class GameForm(forms.ModelForm):
    name = forms.CharField(required=True)
    price_limit = forms.IntegerField(required=False)
    draw_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    gift_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Название игры'
        self.fields['price_limit'].label = 'Стоимость подарка'
        self.fields['draw_date'].label = 'Дата жеребьёвки'
        self.fields['gift_date'].label = 'Дата отправки подарка'

    def clean(self):
        draw_date = self.cleaned_data['draw_date']
        gift_date = self.cleaned_data['gift_date']
        date_select = datetime.strptime('2021-12-31', '%Y-%m-%d').date()

        if draw_date < date.today() or date_select < draw_date:
            raise forms.ValidationError(
                'Жеребьевку можно провести начиная с сегодняшнего и до 31.12.2021.')

        if gift_date < draw_date or date_select < gift_date:
            raise forms.ValidationError(
                'Подарок можно отправить только после жеребьевки и до 31.12.2021.')

        return self.cleaned_data

    class Meta:
        model = Game
        fields = [
            'name', 'price_limit', 'draw_date', 'gift_date',
        ]
