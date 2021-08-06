import unittest
import json

from create_email_from_json import create_email_response
from order import JsonOrder

unittest.util._MAX_LENGTH=2000

class TestCreateEmailResponse(unittest.TestCase):
    maxDiff = None

    def test_email_response(self):
        expected = 'Sehr geehrte Kundin / Kunde\n\nDie Bestellung mit Ordnungsnummer 9703940734 hat jetzt folgende Positionen: alle.\nEndlieferung wurde gesetzt.\nEndrechnung wurde gesetzt.\nBestellung ist jetzt geschlossen.\n\nDie Bestellung mit Ordnungsnummer 9704688505 hat jetzt folgende Positionen: alle.\nEndlieferung wurde gesetzt.\nEndrechnung wurde gesetzt.\nBestellung ist jetzt geschlossen.\n\nVielen dank'
        input_data = '{"orders": [{"PO": "9703940734", "Positions": ["alle"], "Action": "Close", "Type": ["elk", "erk"]}, {"PO": "9704688505", "Positions": ["alle"], "Action": "Close", "Type": ["elk", "erk"]}]}'
        json_data = json.loads(input_data)
        orders = [JsonOrder(order) for order in json_data["orders"]]
        actual = create_email_response(orders)
        self.assertEqual(actual, expected)

    def test_error_response(self):
        expected = 'Sehr geehrte Kundin / Kunde\n\nleider haben wir keine gültige Produktbestellungnummern von Ihnen erhalten.\nEin Produktbestellungnummer besteht aus 10-stelligem Ziffer.\nBitte beprüfen Sie nochmal Ihre Produktbestellung.\n\nVielen dank'
        actual = create_email_response([])
        self.assertEqual(actual, expected)

