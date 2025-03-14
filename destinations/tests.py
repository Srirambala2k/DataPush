from django.test import TestCase
from .models import Destination
from accounts.models import Account
class DestinationModelTests(TestCase):
        def setUp(self):
                self.account = Account.objects.create(            
                    account_name='Test Account',
                    app_secret_token='testtoken', 
                    website='https://example.com',
                    )
                self.destination = Destination.objects.create( 
                            account=self.account,
                                url='https://api.example.com',
                                http_method='GET',
                                headers={'Authorization': 'Bearer token'},
                                created_by='testuser',
                                updated_by='testuser'
                                )    
        def test_create_destination(self):
                        # Test destination creation
                self.assertEqual(self.destination.account, self.account)
                self.assertEqual(self.destination.url, 'https://api.example.com')
                self.assertEqual(self.destination.http_method, 'GET')
                self.assertEqual(self.destination.headers, {'Authorization': 'Bearer token'})
                self.assertEqual(self.destination.created_by, 'testuser')        
                self.assertEqual(self.destination.updated_by, 'testuser')
        def test_update_destination(self):
                    # Test destination update
                self.destination.url = 'https://api.updated.com'
                self.destination.http_method = 'POST'
                self.destination.save()
                self.assertEqual(self.destination.url, 'https://api.updated.com')
                self.assertEqual(self.destination.http_method, 'POST')

        def test_delete_destination(self):
            # Test destination deletion
            destination_id = self.destination.id
            self.destination.delete()
            with self.assertRaises(Destination.DoesNotExist):
                Destination.objects.get(id=destination_id)
