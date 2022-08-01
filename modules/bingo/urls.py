from django.urls import path

from modules.bingo.views import UserView

urlpatterns = [path("", UserView.as_view({"get": "get"}), name="bingo")]
