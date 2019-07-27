from rest_framework import renderers


class JsonUnicodeRenderer(renderers.JSONRenderer):
    charset = 'utf-8'
