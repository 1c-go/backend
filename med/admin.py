from reversion.admin import VersionAdmin

from main.admin import admin_site
from .models.patient import Patient
from .models.specialization import Specialization
from .models.doctor import Doctor
from .models.hospital import Hospital
from .models.record import Record
from .models.division import Division
from .models.position import Position


admin_site.register(Patient)
admin_site.register(Specialization)
admin_site.register(Doctor)
admin_site.register(Hospital)
admin_site.register(Record)
admin_site.register(Division)
admin_site.register(Position)
