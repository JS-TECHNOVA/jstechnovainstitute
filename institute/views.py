from django.shortcuts import render
from django.views import View
from . import models
# Create your views here.

class Home(View):
    template_name = "website/home.html"

    def get(self, req):
        tutors = models.Tutors.objects.all()[:10]
        st_feedbacks = models.StudentFeedbacks.objects.all()
        
        context = {
            "tutors":tutors,
            'st_feedbacks':st_feedbacks
        }

        return render(req, self.template_name, context=context)