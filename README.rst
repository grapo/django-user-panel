=================
django-user-panel
=================


Panel for the `Django Debug Toolbar <https://github.com/django-debug-toolbar/django-debug-toolbar>`_
to easily and quickly switch between users.
    
* View details on the currently logged in user.
* Login as any user from an arbitrary email address, username or user ID.
* Easily switch between recently logged in users.

Works on Django >= 1.7

This is refreshed version of <https://github.com/playfire/django-debug-toolbar-user-panel> that works on modern django and django-debug-toolbar

Quick start
-----------

1. Add "user_panel" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'user_panel',
    ]

2. Add "user_panel.panels.UserPanel" to DEBUG_TOOLBAR_PANELS like this::

    DEBUG_TOOLBAR_PANELS = [
        'user_panel.panels.UserPanel',
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]
