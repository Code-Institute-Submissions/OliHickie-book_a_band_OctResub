from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import stripe

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
            booking_form = form.save(commit=False)
            booking_form.email = request.user.email
            booking_form.band_name = band.name
            booking_form.price = band.price
            form.save()

        return redirect('my_bookings')

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
    bookings = NewBooking.objects.filter(email=user).order_by('paid')

    confirmed_bookings = bookings.filter(paid=True)
    unconfirmed_bookings = bookings.filter(paid=False)
    total = 0
    for booking in unconfirmed_bookings:
        total += booking.price

    context = {
        'bookings': bookings,
        'user': user,
        'confirmed_bookings': confirmed_bookings,
        'unconfirmed_bookings': unconfirmed_bookings,
        'total': total,
    }

    return render(request, 'bookings/my_bookings.html', context)


# @csrf_exempt
# def create_checkout_session(request):
#     if request.method == 'POST':
#         try:
#             checkout_session = stripe.checkout.Session.create(
#                 line_items=[
#                     {
#                         'price': '1000',
#                         'quantity': 1,
#                     },
#                 ],
#                 customer_email=request.user.email,
#                 payment_method_types='card',
#                 currency='gbp',
#                 mode='payment',
#                 success_url='https://8000-lime-moose-106flrrt.ws-eu16.gitpod.io/bands/?sort=rating&direction=desc',
#                 cancel_url='https://8000-lime-moose-106flrrt.ws-eu16.gitpod.io/bands/?sort=rating&direction=desc',
#             )

#             return JsonResponse({'sessionId': checkout_session.id})

#         except stripe.error.StripeError as error:
#             return JsonResponse({'error': str(error)})
