from django.http import HttpResponse

def about_us(request):
    return HttpResponse("<h1>About Us</h1><p>Welcome to our Car Dealership Application!</p>")

def contact_us(request):
    return HttpResponse("<h1>Contact Us</h1><p>Email us at support@dealership.com</p>")
