# <-------------------------------------------------------------------->
'''
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()  # будет выбрана одна конкретная запись, а не все
    serializer_class = WomenSerializer


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()  # будет выбрана одна конкретная запись, а не все
    serializer_class = WomenSerializer
'''

# <-------------------------------------------------------------------->
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from women.models import Women
from women.permissions import IsAdminOrReadOnly
from women.serializers import WomenSerializer


class WomenAPIListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10000


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)
    # permission_classes = (IsOwnerOrReadOnly,)
    # authentication_classes = (TokenAuthentication, )


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsAdminUser, )
    permission_classes = (IsAdminOrReadOnly,)

# <---------------------------------------------------->
# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         # return Women.objects.all()[:3]
#         if not pk:
#             return Women.objects.all()[:3]
#
#         return Women.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({"cats": cats.name})

# @action(methods=['get'], detail=False)
# def category(self, request):
#     cats = Category.objects.all()
#     return Response({"cats": [c.name for c in cats]})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Women.objects.get(pk=pk)
#         except Women.DoesNotExist:
#             raise Http404
#
#     def get(self, request):
#         # lst = Women.objects.all().values()
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#         return Response({'post': serializer.data})
#         # return Response({'post': WomenSerializer(post_new).data})
#         # return Response({'post': model_to_dict(post_new)})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method Put not allowed"})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object doesn't exist"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method Delete not allowed"})
#
#         # instance = Women.objects.get(pk=pk)
#         instance = self.get_object(pk)
#         instance.delete()
#
#         return Response({"post": "delete post " + str(pk)})
