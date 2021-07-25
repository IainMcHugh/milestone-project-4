from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["product"].widget.attrs["hidden"] = True
        self.fields["product"].label = False
        self.fields["user"].widget.attrs["hidden"] = True
        self.fields["user"].label = False

    comment = forms.CharField(max_length=254, widget=forms.Textarea)
    rating = forms.IntegerField(min_value=1, max_value=5, initial=1)
