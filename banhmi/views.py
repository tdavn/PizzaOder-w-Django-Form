from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import BanhmiForm, MultipleBanhmiForm
from django.forms import formset_factory
from .models import Banhmi

class HomeView(FormView):
    template_name = 'banhmi/index.html'
    form_class = BanhmiForm
    context = {'form': form_class}
    success_url = 'banhmi/order.html'

    def form_valid(self, form):
        return super().form_valide(form)


def order(request):
    multiple_form = MultipleBanhmiForm()
    if request.method == 'POST':
        filled_form = BanhmiForm(request.POST)
        if filled_form.is_valid():
            created_banhmi = filled_form.save()
            created_banhmi_pk = created_banhmi.id
            note = f"Thank you for ordering! You {filled_form.cleaned_data['size']} {filled_form.cleaned_data['topping1']} and \
              {filled_form.cleaned_data['topping2']} banhmi is on its way."
            filled_form = BanhmiForm()
        else:
            created_banhmi_pk = None
            note = 'Pizza order has failed. Try again!'
        return render(request, 'banhmi/order.html', {'created_banhmi_pk': created_banhmi_pk,
                                                         'banhmiform': filled_form, 'note': note, 'multiple_form': multiple_form})
    else:
        form = BanhmiForm()
        return render(request, 'banhmi/order.html', {'banhmiform': form, 'multiple_form': multiple_form})

def banhmis(request):
    number_of_banhmi = 2
    filled_multiple_banhmi_form = MultipleBanhmiForm(request.GET)
    if filled_multiple_banhmi_form.is_valid():
        number_of_banhmi = filled_multiple_banhmi_form.cleaned_data['number']
    BanhmiFormSet = formset_factory(BanhmiForm, extra=number_of_banhmi)
    formset = BanhmiFormSet()
    if request.method == 'POST':
        filled_formset = BanhmiFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
                print(form.cleaned_data['topping1'])
            note = 'Banhmis have been ordered!'
        else:
            note = 'Oder was not created, please try again'
        return render(request, 'banhmi/banhmis.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'banhmi/banhmis.html', {'formset': formset})

def edit_order(request, pk):
    banhmi = Banhmi.objects.get(pk=pk)
    form = BanhmiForm(instance=banhmi)
    note = f'Banhmi no {pk}!'
    if request.method == 'POST':
        filled_form = BanhmiForm(request.POST, instance=banhmi)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order updated!'
        else:
            note = 'Not update yet.'

        return render(request, 'banhmi/edit_order.html', {'banhmiform': form,
                                                     'banhmi': banhmi, 'note': note})
    else:
        return render(request, 'banhmi/edit_order.html', {'banhmiform': form,
                                                   'banhmi': banhmi, 'note': note})