from django.urls import reverse

from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
from jet.dashboard import modules


class DefaultIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)

        self.children.append(modules.AppList(
            'Приложения',
            exclude=('auth.*',),
            column=1,
            order=0
        ))

        self.children.append(modules.AppList(
            'Администрирование',
            models=('auth.*',),
            column=0,
            order=0
        ))

        self.children.append(modules.RecentActions(
            'Последние действия',
            10,
            column=2,
            order=1
        ))


class DefaultAppIndexDashboard(AppIndexDashboard):
    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)

        self.children.append(modules.ModelList(
            title='Модели приложения',
            models=self.models(),
            column=0,
            order=0
        ))
        self.children.append(modules.RecentActions(
            include_list=self.get_app_content_types(),
            column=1,
            order=0
        ))
