from django.conf.urls.defaults import patterns, url
from django.views.decorators.cache import never_cache

from views import ReportView, ReportExcelModalView, ReportExcelDownloadView

urlpatterns = patterns(
    '',

    # Report Views
    url(
        r'^report/$',
        ReportView.as_view()),
    url(
        r'^report/csv-modal/(?P<rows>\d+)/$',
        never_cache(ReportExcelModalView.as_view()),
        name="report_modal"),
    url(
        r'^report/csv-download/(?P<task>[^/]+)/$',
        never_cache(ReportExcelDownloadView.as_view()),
        name="download_report")
)
