class ActivityRouter:
    default_db = "default"
    activity_db = "activity"

    def __processor(self, model):
        if model._meta.model_name == 'useractivity':
            return self.activity_db
        return None

    def db_for_read(self, model, **hints):
        return self.__processor(model)

    def db_for_write(self, model, **hints):
        return self.__processor(model)

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name == 'useractivity' or obj2._meta.model_name == 'useractivity':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'useractivity':
            return db == self.activity_db
        return db == self.default_db
