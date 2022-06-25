from django import forms
from .models import Post, Comment, FreePost, FreeComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20,
            'cols' : 100
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }

class FreePostForm(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = ['title', 'address', 'size', 'period', 'price', 'body']

    def __init__(self, *args, **kwargs):
        super(FreePostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20,
        }

        self.fields['address'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "공유 공간의 주소 혹은 물건을 입력해주세요",
            'rows': 20,
        }

        self.fields['size'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "공유 공간의 넓이 혹은 물건의 크기를 입력해주세요",
            'rows': 20,
        }

        self.fields['period'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "기간을 입력해주세요",
            'rows': 20,
        }

        self.fields['price'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "희망 가격을 입력해주세요",
            'rows': 20,
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20,
            'cols' : 100,
        }


class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(FreeCommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }