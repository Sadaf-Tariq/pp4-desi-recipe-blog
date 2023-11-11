from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe, Rating, Comment, RecipeCategory, RecipeMethod
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import CommentForm, RecipeForm, RatingForm
from django.urls import reverse_lazy


# class RecipeList(generic.ListView):

#     model = Recipe
#     queryset = Recipe.objects.all().order_by('-created_on')
#     template_name = "home.html"
#     paginated_by = 6

class RecipeList(generic.ListView):

    context_object_name = "model"
    template_name = "home.html"
    paginated_by = 6

    def get_queryset(self):
        myset = {
            "recipe_list": Recipe.objects.all(),
            "category_list": RecipeCategory.objects.all(),
            "method_list": RecipeMethod.objects.all(),
        }
        return myset


# def full_recipe(request, slug, *args, **kwargs):
#     """
#     A function-based view to view the detail of a post.
#     Largely the same as the class-based, but we don't have
#     different methods for GET and POST. Because it's not a
#     class, all of the extra "self" stuff is removed too.

#     Functionally, it's the same, but it is a bit clearer
#     what's going on. To differentiate between request methods,
#     we use request.method == "GET" or request.method == "POST"
#     """

#     queryset = Recipe.objects.all()
#     recipe = get_object_or_404(queryset, slug=slug)
#     comments = recipe.comments.all().order_by("-created_on")
#     comment_count = recipe.comments.filter(approved=True).count()
#     liked = False
#     commented = False

#     if recipe.likes.filter(id=request.user.id).exists():
#         liked = True

#     if request.method == "POST":
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             comment_form.instance.email = request.user.email
#             # comment_form.instance.name = request.user.username
#             comment = comment_form.save(commit=False)
#             comment.recipe = recipe
#             comment.save()
#             messages.add_message(request, messages.SUCCESS,
#                                  'Comment pending approval!')
#         else:
#             comment_form = CommentForm()
#     else:
#         comment_form = CommentForm()

#     return render(
#         request,
#         "full_recipe.html",
#         {
#             "recipe": recipe,
#             "comments": comments,
#             "comment_count": comment_count,
#             "liked": liked,
#             "comment_form": comment_form
#         },
#     )

# def full_recipe(request, slug, *args, **kwargs):
#     """
#     A function-based view to view the detail of a post.
#     Largely the same as the class-based, but we don't have
#     different methods for GET and POST. Because it's not a
#     class, all of the extra "self" stuff is removed too.

#     Functionally, it's the same, but it is a bit clearer
#     what's going on. To differentiate between request methods,
#     we use request.method == "GET" or request.method == "POST"
#     """

#     queryset = Recipe.objects.all()
#     recipe = get_object_or_404(queryset, slug=slug)
#     comments = recipe.comments.all().order_by("-created_on")
#     comment_count = recipe.comments.filter(approved=True).count()
#     liked = False
#     commented = False

#     if recipe.likes.filter(id=request.user.id).exists():
#         liked = True

#     if request.method == "POST":
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             comment_form.instance.email = request.user.email
#             # comment_form.instance.name = request.user.username
#             comment = comment_form.save(commit=False)
#             comment.recipe = recipe
#             comment.save()
#             messages.add_message(request, messages.SUCCESS,
#                                  'Comment pending approval!')
#         else:
#             comment_form = CommentForm()
#     else:
#         comment_form = CommentForm()

#     return render(
#         request,
#         "full_recipe.html",
#         {
#             "recipe": recipe,
#             "comments": comments,
#             "comment_count": comment_count,
#             "liked": liked,
#             "comment_form": comment_form
#         },
#     )


class FullRecipe(View):

    commented = False

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

    
        return render(
            request,
            "full_recipe.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": self.commented,
                "liked": liked,
                "comment_form": CommentForm(),
                "rating_form": RatingForm(),
            },
        )

    
    def post(self, request, slug, *args, **kwargs, ):


        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by("-created_on") 
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        rating_form = RatingForm()
        comment_form = CommentForm()

        if 'rating_hidden_field' in self.request.POST:
            rating_form = RatingForm(data=request.POST)
            if rating_form.is_valid():
                counts = recipe.comments.filter(approved=False, email=request.user, recipe=recipe).count() 
                if counts > 0:
                    self.commented = True
                rating_form.instance.user_id = request.user.id
                reviewCheck = Rating.objects.filter(user=request.user, recipe=recipe).count()
                if request.user.is_authenticated:
                    if reviewCheck > 0:
                        Rating.objects.filter(recipe=recipe, user=request.user).first().delete() 
                rating = rating_form.save(commit=False)
                rating.recipe = recipe
                rating.save()
                # return redirect('post_detail', post.slug)
            else:
                counts = recipe.comments.filter(approved=False, email=request.user, recipe=recipe).count() 
                if counts > 0:
                    self.commented = True

            

        if 'comment_hidden_field' in self.request.POST:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                self.commented = True
                comment_form.instance.email = request.user.email
                comment = comment_form.save(commit=False)
                comment.recipe = recipe
                comment.save()
                # return redirect('post_detail', post.slug)


        return render(
            request,
            "full_recipe.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": self.commented,
                "rating_form": rating_form,
                "comment_form": comment_form,
                "liked": liked,
            }
        )


def recipe_like(request, slug, *args, **kwargs):
    """
    The view to update the likes. Although it should always be
    called using the POST method, we have still added some
    defensive programming to make sure.
    """
    post = get_object_or_404(Recipe, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponseRedirect(reverse('full_recipe', args=[slug]))


class RecipeCatListView(generic.ListView):
    template_name = 'recipes_category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'recipes': Recipe.objects.filter(category__food_type=self.kwargs['category'])
        }
        return content


class RecipeMethodListView(generic.ListView):
    template_name = 'recipes_method.html'
    context_object_name = 'methodlist'

    def get_queryset(self):
        content = {
            'method': self.kwargs['method'],
            'recipes': Recipe.objects.filter(method__recipe_method=self.kwargs['method'])
        }
        return content


class CreateNewRecipe(CreateView):
    model = Recipe
    template_name = "create_new_recipe.html"
    form_class = RecipeForm
    # success_url = reverse_lazy('new_recipe')

    def get_success_url(self):
        URL = self.request.path_info
        return HttpResponseRedirect(URL)

    def form_valid(self, form):
        obj = form.save(commit=False)
        form.instance.author_email = self.request.user
        messages.add_message(self.request, messages.SUCCESS,
                             "Your recipe has been added successfully.")
        obj.save()
        return super().form_valid(form)


class EditRecipe(UpdateView):
    model = Recipe
    template_name = "edit_recipe.html"
    form_class = RecipeForm
    success_url = reverse_lazy('home')

    # def get_success_url(self):
    #     URL = self.request.path_info
    #     return HttpResponseRedirect(URL)
        
    def form_valid(self, form):
        form.instance.author_email = self.request.user
        messages.add_message(self.request, messages.SUCCESS,
                             "Your recipe has been updated successfully.")
        return super().form_valid(form)
