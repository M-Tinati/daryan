from django import forms

class CreateOrderForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        label="نام و نام خانوادگی",
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'نام و نام خانوادگی'})
    )
    phone = forms.CharField(
        max_length=11,
        label="شماره تلفن",
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'شماره تلفن'})
    )
    national_id = forms.CharField(
        max_length=10,
        label="کد ملی",
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'کد ملی'})
    )
    address = forms.CharField(
        label="آدرس",
        widget=forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 3, 'placeholder': 'آدرس کامل'})
    )
    length = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        label="متراژ لوله (متر)",
        widget=forms.NumberInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'متراژ لوله'})
    )
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        label="تعداد",
        widget=forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'})
    )
