from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.urls import reverse

from celery.result import AsyncResult


class StartExportView(TemplateView):
    """
        Triggers the task for creating an excel export and provides
        a waiting page that polls for completion.

        Requires self.export_method be defined
    """
    template_name = "django_celery_downloader/wait_task.html"
    download_url_name = ""

    def get_download_url(self, task):
        """ Useful if your download url will be dynamic """
        return reverse(self.download_url_name, args=[task])

    def get_task_params(self):
        """ Override this to add aditional parameters """
        return {}

    def get_context_data(self, **kwargs):
        _c = super(StartExportView, self).get_context_data(**kwargs)
        task = self.export_method.delay(self.get_task_params())
        _c['task'] = task
        _c['download_url'] = self.get_download_url(task)
        return _c


class DownloadExportView(View):
    """
        Extend and define mimetype and extension

        The generic View class doesn't have a get method, so this is it.
    """

    def get_filename(self):
        raise NotImplementedError

    def get(self, request, *args, **kwargs):
        """ Renders the excel file as a response """

        task_id = self.kwargs['task']
        result = AsyncResult(task_id)
        f = open(result.result, 'r')
        response = HttpResponse(f, mimetype=self.mimetype)
        response['Content-Disposition'] = ('attachment; filename=%s.%s' %
                                           (self.get_filename(),
                                            self.extension))
        return response
