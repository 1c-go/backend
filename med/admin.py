from django.contrib.admin import ModelAdmin, register, StackedInline, TabularInline

from main.admin import admin_site
from .models.patient import Patient
from .models.specialization import Specialization
from .models.doctor import Doctor
from .models.hospital import Hospital
from .models.record import Record
from .models.division import Division
from .models.position import Position
from .models.question import Question
from .models.answer import Answer


class RecordTable(TabularInline):
    model = Record
    show_change_link = True
    readonly_fields = ('id', 'status', 'hospital', 'specialization', 'doctor', 'opened_at',
                       'recording_at', 'closed_at', 'title')
    fields = readonly_fields
    classes = ('collapse',)
    extra = 0


class DivisionTable(TabularInline):
    model = Division
    show_change_link = True
    fields = ('id', 'name')
    classes = ('collapse',)
    extra = 0


class PositionTable(TabularInline):
    model = Position
    show_change_link = True
    classes = ('collapse',)
    fields = ('id', 'doctor', 'specialization')
    extra = 0


class PositionTableDoctor(TabularInline):
    model = Position
    show_change_link = True
    classes = ('collapse',)
    fields = ('id', 'division', 'specialization')
    extra = 0


class AnswerTable(TabularInline):
    model = Answer
    classes = ('collapse',)
    fields = ('id', 'question', 'answer')
    readonly_fields = fields
    extra = 0


@register(Patient, site=admin_site)
class PatientAdmin(ModelAdmin):
    list_display = ('id', 'user', 'default_hospital')
    search_fields = ('user__full_name', 'default_hospital__name')
    inlines = (RecordTable,)


@register(Specialization, site=admin_site)
class SpecializationAdmin(ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@register(Doctor, site=admin_site)
class DoctorAdmin(ModelAdmin):
    list_display = ('id', 'full_name')
    search_fields = ('full_name',)
    inlines = (PositionTableDoctor,)


@register(Hospital, site=admin_site)
class HospitalAdmin(ModelAdmin):
    list_display = ('id', 'name', 'address')
    search_fields = ('name', 'address')
    inlines = (DivisionTable,)


@register(Record, site=admin_site)
class RecordAdmin(ModelAdmin):
    list_display = ('id', 'status', 'patient', 'hospital', 'specialization', 'doctor', 'opened_at',
                    'recording_at', 'closed_at', 'title')
    list_filter = ('status', 'hospital', 'specialization')
    search_fields = ('title', 'description')
    date_hierarchy = 'opened_at'
    inlines = (AnswerTable,)


@register(Division, site=admin_site)
class DivisionAdmin(ModelAdmin):
    list_display = ('id', 'name', 'hospital')
    list_filter = ('hospital',)
    search_fields = ('name', 'hospital__name')
    inlines = (PositionTable,)


@register(Position, site=admin_site)
class PositionAdmin(ModelAdmin):
    list_display = ('id', 'doctor', 'division', 'specialization')
    list_filter = ('doctor', 'division', 'specialization')
    search_fields = ('doctor__full_name', 'division__name', 'specialization__name')


@register(Question, site=admin_site)
class QuestionAdmin(ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'hospital', 'positive_answer')
    list_filter = ('specialization', 'hospital', 'positive_answer')
    search_fields = ('name', 'specialization__name', 'hospital__name')


@register(Answer, site=admin_site)
class AnswerAdmin(ModelAdmin):
    list_display = ('id', 'record', 'question', 'answer')
    list_filter = ('record', 'question', 'answer')
    search_fields = ('question__name',)
