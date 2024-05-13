from django.shortcuts import render
from .models import Profile


def create_profile(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        designation = request.POST.get('designation')
        mobile_number = request.POST.get('mobile_number')
        profile_summary = request.POST.get('profile_summary')
        skills = request.POST.get('skills')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')

        profile = Profile(full_name == full_name, mobile_number == mobile_number,
                          designation==designation,profile_summary==profile_summary,
                          skills==skills,city==city,state==state,country==country
                          )

        profile.save()

    return render(request, 'profile.html',{'profiles':profiles})







