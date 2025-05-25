from django import forms
from shop.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Enter a detailed description...'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        friendly_names = [(c.id, c.name) for c in categories]
        self.fields['category'].choices = friendly_names

        # Style and placeholders
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-2 form-control'

            placeholders = {
                'name': 'Product name',
                'price': 'e.g. 14.99',
                'image_url': 'http://example.com/image.jpg',
                'description': 'Brief product details',
            }
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]

            if field_name == 'name':
                field.widget.attrs['autofocus'] = True

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
