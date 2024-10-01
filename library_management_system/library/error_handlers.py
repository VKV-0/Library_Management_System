from django.shortcuts import render
from django.http import JsonResponse
from django.template import TemplateDoesNotExist

"""
Generic function to handle errors based on the status code and request type.
"""
def handle_error(request, template_name, status_code, exception=None):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'error': 'An error occurred.'}, status=status_code)
    else:
        context = {'status_code': status_code, 'exception': exception}
        try:
            return render(request, f'errors/{template_name}', context, status=status_code)
        except TemplateDoesNotExist:
            return render(request, 'errors/base_error.html', {
                'status_code': status_code,
                'error_message': "Template Not Found",
                'error_description': "The requested template could not be found.",
            }, status=status_code)
        


# Dictionary to map error codes to their handlers
error_handlers = {
    404: lambda request, exception=None: handle_error(request, '404.html', 404, exception),
    500: lambda request, exception=None: handle_error(request, '500.html', 500, exception),
    403: lambda request, exception=None: handle_error(request, '403.html', 403, exception),
    400: lambda request, exception=None: handle_error(request, '400.html', 400, exception),
}

