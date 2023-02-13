from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_title = 'TypeIdea管理后台'
    site_header = 'Typeidea'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
