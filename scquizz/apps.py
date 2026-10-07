from django.apps import AppConfig

class ScquizzConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scquizz'
    verbose_name = 'SCQuizz'
    
    # Landing page metadata
    landing_url = '/scquizz/'
    landing_icon = '/static/core/scquizz.svg'
    landing_description = 'ส่งคำถามและตอบโพลแบบเรียลไทม์ระหว่างกิจกรรม'
