import csv
from celery.decorators import task
from django.core.files.temp import NamedTemporaryFile


@task()
def build_report(rows):
    """
        A dummy report task. DownloadExportView expects a path to a file, so
        one needs to be created.

        I'm using a NamedTemporaryFile here that doesn't automatically delete
        you may need a cleanup method if you do it this way.
    """

    outfile = NamedTemporaryFile(suffix='.csv', delete=False)

    with open(outfile.name, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Column #1', 'Column #2', 'Column #3'])
        for i in range(int(rows)):
            writer.writerow(['Row #%d' % i, 'from task', 'build_report'])

    outfile.close()
    return outfile.name
