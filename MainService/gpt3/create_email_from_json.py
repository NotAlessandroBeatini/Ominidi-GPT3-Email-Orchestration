def create_email_response(orders):
    body = [summarize(order) for order in orders] if orders else [ERROR_MESSAGE]
    return '\n\n'.join(("Sehr geehrte Kundin / Kunde", *body, 'Vielen dank'))

def summarize(order):
    resp = [
    f'Die Bestellung mit Ordnungsnummer {order.po} hat jetzt folgende Positionen: {order.positions}.']
    if "elk" in order.categories:
        resp.append('Endlieferung wurde gesetzt.')
    if "erk" in order.categories:
        resp.append('Endrechnung wurde gesetzt.')
    resp.append('Die Bestellung ist immer noch offen.' if order.is_open else 'Bestellung ist jetzt geschlossen.')

    return '\n'.join(resp)

ERROR_MESSAGE = """leider haben wir keine gueltige Produktbestellungnummern von Ihnen erhalten.
Ein Produktbestellungnummer besteht aus 10-stelligem Ziffer.
Bitte bepruefen Sie nochmal Ihre Produktbestellung."""
