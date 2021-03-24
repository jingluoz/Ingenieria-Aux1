# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import TodoList, Category
import datetime
# Create your views here.

def index(request): #the index view
	todos = TodoList.objects.all() #quering all todos with the object manager
	categories = Category.objects.all() #getting all categories with object manager
	if request.method == "POST": #checking if the request method is a POST
		if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
			checkedlist = request.POST["checkedbox"]  # checked todos to be deleted
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id))  # getting todo id
				todo.delete()  # deleting todo
			return redirect("/") #reloading the page
		
			#Persona A agrega código AQUI!
	return render(request, "index.html", {"todos": todos, "categories":categories})
