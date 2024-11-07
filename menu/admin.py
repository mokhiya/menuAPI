from tkinter import Menu

from django.contrib import admin

from menu.models import MenuModel, CommentModel


@admin.register(MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'meal', 'comment')
