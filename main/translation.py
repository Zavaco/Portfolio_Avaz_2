from modeltranslation.translator import translator, TranslationOptions
from .models import *


class PageTranslationOptions(TranslationOptions):
    fields = (
        'my_name',
        'my_info',
        'icon2_info',
        'f_name',
        'icon_info',
        'l_name',
        'message',
        'btn',

    )


translator.register(Page, PageTranslationOptions)


class MenuTranslationOptions(TranslationOptions):
    fields = (
        'menu_name',
    )


translator.register(Menu, MenuTranslationOptions)