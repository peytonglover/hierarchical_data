from django.shortcuts import render
from homepage.models import File
from mptt.utils import drilldown_tree_for_node
# Create your views here.

def index(request):
    return render(request, 'index.html')