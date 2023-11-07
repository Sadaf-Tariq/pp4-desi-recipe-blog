from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Recipe, Rating, Comment, RecipeCategory, RecipeMethod
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import CommentForm


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


def full_recipe(request, slug, *args, **kwargs):
    """
    A function-based view to view the detail of a post.
    Largely the same as the class-based, but we don't have
    different methods for GET and POST. Because it's not a
    class, all of the extra "self" stuff is removed too.

    Functionally, it's the same, but it is a bit clearer
    what's going on. To differentiate between request methods,
    we use request.method == "GET" or request.method == "POST"
    """

    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    liked = False
    commented = False

    if recipe.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            # comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment pending approval!')
        else:
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "full_recipe.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "liked": liked,
            "comment_form": comment_form
        },
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


# def CategoryList(request):
#     queryset = RecipeCategory.objects.all()
#     context = {
#         'queryset': queryset
#     }
#     return render(request, "home.html", context)