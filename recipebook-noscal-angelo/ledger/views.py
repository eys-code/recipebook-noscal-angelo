from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RecipeForm, RecipeImageForm
from .models import Recipe, RecipeImage

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipe_create.html"
    form_class = RecipeForm


    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = "recipe_add_image.html"
    form_class = RecipeImageForm

    def get_success_url(self):
        return reverse_lazy(
            "ledger:recipe_detail", kwargs={"pk": self.object.recipe.pk}
        )

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)