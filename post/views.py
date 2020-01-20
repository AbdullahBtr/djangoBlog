from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post,Comment
from users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

# Create your views here.

class CreatePostView(LoginRequiredMixin,CreateView):
    model=Post
    template_name='create_post.html'
    fields=['title','body_text',]
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListPostView(ListView):
    model = Post
    template_name = 'home.html'
    #queryset = Post.objects.all()
    #context_object_name = 'posts'#list gets the name posts
    ordering = ['-created_on']
    paginate_by=4


class DetailPostView(DetailView):
    model = Post
    template_name = 'post_detail.html'    

class DeletePostView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')

    #only owner of post is able to delete it
    def test_func(self):
        self.object=self.get_object()
        return self.object.author==self.request.user

class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body_text']

    #only owner of post is able to update it
    def test_func(self):
        self.object=self.get_object()
        return self.object.author==self.request.user

class SearchPostView(ListView):
    model=Post
    template_name='search_list.html'

    def get_queryset(self): 
        #return Post.objects.raw('SELECT id,title,body_text FROM post_post where title=%s',[self.request.GET['search']])
        return Post.objects.filter(Q(title__icontains=self.request.GET['search']) | Q(body_text__icontains=self.request.GET['search']))

class ProfilPostView(ListView):
    model=Post
    template_name='profile.html'

    #display posts created by user
    def get_queryset(self):
        #doppelter unterstrich um auf die felder der User tabelle zuzugereifen
        return Post.objects.filter(author__username=self.kwargs['slug']).order_by('created_on')
        #return Post.objects.filter(author=self.request.user).order_by('created_on')

    #display profile information of user
    def get_context_data(self,**kwargs):
        context=super(ProfilPostView,self).get_context_data(**kwargs)
        context['profiles']=Post.objects.filter(author__username=self.kwargs['slug'])
        return context

class CreateCommentView(LoginRequiredMixin,CreateView):
    model=Comment
    template_name='create_comment.html'
    fields=['text','email']

