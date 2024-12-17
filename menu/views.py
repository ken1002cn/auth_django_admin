import json

from django.core.paginator import Paginator, EmptyPage
from django.views import View
from django.http import JsonResponse
from auth_django_admin.utill.JsonResultUtill import JsonResponseUtil
from menu.models import TravelItem, TravelItemDetail, TravelItemDetailRelImage, Product, FeaturedCuisine, \
    TravelItemDetailSerializer, TravelItemDetailRelImageSerializer, ProductSerializer, FeaturedCuisineSerializer


# Create your views here.
class TravelItemPageView(View):
    def get(self, request):
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 12))
        search_query = request.GET.get('search', '')  # 获取搜索条件
        # 如果有搜索条件，进行模糊匹配
        if search_query:
            travel_item = TravelItem.objects.filter(title__icontains=search_query)
        else:
            travel_item = TravelItem.objects.all()
        # 分页处理
        paginator = Paginator(travel_item, page_size)
        try:
            page_obj = paginator.get_page(page)  # 获取分页器实例
        except Exception:
            return JsonResponse({'code': 200, 'total': paginator.count, 'data': []})

        # 返回分页数据
        return JsonResponse({
            'code': 200,
            'total': paginator.count,
            'data': list(page_obj.object_list.values('id', 'title', 'image_url', 'status'))
        })

class TravelItemPageDetailView(View):
    def get(self,request):
        id = request.GET.get('id')
        try:
            travel_item_detail = TravelItemDetail.objects.get(item_id=id)
            travel_item_detail_image = TravelItemDetailRelImage.objects.filter(item_id=id)
            product = Product.objects.filter(item_id = id)
            featured_cuisine = FeaturedCuisine.objects.filter(item_id = id)
            return JsonResponse({
                'code':200,
                'message':'成功',
                'data':{
                    'detail': TravelItemDetailSerializer(travel_item_detail).data,
                    'image': TravelItemDetailRelImageSerializer(travel_item_detail_image, many=True).data,
                    'product': ProductSerializer(product, many=True).data,
                    'featured': FeaturedCuisineSerializer(featured_cuisine, many=True).data
                }
            })
        except TravelItemDetail.DoesNotExist:
            return JsonResponseUtil.failure("数据有误，详情信息不存在")
