from django.db.models import Manager, QuerySet


class LogicalQuerySet(QuerySet):
    def delete(self):
        return super().update(is_deleted=True)

    def undelete(self):
        return super().update(is_deleted=False)


class LogicalManager(Manager):
    __queryset = {}

    def get_queryset_object(self):
        if not self.__class__.__queryset.get(self.model.__name__, None):
            self.__class__.__queryset[self.model.__name__] = LogicalQuerySet(self.model)

        return self.__class__.__queryset[self.model.__name__]

    def get_queryset(self):
        return self.get_queryset_object().filter(is_deleted=False)

    def deleted(self):
        return self.get_queryset_object().filter(is_deleted=True)

    def archive(self):
        return self.get_queryset_object()
