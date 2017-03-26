from django.db import models

class Spectacle(models.Model):
    """Спектакли"""
    name = models.CharField("наименование", max_length=250)
    price = models.DecimalField("цена", max_digits=15, decimal_places=2)
    description = models.TextField("описание")
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
        verbose_name = "Спектакль"
        verbose_name_plural = "Спектакли"

# poll = models.ForeignKey(
#     Poll,
#     on_delete=models.CASCADE,
#     verbose_name="the related poll",
# )