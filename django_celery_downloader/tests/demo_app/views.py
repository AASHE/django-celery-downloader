from django.views.generic import TemplateView
from django_celery_downloader.views import StartExportView, DownloadExportView

from .tasks import build_report


class ReportView(TemplateView):

    template_name = "report.html"


class ReportExcelModalView(StartExportView):
    """
        Populates the download modal and triggers task
    """
    export_method = build_report
    download_url_name = "download_report"

    def get_task_params(self):
        return self.kwargs['rows']


class ReportExcelDownloadView(DownloadExportView):
    """
        Returns the result of the task (hopefully an excel export)
    """
    mimetype = 'text/csv'
    extension = "csv"

    def get_filename(self):
        return "My_Fancy_Report"
