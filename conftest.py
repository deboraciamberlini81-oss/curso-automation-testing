from pytest_metadata.plugin import metadata_key


def pytest_configure(config):
    config.stash[metadata_key]["Proyecto"] = "QA Automation"
    config.stash[metadata_key]["Autor"] = "Debora"
    config.stash[metadata_key]["Aplicacion UI"] = "SauceDemo"
    config.stash[metadata_key]["API"] = "JSONPlaceholder"


def pytest_html_report_title(report):
    report.title = "Talento Lab - QA Automation"