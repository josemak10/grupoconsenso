from readline import clear_history
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from .models import Party, Customer

import json

# Create your views here.

class PartyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, type=''):
        if type != '':
            clist = list(Customer.objects.filter(type=type).values())
        else:
            clist = list(Customer.objects.values())
        if clist:
            vlist = [{
                'name': x['name'], 
                'identifier': x['identifier'], 
                'type_identifier': x['type'], 
                'type_customer': x['type_customer']} for x in clist]
            data = {
                'message': 'Success',
                'data': vlist,
            }
        else:
            data = {
                'message': 'No data'
            }
        return JsonResponse( data )

    def post(self, request):
        obj = json.loads(request.body)
        party = Party.objects.create(
            name=obj['name'],
            genre=obj['genre'],
            identifier=obj['identifier'],
            type=obj['type'],
            civil_status=obj['civil_status']
        )
        party.save()
        Customer.objects.create(
            party_ptr = party,
            family_responsibilities=obj['family_responsibilities'],
            type_customer=obj['type_customer'],
            residence_date=obj['residence_date']
        )

        data = {
            'message': 'Success'
        }
        return JsonResponse( data )

    def put(self, request, id):
        obj = json.loads(request.body)
        clist = list(Party.objects.filter(id=id).values())
        if clist:
            new = Party.objects.get(id=id)
            new.name=obj['name']
            new.genre=obj['genre']
            new.identifier=obj['identifier']
            new.type=obj['type']
            new.civil_status=obj['civil_status']
            new.save()
            data = {
                'message': 'Success',
            }
        else:
            data = {
                'message': 'No data'
            }
        return JsonResponse( data )


    def delete(self, request, id):
        clist = list(Party.objects.filter(id=id).values())
        if clist:
            Party.objects.filter(id=id).delete()
            data = {
                'message': 'Success',
            }
        else:
            data = {
                'message': 'No data'
            }
        return JsonResponse( data )
