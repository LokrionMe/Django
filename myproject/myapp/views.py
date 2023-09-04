import logging
from django.http import HttpResponse
from django.shortcuts import render
logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, 'main.html')


def about(request):
    logger.debug('About page accessed')
    return render(request, 'about.html')
