from tinymce.models import HTMLField 
from django.db import models 
""" ������ ������ about_us """
class about_us(models.Model):
      name = models.CharField(&nbsp; &nbsp; &nbsp;max_length = 64, blank=True, &nbsp; null=True, default='None', verbose_name= ' ')
      description = HTMLField(&nbsp; &nbsp; &nbsp;&nbsp; blank=True, &nbsp; null=True, default='None', verbose_name='��������')
      icon = models.CharField(&nbsp; &nbsp; &nbsp;max_length = 64, blank=True, &nbsp; null=True, default='None', verbose_name='������ � fontawesome.com')
      is_active = models.BooleanField(&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; default=True, verbose_name='�������� �� �������?')
      def __str__(self):
        return "���������� � ���: %s" % (self.name)
      class Meta:
        verbose_name = "���������� � ���"
        verbose_name_plural = "����������"
""" ������ ������ Post_categories """
class Post_categories(models.Model):
      name = models.CharField(&nbsp; &nbsp; &nbsp;max_length = 64, blank=True, &nbsp; null=True, default='None', verbose_name= '��� ��������� � ��������� ')
      description = HTMLField(&nbsp; &nbsp; &nbsp;&nbsp; blank=False, &nbsp; null=True, default='None', verbose_name= '�������� ��������� ���� ����� ��������� ����� ������ � html ')
      image = models.ImageField(&nbsp; &nbsp; &nbsp;blank=True, &nbsp; , upload_to='static/media/categories_images/', help_text = '��������� ���� ����������� ��� ��������� ��� ����� � ������� ���������', &nbsp; verbose_name= ' ������� ����������� ��� ���������')
      is_active = models.BooleanField(&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; default='True', verbose_name= '���? ')
      def __str__(self):
        return "���������: %s" % (self.name)
      class Meta:
        verbose_name = "���������"
        verbose_name_plural = "���������"
