from material.frontend.views import ModelViewSet

from . import models


class SpectacleViewSet(ModelViewSet):
    model = models.Spectacle

