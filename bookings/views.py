from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import BookingForm
from .models import NewBooking
from bands.models import Band


def new_booking(request, band_id):
    """
    A view to display booking form and process booking
    """
    band = get_object_or_404(Band, pk=band_id)
    form = BookingForm()

    if request.method == 'POST':

        booking_form = {
            'client_name': request.POST['client_name'],
            'email': request.POST['email'],
            'contact_number': request.POST['contact_number'],
            'venue_name': request.POST['venue_name'],
            'venue_address1': request.POST['venue_address1'],
            'venue_address2': request.POST['venue_address2'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'wedding_date': request.POST['wedding_date'],
            'start_time': request.POST['start_time'],
            'emergency_contact': request.POST['emergency_contact'],
            'emergency_phone': request.POST['emergency_phone'],
            'additional_information': request.POST['additional_information'],
        }

        form = BookingForm(booking_form)
        if form.is_valid():
            form.save()

        return redirect('all_bands')

    context = {
            'band': band,
            'form': form,
            }

    return render(request, 'bookings/new_booking.html', context)


@login_required
def my_bookings(request):
    """
    A view to display users bookings
    """
    user = request.user.email
    bookings = NewBooking.objects.filter(email=user)

    context = {
        'bookings': bookings,
        'user': user,
    }

    return render(request, 'bookings/my_bookings.html', context)
