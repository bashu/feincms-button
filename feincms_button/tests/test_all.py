from django.test import TestCase

from feincms.module.page.models import Page

from .models import PageButtonContent


class ButtonContentTest(TestCase):
    def setUp(self):
        self.page = Page.objects.create(title="Home", slug="home", override_url="/")

    def test_primary(self):
        content = PageButtonContent.objects.create(
            parent=self.page,
            region="main",
            url="http://example.com",
            style="btn-primary",
            title="TEST",
        )

        html = str(content.render())

        self.assertHTMLEqual(
            html,
            '<a href="http://example.com" class="btn btn-primary">TEST</a>',
        )

    def test_align_center(self):
        content = PageButtonContent.objects.create(
            parent=self.page,
            region="main",
            url="http://example.com",
            style="btn-secondary",
            title="TEST2",
            align="center",
        )

        html = str(content.render())

        self.assertHTMLEqual(
            html,
            '<p class="text-center btn-center-wrapper">'
            '<a href="http://example.com" class="btn btn-secondary">TEST2</a>'
            "</p>",
        )

    def test_align_left(self):
        content = PageButtonContent.objects.create(
            parent=self.page,
            region="main",
            url="http://example.com",
            style="btn-secondary",
            title="TEST3",
            align="left",
        )

        html = str(content.render())

        self.assertHTMLEqual(
            html,
            '<a href="http://example.com" class="btn btn-secondary float-start">TEST3</a>',  # noqa: E501
        )

    def test_align_right(self):
        content = PageButtonContent.objects.create(
            parent=self.page,
            region="main",
            url="http://example.com",
            style="btn-secondary",
            title="TEST4",
            align="right",
        )

        html = str(content.render())

        self.assertHTMLEqual(
            html,
            '<a href="http://example.com" class="btn btn-secondary float-end">TEST4</a>',  # noqa: E501
        )

    def test_align_block(self):
        content = PageButtonContent.objects.create(
            parent=self.page,
            region="main",
            url="http://example.com",
            style="btn-secondary",
            title="TEST5",
            align="block",
        )

        html = str(content.render())

        self.assertHTMLEqual(
            html,
            '<a href="http://example.com" class="btn btn-secondary d-block w-100">TEST5</a>',  # noqa: E501
        )

    def test_object(self):
        content = PageButtonContent.objects.create(
            parent=self.page,
            region="main",
            url="http://example.com",
            style="btn-secondary",
            title="TEST-STR",
        )

        assert str(content) == "TEST-STR"

    def test_get_absolute_url(self):
        content = PageButtonContent.objects.create(
            parent=self.page,
            region="main",
            url="http://example.com",
            style="btn-secondary",
            title="TEST-URL",
        )

        assert content.get_absolute_url() == "http://example.com"
