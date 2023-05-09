import pytest


@pytest.fixture(scope='session')
def html_report_title():
    return 'Informe de pruebas de la aplicacion Ecommerce'

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html_report_title)

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, report.description)

def pytest_configure(config):
    config._metadata['Proyecto'] = 'Ecommerce'
    config._metadata['Tester'] = 'Diego-Novoa-Jairo-Perez'

def pytest_html_report_title(report):
    report.title = "Informe de pruebas de la aplicacion Ecommerce"

def pytest_html_results_table_row(report, cells):
    print(report)