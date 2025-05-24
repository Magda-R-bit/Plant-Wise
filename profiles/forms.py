from django import forms
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        labels = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postcode',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
            'default_country': 'Country',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            Row(
                Column(
                    'default_phone_number',
                    css_class='form-group col-md-6 mb-0'
                ),
            ),
            Row(
                Column(
                    'default_postcode',
                    css_class='form-group col-md-6 mb-0'
                ),
                Column(
                    'default_town_or_city',
                    css_class='form-group col-md-6 mb-0'
                ),
            ),
            'default_street_address1',
            'default_street_address2',
            'default_county',
            'default_country',
            Submit(
                'submit',
                'Update Profile',
                css_class='btn btn-success mt-3'
            )
        )
