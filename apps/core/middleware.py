import time
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from apps.core.models import DailyVisit, UserActivity


def simple_middleware(get_response):
    def middleware(request):
        print("Hello ! -> in middleware 😉")
        response = get_response(request)
        return response

    return middleware


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Hello ! -> in middleware 😉")
        response = self.get_response(request)
        return response


class BetterSimpleMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__(get_response)

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print("Process View -> in middleware (BetterSimpleMiddleware) 🔥")
    #     return view_func(request, view_args, view_kwargs)

    # def process_exception(self, request, exception):
    #     print("Exception Handing -> 🐱")
    #     pass

    def __call__(self, request):
        print("Hello ! -> in middleware (BetterSimpleMiddleware) 🔥")
        response = self.get_response(request)
        return response


class ResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        print(f"⏰  {duration:.2f}s - {request.path}")
        return response


class DailyVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        today = timezone.now().date()

        # ignore admin path
        if "/admin" not in (url := request.path):
            visit, _ = DailyVisit.objects.get_or_create(date=today, url=url)
            visit.count += 1
            visit.save()

        return self.get_response(request)


class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def get_client_ip(request):
        return _.split(',')[0] if (_:=request.META.get('HTTP_X_FORWARDED_FOR')) else request.META.get('REMOTE_ADDR')

    @staticmethod
    def get_user(request):
        return (request.user.is_authenticated and request.user) or None

    def __call__(self, request):
        # ignore admin path
        if "/admin" not in (url := request.path):
            UserActivity.objects.create(
                timestamp=timezone.now(),
                url=url,
                ip=self.get_client_ip(request),
                user=self.get_user(request)
            )


        return self.get_response(request)