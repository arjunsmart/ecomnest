from .models import Coupon

def menu_coupons(request):
    coupons = Coupon.objects.all()
    
    return {'menu_coupons':coupons}