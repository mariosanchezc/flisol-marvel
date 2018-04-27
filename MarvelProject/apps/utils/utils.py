def user_directory_path(instance, filename):
    """
    tomado de la página oficial de django
    https://docs.djangoproject.com/en/2.0/ref/models/fields/
    """
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
