from .serializers import CustomerSerializer, CustomerGroupSerializer
from safemanager.models import Customer, Customer_Group
from rest_framework import viewsets,generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all().order_by("id")

class CustomerGroupView(viewsets.ModelViewSet):
    serializer_class = CustomerGroupSerializer
    queryset = Customer_Group.objects.all().order_by("id")


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET thirdparty/api',
        'GET thirdparty/api/customers',
        'GET thirdparty/api/customers/:id',
        'POST thirdparty/api/create_customer/'
    ]
    return Response(routes)


@api_view(['GET'])
def getCustomers(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerGroupView(generics.ListAPIView):
    queryset = Customer_Group.objects.all()
    serializer_class = CustomerGroupSerializer

