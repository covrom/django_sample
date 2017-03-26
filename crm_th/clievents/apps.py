from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class ClieventsConfig(ModuleMixin, AppConfig):
    """Продажи театра"""
    name = 'clievents'
    verbose_name = "Продажа спектаклей"
    icon = '<i class="material-icons">call</i>'
