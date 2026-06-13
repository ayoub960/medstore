from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicine, Order
from .forms import OrderForm


def home(request):
    medicines = Medicine.objects.all()
    return render(request, 'home.html', {'medicines': medicines})


def medicine_detail(request, slug):
    medicine = get_object_or_404(Medicine, slug=slug)
    form = OrderForm()

    return render(request, 'medicine_detail.html', {
        'medicine': medicine,
        'form': form
    })


def place_order(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.medicine = medicine
            order.save()

            return redirect('order_success')

        # 🔥 IMPORTANT: if invalid, return form with errors
        return render(request, 'medicine_detail.html', {
            'medicine': medicine,
            'form': form
        })

    return redirect('medicine_detail', slug=medicine.slug)


def order_success(request):
    return render(request, 'order_success.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')