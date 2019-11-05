from django.contrib import admin

# Register your models here.
from .models import SsoConfig


class SsoConfigAdmin(admin.ModelAdmin):
    list_display =  ('name','acs')

    #def get_form(self, request, obj=None, **kwargs):
     ##          u'Please go the through the default config json and its properties on <a href="',
       #         reverse_lazy("django_saml2_auth:default_config"),
        #        u'">this url</a>"')}
        #kwargs.update({'help_texts': help_texts})
        #return super(SsoConfigAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        super(SsoConfigAdmin,self).save_model(request, obj, form, change)
        obj.acs = request.build_absolute_uri('/')[:-1]+'/sso/acs/'+str(obj.id)
        obj.save()


    class Meta:
        model = SsoConfig


admin.site.register(SsoConfig, SsoConfigAdmin)
