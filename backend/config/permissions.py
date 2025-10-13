from django.apps import apps


def get_permission_check(app_label, model_name):
    # Checks whether user has view permission for any specific app model
    perm_name = f"{app_label}.view_{model_name}"
    return lambda request: request.user.has_perm(perm_name)


def get_permissions_for_app(app_label):
    # Checks for 'view' permissions on all models in an app.
    def check_perms(request):
        try:
            app_config = apps.get_app_config(app_label)
            for model in app_config.get_models():
                perm_name = f"{app_label}.view_{model._meta.model_name}"
                if request.user.has_perm(perm_name):
                    return True
        except LookupError:
            pass
        return False

    return check_perms
