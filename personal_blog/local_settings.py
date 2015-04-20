__author__ = 'lb'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '90!*dn*p$-0^(xguvo9c9sl4q@0*(^)uyhl2fs!z_6wta6#)bh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

###---< Email Settings >---###
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'lbrambrink@gmail.com'
EMAIL_HOST_PASSWORD = 'Conditioner124124'