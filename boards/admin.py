from django.contrib import admin
from  boards.models import Board , Post ,Topic


admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)
