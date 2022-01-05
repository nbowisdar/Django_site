from django.urls import path
from st.views import test_funk

urlpatterns = [
    path('test/', test_funk)
]