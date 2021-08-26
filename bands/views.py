from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .forms import BandForm
from .models import Band, Category


def all_bands(request):
    """
    A view to display all bands and quick links
    """
    # Display bands, ordered by rating (highest first)
    bands = Band.objects.all().order_by('-rating')
    categories = Category.objects.all()
    query = None

    # full list of locations
    full_location_list = []
    # location list without duplicates
    locations = []
    for band in bands:
        i = band.location
        full_location_list.append(i)
        if i not in locations:
            locations.append(i)

    # sorted alphabetically
    sorted_locations = sorted(locations)

    # Count number of occurances for each location, add to dict
    locations_counted = {}
    for x in sorted_locations:
        num = full_location_list.count(x)
        locations_counted[x] = num

    # Search for bands
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(name__icontains=query) | Q(biography__icontains=query)
            bands = bands.filter(queries)

        # Search by location
        if 'locations' in request.GET:
            query = request.GET['locations']
            queries = Q(location__icontains=query)
            bands = bands.filter(queries)

        # if 'group' in request.GET:
        #     query = request.GET['group']
        #     if query == 'strings':
        #         query = 1
        #     bands = bands.filter(category__name__in=query)

        # Search by price
        if 'price' in request.GET:
            query = request.GET['price']
            if query == '£2000':
                bands = bands.filter(price__gte=2000)
            if query == '£1500':
                bands = bands.filter(price__range=(1500, 1999))
            if query == '£1000':
                bands = bands.filter(price__range=(1000, 1499))
            if query == '£500':
                bands = bands.filter(price__range=(500, 999))
            if query == 'Less than £500':
                bands = bands.filter(price__lt=500)

    context = {
        'bands': bands,
        'categories': categories,
        'locations': locations,
        'locations_counted': locations_counted,
        'query': query,
    }

    return render(request, 'bands/bands.html', context)


def band_profile(request, band_id):
    """
    A view to display the band profile
    """

    band = get_object_or_404(Band, pk=band_id)

    # Return four random bands in same category, excluding current band
    random_bands = Band.objects.all().filter(
        category=band.category).exclude(pk=band_id).order_by('?')[:4]

    context = {
        'band': band,
        'random_bands': random_bands,
    }

    return render(request, 'bands/band_profile.html', context)


def add_band(request):
    """
    A view to add a new band to the database
    """

    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # change to form when messages complete
            return redirect('success')
    else:
        form = BandForm()
    return render(request, 'bands/add_band.html', {'form': form})


# remove once messages complete
def success(request):
    return HttpResponse('successfully uploaded')
