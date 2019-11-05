from .models import Audit


class Audit_Log():
    @staticmethod
    def log(action, message, user, audit_details):
        audit = Audit()
        audit.action = action
        audit.message = message
        audit.performed_by = user
        audit.audit_details = audit_details
        audit.save()
