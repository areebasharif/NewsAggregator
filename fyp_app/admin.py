from django.contrib import admin
from .models import Contact
from .models import Registeration
from .models import Document

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("sno", "name", "email", "message", "timeStamp")


admin.site.register(Contact, ContactAdmin)


class RegisterationAdmin(admin.ModelAdmin):
    list_display = ("sno", "firstName", "lastName", "email", "password", "timeStamp")


admin.site.register(Registeration, RegisterationAdmin)


admin.site.register(Document)
from .models import Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = (
        "message",
        "created",
        "user",
    )
    search_fields = ["message"]
