from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from . import models
from . import forms
from django.contrib import messages
# Create your views here.

class SubmitGetInTouchForm(View):
    def post(self, req):
        get_in_touch_form = forms.GetInTouchForm(req.POST)
        if get_in_touch_form.is_valid():
            get_in_touch_form.save()
            messages.success(req, "Success!!")
        return redirect("home")


class Home(View):
    template_name = "website/home.html"

    def get(self, req):
        tutors = models.Tutors.objects.all()[:10]
        st_feedbacks = models.StudentFeedbacks.objects.all()
        
        context = {
            "tutors":tutors,
            'st_feedbacks':st_feedbacks,
            "get_in_touch_form": forms.GetInTouchForm(),
        }
        return render(req, self.template_name, context=context)
    


class AboutView(View):
    def get(self,req):
        return render(req, "website/about.html")


class BookDemoClass(View):
    def get(self, req):
        context = {
            "book_demo_class_form": forms.DemoClassForm()
        }
        return render(req, "website/book-demo-class.html", context=context)

    def post(self, req):
        form = forms.DemoClassForm(req.POST)
        context = {
            "book_demo_class_form": form
            }
        if form.is_valid():
            form.save(commit=True)
            messages.success(req,"Your Details are submitted. Out team will contact you soon.")
            return redirect("BookDemoClass")
        else:
            return render(req, "website/book-demo-class.html", context=context)



class Tutors(View):
    def get(self, req):
        context = {
            "tutor_reg_form": forms.TutorRegForm()
        }
        return render(req, "website/tutor.html", context=context)

    def post(self, req):
        form = forms.TutorRegForm(req.POST, req.FILES)
        context = {
            "tutor_reg_form": form
            }
        if form.is_valid():
            form.save(commit=True)
            messages.success(req,"Your Details are submitted. Out team will contact you soon.")
            return redirect("tutors")
        else:
            return render(req, "website/tutor.html", context=context)

