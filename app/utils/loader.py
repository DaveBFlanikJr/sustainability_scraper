import importlib


def loader(profile_id: str):
    try:
        module = importlib.import_module(f"app.site_profiles.{profile_id}")
        return module.profile
    except Exception as e:
        raise ValueError(f"Profile '{profile_id}' could not be loaded: {e}")
