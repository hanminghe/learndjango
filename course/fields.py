from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):
    def __init__(self,for_fields=None, *args, **kargs):
        self.for_fields=for_fields
        print('1',for_fields)
        super(OrderField,self).__init__(*args,**kargs)

    def pre_save(self,model_instance,add):
        if getattr(model_instance,self.attname) is None:
            print('2',self.attname)
            try:
                qs=self.model.objects.all()
                if self.for_fields:
                    query={ field: getattr(model_instance,field) \
                                for field in self.for_fields }
                    qs=qs.filter(**query)
                last_item=qs.latest(self.attname)
                value=last_item.order+1
            except ObjectDoesNotExist:
                value=0
            setattr(model_instance,self.attname,value)
            return value
        else:
            print('3')
            return super(OrderField,self).pre_save(model_instance,add)

    def get_attname_column(self):
        attname=self.get_attname()
        print('4',self.db_column,attname)
        column=self.db_column or attname
        return attname,column

    def set_attributes_from_name(self,name):
        if not self.name:
            self.name=name
            self.attname,self.column=self.get_attname_column()
            self.concrete=self.column is not None
        if self.verbose_name is None and self.name:
            self.verbose_name=self.name.replace('_','')

        print( self.concrete, self.verbose_name)
