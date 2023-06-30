from django.utils.translation import activate


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = request.META.get('HTTP_ACCEPT_LANGUAGE')

        # Determine the user's language preference here
        # For example, you can check the language in the request header
        # and set the language accordingly
        if language == 'ar':
            activate('ar')  # Set the language to Arabic
        else:
            activate('en')  # Set the language to English

        response = self.get_response(request)
        return response