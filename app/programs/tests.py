from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.

def test_homepage_access():
    url = reverse('home')
    assert url == "/"
