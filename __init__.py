def object_type(name):
    def decorator(cls):
        cls.object_type = name
        return cls
    return decorator


@object_type('backend')
class backend:
    pass
