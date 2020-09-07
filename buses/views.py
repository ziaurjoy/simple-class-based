from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.shortcuts import render
# from django.views.generic import ListView,CreateView,UpdateView
from django.views import generic

from buses.models import BussesCompany


class BusCompanyList(generic.ListView):
    model = BussesCompany
    queryset = BussesCompany.objects.all().order_by('name')
    context_object_name = 'buses'
    template_name = 'buses/index.html'





class BusCompanyCreate(UserPassesTestMixin,generic.CreateView):
    model = BussesCompany
    template_name = "buses/forms.html"
    fields = '__all__'
    success_url = 'http://127.0.0.1:8000/'

    def test_func(self):
        return self.request.user.has_perm('buses.add_bussescompany')


class BusCompanyUpdagte(UserPassesTestMixin,generic.UpdateView):
    model = BussesCompany
    template_name = 'buses/forms.html'
    fields = '__all__'
    success_url = 'http://127.0.0.1:8000/'

    def test_func(self):
        return self.request.user.has_perm('buses.change_bussescompany')


class BusCompanyDelete(UserPassesTestMixin,generic.DeleteView):
    model = BussesCompany
    template_name = 'buses/delete.html'
    success_url = '/'

    def test_func(self):
        return self.request.user.has_perm('buses.delete_bussescompany')

# def buses_company_list(request):
#     buses = BussesCompany.objects.all().order_by('name')
#     context = {
#         'buses':buses
#     }
#     return render(request,'buses/index.html',context)

