from django import forms
from ckeditor.widgets import CKEditorWidget

from blogger.models import Post

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from crispy_forms.bootstrap import PrependedText

class CreatePostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Post
        fields = ['title', 'content']
