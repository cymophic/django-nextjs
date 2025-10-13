from config.permissions import get_permission_check, get_permissions_for_app
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "Site Admin",
    "SITE_HEADER": "Site Admin",
    "SITE_SUBHEADER": "Django Admin Panel",
    "THEME": "light",
    "SITE_URL": "/",
    "COLORS": {
        "primary": {
            "50": "#fafafa",
            "100": "#f5f5f5",
            "200": "#e5e5e5",
            "300": "#d4d4d4",
            "400": "#a3a3a3",
            "500": "#737373",
            "600": "#525252",
            "700": "#404040",
            "800": "#262626",
            "900": "#171717",
            "950": "#0a0a0a",
        },
    },
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("favicon/favicon-light.ico"),
        },
    ],
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": _("Overview"),
                "items": [
                    {
                        "link": reverse_lazy("admin:index"),
                        "title": _("Dashboard"),
                        "icon": "dashboard",
                        "permission": lambda request: request.user.is_authenticated,
                    },
                ],
            },
            {
                "title": _("Users & Roles"),
                "collapsible": True,
                "permission": lambda request: request.user.is_superuser,
                "items": [
                    {
                        "link": reverse_lazy("admin:users_customuser_changelist"),
                        "title": _("Users"),
                        "icon": "person",
                        "permission": get_permission_check("users", "customuser"),
                    },
                    {
                        "link": reverse_lazy("admin:users_role_changelist"),
                        "title": _("Roles"),
                        "icon": "admin_panel_settings",
                        "permission": get_permission_check("users", "role"),
                    },
                ],
            },
            {
                "title": _("System Settings"),
                "collapsible": True,
                "permission": get_permissions_for_app("sites"),
                "items": [
                    {
                        "link": reverse_lazy("admin:sites_site_changelist"),
                        "title": _("Sites"),
                        "icon": "web",
                        "permission": get_permission_check("sites", "site"),
                    },
                ],
            },
        ],
    },
}
