from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from inmar_app.api.parser import JSONSchemaParser
from inmar_app.api.serilizers import (
    StoreSerializer,
    DepartmentSerializer,
    CategorySerializer,
    SubcategorySerializer,
    LocationSerializer
)
from inmar_app.models import Store, Location, Department, Category, SubCategory


class StoreView(ListCreateAPIView):
    parser_classes = (JSONSchemaParser,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class LocationView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryView(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubcategorySerializer


@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def get_data(request, location=None, department=None, category=None, subcategory=None):

    """
    Method to return serialized data based on API request with all Http Methods.
    :param request: API request.
    :param location: location_id.
    :param department: department_id.
    :param category: category_id.
    :param subcategory: subcategory_id.
    :return: Serializer data if the query matches.
    :raise: Http404, not found data if match query not found.
    """

    data = {}
    if all([
        location, department, category, subcategory
    ]):
        data = Store.objects.filter(location=location, department=department,
                                    category=category, subcategory=subcategory
                                    )
    elif all([
        location, department, category
    ]):
        data = Store.objects.filter(location=location, department=department,
                                    category=category
                                    )
    elif location and department:
        data = Store.objects.filter(location=location, department=department)
    elif location:
        data = Store.objects.filter(location=location)
    if data:
        serialized_data = StoreSerializer(data, many=True)
        return Response(serialized_data.data)
    else:
        raise Http404




