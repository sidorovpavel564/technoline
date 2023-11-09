from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['rows'] = '4'
            visible.field.widget.attrs['style'] = 'background: rgb(255, 255, 255); height: 105px;'

    class Meta:
        model = Review
        fields = ('text', )
