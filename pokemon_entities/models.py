from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name="название(рус.)")
    title_en = models.CharField(
        max_length=200, blank=True, verbose_name="название(англ.)"
    )
    title_jp = models.CharField(
        max_length=200, blank=True, verbose_name="название(яп.)"
    )
    image = models.ImageField(verbose_name="картинка")
    description = models.TextField(blank=True, verbose_name="описание")
    appeared_at = models.DateTimeField(
        null=True, blank=True, verbose_name="время появления"
    )
    disappeared_at = models.DateTimeField(
        null=True, blank=True, verbose_name="время исчезновения"
    )
    level = models.IntegerField(null=True, blank=True, verbose_name="уровень")
    health = models.IntegerField(null=True, blank=True, verbose_name="здоровье")
    strength = models.IntegerField(null=True, blank=True, verbose_name="атака")
    defence = models.IntegerField(null=True, blank=True, verbose_name="защита")
    stamina = models.IntegerField(
        null=True, blank=True, verbose_name="выносливость"
    )
    previous_evolution = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="next_evolutions",
        on_delete=models.CASCADE,
        verbose_name="из кого эволюционировал",
    )

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        related_name="entities",
        on_delete=models.CASCADE,
        verbose_name="покемон",
    )
    lat = models.FloatField(verbose_name="широта")
    lon = models.FloatField(verbose_name="долгота")
