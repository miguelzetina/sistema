
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied

from .models import Semilla
from .forms import SemillaForm
# Create your views here.


def semilla_list(request):
    queryset_list = Semilla.objects.all().order_by("Nombre")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(Nombre__icontains=query)|
            Q(CantidadExistente__icontains=query)|
            Q(CantidadPorHectarea__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset_list,
        "title": "Inventario"
    }

    return render(request, "semilla_list.html", context)


class SemillaCreate(CreateView):

    model = Semilla
    template_name = "ingreso_semilla.html"
    form_class = SemillaForm
    success_url = reverse_lazy('inventario:inventario')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return super(SemillaCreate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SemillaCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['semilla_list'] = Semilla.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


def semillaUpdate(request, id_semilla):
    if not request.user.is_staff:
        raise PermissionDenied
    #elif not request.user.is_superuser:
    #    return Http404

    semilla = Semilla.objects.get(id=id_semilla)
    if request.method == 'GET':
        form = SemillaForm(instance=semilla)
    else:
        form = SemillaForm(request.POST, instance=semilla)
        if form.is_valid():
            form.save()
        return redirect("inventario:inventario")

    return render(request, "update_semilla.html", {'form': form})


class SemillaDelete(DeleteView):
    model = Semilla
    template_name = "semilla_delete.html"
    form_class = SemillaForm
    success_url = reverse_lazy("inventario:inventario")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super(SemillaDelete, self).dispatch(request, *args, **kwargs)
