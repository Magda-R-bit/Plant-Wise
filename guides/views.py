from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Guide
from .forms import GuideForm


def guide_list(request):
    guides = (
        Guide.objects.filter(is_published=True)
        .exclude(category='user')
        .order_by('-created_on')[:3]
    )
    tips = (
        Guide.objects.filter(category='user', is_published=True)
        .order_by('-created_on')[:3]
    )
    return render(
        request,
        'guides/guide_list.html',
        {
            'guides': guides,
            'tips': tips
        }
    )


def guide_detail(request, slug):
    guide = get_object_or_404(Guide, slug=slug, is_published=True)
    return render(
        request,
        'guides/guide_detail.html',
        {'guide': guide}
    )


def tip_list(request):
    tips = (
        Guide.objects.filter(category='user', is_published=True)
        .order_by('-created_on')
    )
    return render(request, 'guides/tip_list.html', {'tips': tips})


@login_required
def submit_tip(request):
    if request.method == 'POST':
        form = GuideForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.user = request.user
            tip.category = 'user'
            tip.is_published = False
            tip.save()
            messages.success(
                request,
                "Thank you for your tip! It will be reviewed shortly."
            )
            return redirect('tip_list')
    else:
        form = GuideForm()
    return render(request, 'guides/submit_tip.html', {'form': form})
