from django.shortcuts import render
from django.views.generic import TemplateView

from inmar_app.forms import StoreForms
from inmar_app.models import Location, Department, Category, SubCategory, Store


class StoreView(TemplateView):
    template_name = 'store/store.html'

    def get(self, request, *args, **kwargs):
        store = Store.objects.all()
        return self.render_to_response(context={'data': store})

    def post(self, request, *args, **kwargs):
        return render(request, 'store/add.html', {'data': 'done'})


def add_store(request):
    if request.method == 'GET':
        form = StoreForms()
        return render(request, 'store/add.html', {'form': form})
    elif request.method == 'POST':
        form = StoreForms(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'store/add.html', {'operation': 'successfull'})


def get_store_by_id(request, id):
    store = Store.objects.get(id=id)
    return render(request, 'store/store.html', {'data': store, 'data_id': 'id'})


def update_store(request):
    test = 'test'


def delete_store(request, id):
    data = Store.objects.get(id=id).delete()
    return render(request, 'store/delete.html', {'id':id})
