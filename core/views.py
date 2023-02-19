from rest_framework import generics, filters

from core.models import Factory, Stores, IndividualEntrepreneur, Contact
from rest_framework import permissions

from core.serializers import FactorySerializer, StoresSerializer, IndividualEntrepreneurSerializer, \
    ContactSerializer


class ContactCreateView(generics.CreateAPIView):
    model = Contact
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer


class ContactUpdateView(generics.UpdateAPIView):
    model = Contact
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer


class ContactDeleteView(generics.DestroyAPIView):
    model = Contact
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer


class ContactView(generics.RetrieveAPIView):
    model = Contact
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactListView(generics.ListAPIView):
    model = Contact
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['city']
    ordering = ['city']
    search_fields = ['city']


class FactoryCreateView(generics.CreateAPIView):
    model = Factory
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FactorySerializer


class FactoryView(generics.RetrieveAPIView):
    model = Factory
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()


class FactoryUpdateView(generics.UpdateAPIView):
    model = Factory
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()


class FactoryDeleteView(generics.DestroyAPIView):
    model = Factory
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()


class FactoryListView(generics.ListAPIView):
    model = Factory
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['city']
    ordering = ['city']
    search_fields = ['city']


class StoresCreateView(generics.CreateAPIView):
    model = Stores
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StoresSerializer


class StoresView(generics.RetrieveAPIView):
    model = Stores
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StoresSerializer
    queryset = Stores.objects.all()


class StoresUpdateView(generics.UpdateAPIView):
    model = Stores
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StoresSerializer
    queryset = Stores.objects.all()


class StoresDeleteView(generics.DestroyAPIView):
    model = Stores
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StoresSerializer
    queryset = Stores.objects.all()


class StoresListView(generics.ListAPIView):
    model = Stores
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StoresSerializer
    queryset = Stores.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['city']
    ordering = ['city']
    search_fields = ['city']


class IndividualEntrepreneurCreateView(generics.CreateAPIView):
    model = IndividualEntrepreneur
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IndividualEntrepreneurSerializer


class IndividualEntrepreneurView(generics.RetrieveAPIView):
    model = IndividualEntrepreneur
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()


class IndividualEntrepreneurUpdateView(generics.UpdateAPIView):
    model = IndividualEntrepreneur
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()


class IndividualEntrepreneurDeleteView(generics.DestroyAPIView):
    model = IndividualEntrepreneur
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()


class IndividualEntrepreneurListView(generics.ListAPIView):
    model = IndividualEntrepreneur
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['city']
    ordering = ['city']
    search_fields = ['city']
