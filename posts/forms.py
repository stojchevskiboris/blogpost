from django import forms
from .models import Post, PostComment


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
            # field.field.widget.attrs["disabled"] = "true"

    class Meta:
        model = Post
        exclude = ("author",)


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
            # field.field.widget.attrs["disabled"] = "true"

    class Meta:
        model = PostComment
        exclude = ("posted_by", "post",)
