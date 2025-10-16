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
                        "link": reverse_lazy("admin:auth_user_changelist"),  # Changed
                        "title": _("Users"),
                        "icon": "person",
                        "permission": lambda request: request.user.is_authenticated,
                    },
                    {
                        "link": reverse_lazy("admin:auth_group_changelist"),  # Changed
                        "title": _("Groups"),  # Changed from "Roles"
                        "icon": "admin_panel_settings",
                        "permission": lambda request: request.user.is_authenticated,
                    },
                ],
            },
        ],
    },
}
