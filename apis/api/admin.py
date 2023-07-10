from django.contrib import admin
from .models import Account, Rack_group, Rack, Document, Borrowing,Environment_status, Operation_status,Breakdown_status,Operation,User,History
from django.utils.html import mark_safe
class DocumentAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all':('/static/css/main.css',)
        }
    list_display = ["id","name","rack_id_Document"]
    search_fields = ["name","author","id"]
    list_filter = ["author","rack_id_Document"]
    readonly_fields = ["avatar"]

    def avatar(self, Document):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120px'/>".format(img_url=Document.image.name,
                                                                                           alt=Document.name))
# Register your models here.

admin.site.register(Account)
admin.site.register(Rack_group)
admin.site.register(Rack, )
admin.site.register(Document, DocumentAdmin)
admin.site.register(Borrowing)
admin.site.register(Environment_status)
admin.site.register(Operation_status)
admin.site.register(Breakdown_status)
admin.site.register(Operation)
admin.site.register(User)
admin.site.register(History)

