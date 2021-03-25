from django.shortcuts import render

# Houses functions and classes that handle what data displays in HTML templates
# Create your views here

# Renders file when page is loaded, taking an HttpRequestObject as input when
# page is loaded. Contains info about req such as methods GET or POST
def hello_world(req):
    return render(req, "hello_world.html", {})
