# Simulate DB being available and not available from test
from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
# To Simulate the unavailablity of DB
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        # Test waiting for DB when DB is available
        # Override the behaviour of connection
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # Mocking behaviour using patch
            gi.return_value = True
            call_command('wait_for_db')
            # Name of Management command we give
            self.assertEqual(gi.call_count, 1)

    # To remove the delay from time sleep while testing
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        # Test Waiting for DB
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # add Side effect for the above operation for 5 times and return
            # true 6th time
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
