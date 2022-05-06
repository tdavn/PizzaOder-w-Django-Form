from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import BanhmiForm

class HomeView(FormView):
    template_name = 'banhmi/index.html'
    form_class = BanhmiForm

def order(request):
    if request.method == 'POST':
        filled_form = BanhmiForm(request.POST)
        if filled_form.is_valid():
            note = f"Thank you for ordering! You {filled_form.cleaned_data['size']} {filled_form.cleaned_data['topping1']} and \
              {filled_form.cleaned_data['topping2']} banhmi is on its way."
            new_form = BanhmiForm()
            return render(request, 'banhmi/order.html', {'banhmiform':new_form, 'note':note})
    else:
        form = BanhmiForm()
        return render(request, 'banhmi/order.html', {'banhmiform': form})

