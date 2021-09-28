MEDIA_URL =  '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)