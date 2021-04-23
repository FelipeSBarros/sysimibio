from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from djgeojson.fields import PointField
from sysimibio.imibio_tree_ecological_data.validators import validate_date, validate_temperature, validate_humidity, \
    validate_lat, validate_lon, tree_height_validation


class TreeEcologicalData(models.Model):
    date = models.DateField(verbose_name='fecha', validators=[validate_date], help_text='ej.: AAAA-MM-DD')
    start_time = models.TimeField(verbose_name='hora_inicio', help_text='ej.: 12:30')
    end_time = models.TimeField(verbose_name='hora_final', help_text='ej.: 13:00')
    temperature = models.FloatField(verbose_name='temperatura', validators=[validate_temperature], help_text='°C')
    humidity = models.FloatField(verbose_name='humedad', validators=[validate_humidity], help_text='%')
    coordinator = models.ForeignKey(User, verbose_name='responsable', max_length=100, on_delete=models.CASCADE)
    staff = models.ManyToManyField(User, related_name='staff', verbose_name='acompanantes',
                                   max_length=100)
    parcel_id = models.IntegerField(verbose_name='ID parcela')  # TODO should be ForeignKey?
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    last_modification_at = models.DateTimeField(verbose_name='Ultima modificación', auto_now=True)

    class Meta:
        verbose_name_plural = 'Registro de campo'
        verbose_name = 'Campo'
        ordering = ('-date', )

    def __str__(self):
        return f'{self.date} {self.coordinator}'


class Pictures(models.Model):
    picture = models.ImageField(verbose_name="Fotografía", null=True, blank=True, help_text='Choose foto')

    class Meta:
        verbose_name = 'Fotografía'
        verbose_name_plural = 'Fotografías'


class Tree(models.Model):
    EMERGENTE = 'Emergente'
    DOMINANTE = 'Dominante'
    CODOMINANTE = 'Codominante'
    INTERMEDIA = 'Intermedia'
    INFERIOR_SUPRIMIDO = 'Inferior suprimido'
    INFERIOR_SUMERGIDO = 'Inferior sumergido'
    SOCIOLOGICAL_CLASSIFICATION_CHOICES = [
        (EMERGENTE, 'Emergente'),
        (DOMINANTE, 'Dominante'),
        (CODOMINANTE, 'Codominante'),
        (INTERMEDIA, 'Intermedia'),
        (INFERIOR_SUPRIMIDO, 'Inferior Suprimido'),
        (INFERIOR_SUMERGIDO, 'Supeior Sumergido'),
    ]

    BUENO = 'Bueno'
    REGULAR = 'Regular'
    MALO = 'Malo'
    MUERTO = 'Muerto'
    PHYTOSANITARY_STATUS_CHOICES = [
        (BUENO, 'Bueno'),
        (REGULAR, 'Regular'),
        (MALO, 'Malo'),
        (MUERTO, 'Muerto')
    ]

    field = models.ForeignKey('TreeEcologicalData', on_delete=models.CASCADE)  # ao deletar um registro de campo os dados de arvore tbm o serao
    tree_id = models.IntegerField(verbose_name='ID Árbol')
    specie = models.CharField(verbose_name='Nombre especie', max_length=100)
    dap = models.FloatField(help_text='cm')  # todo dap y dab se miden cuando el arbol tiene altura mayor a 1.3 metros
    dab = models.FloatField(help_text='cm')  # todo dap y dab se miden cuando el arbol tiene altura mayor a 1.3 metros
    tree_height = models.FloatField(verbose_name='Altura del árbol', help_text='m', validators = [tree_height_validation])
    latitude = models.FloatField(verbose_name='latitud', validators=[validate_lat])  # todo add aclaración de que se esta usando WSG84
    longitude = models.FloatField(verbose_name='longitud', validators=[validate_lon])
    picture = models.ForeignKey(Pictures, on_delete=models.CASCADE, blank=True, null = True)
    obs = models.TextField(verbose_name="Observaciones", blank=True)
    phytosanitary_status = models.CharField(max_length=100,
                                            choices=PHYTOSANITARY_STATUS_CHOICES,
                                            default=BUENO)
    sociological_classification = models.CharField(verbose_name='clasificación sociologica',
                                                   max_length=100,
                                                   choices=SOCIOLOGICAL_CLASSIFICATION_CHOICES,
                                                   default=EMERGENTE)
    geom = PointField(blank=True)

    class Meta:
        verbose_name = 'Árbol'
        verbose_name_plural = 'Árboles'

    def __str__(self):
        return f'{self.specie} {self.field.date}'

    def save(self, *args, **kwargs):
        self.geom = {'type': 'Point', 'coordinates': [self.longitude, self.latitude]}
        super(Tree, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('imibio_tree_ecological_data:detail', kwargs={'pk': self.pk})

    @property
    def popup_content(self): # todo Me parece que lo importante es poner alguna foto
        popup = "<strong><span>Nombre científico: </span>{}</strong></p>".format(
            self.specie)
        popup += "<span>Condición fitosanitario: </span>{}<br>".format(
            self.phytosanitary_status)
        popup += "<span>Altura: </span>{}<br>".format(
            self.tree_height)
        popup += f"<span><a href={self.get_absolute_url()}>Detalles de la occurrencia</a></strong><br>"
        return popup
