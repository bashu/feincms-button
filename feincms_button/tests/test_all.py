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
            style="btn-default",
            title="TEST2",
            align="center",
        )

        html = str(content.render())

        self.assertHTMLEqual(
            html,
            '<p class="text-center btn-center-wrapper">'
            '<a href="http://example.com" class="btn btn-default">TEST2</a>'
            "</p>",
        )

    def test_align_left(self):
        content = PageButtonContent.objects.create(
            parent=self.page,
            region="main",
            url="http://example.com",
            style="btn-default",
            title="TEST3",
            align="left",
        )

        html = str(content.render())

        self.assertHTMLEqual(
            html,
            '<a href="http://example.com" class="btn btn-default pull-left">TEST3</a>',
        )

    def test_align_right(self):
        content = PageButtonContent.objects.create(
            parent=self.page,
            region="main",
            url="http://example.com",
            style="btn-default",
            title="TEST4",
            align="right",
        )

        html = str(content.render())

        self.assertHTMLEqual(
            html,
            '<a href="http://example.com" class="btn btn-default pull-right">TEST4</a>',
        )

    def test_align_block(self):
        content = PageButtonContent.objects.create(
            parent=self.page,
            region="main",
            url="http://example.com",
            style="btn-default",
            title="TEST5",
            align="block",
        )

        html = str(content.render())

        self.assertHTMLEqual(
            html,
            '<a href="http://example.com" class="btn btn-default btn-block">TEST5</a>',
        )

    def test_object(self):
        content = PageButtonContent.objects.create(
            parent=self.page,
            region="main",
            url="http://example.com",
            style="btn-default",
            title="TEST-STR",
        )

        self.assertEqual(str(content), "TEST-STR")

    def test_get_absolute_url(self):
        content = PageButtonContent.objects.create(
            parent=self.page,
            region="main",
            url="http://example.com",
            style="btn-default",
            title="TEST-URL",
        )

        self.assertEqual(content.get_absolute_url(), "http://example.com")
