from django.utils.translation import gettext as _
from core.constants import OTHER

IDENTITY_TYPES = (
    ('country_id', 'Country ID number'),
    ('passport', 'Passport'),
    ('birth_certificate', 'Birth Certificate'),
    (OTHER, _('Other')),
)

HIGHEST_QUALIFICATIONS = (
    ('None', 'None'),
    ('primary', 'Primary'),
    ('junior_secondary', 'Junior Secondary'),
    ('senior_Secondary', 'Senior Secondary'),
    ('diploma', 'Diploma'),
    ('graduate_certificate', 'Graduate certificate'),
    ('associates_degree', 'Associates degree'),
    ('graduate_diploma', 'Graduate diploma'),
    ('tertiary', 'Tertiary'),
    ('bachelor_degree', 'Bachelor degree'),
    ('masters_degree', 'Masters degree'),
    ('doctoral_degree', 'Doctoral degree'),
    ('phd', 'PhD'),
    ('postdoctoral', 'Postdoctoral')
)
