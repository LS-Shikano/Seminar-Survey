from os import environ
import custom_python.get_config as cf

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
    normal_redirect_link="https://mingle.respondi.com/s/1608318/ospe.php3?c_0002=1&return_tic=",
    screen_out_redirect_link="https://survey.maximiles.com/screenout?p=89808_546de779&m=",
    quota_redirect_link="https://survey.maximiles.com/quotasfull?p=89808_d7bfcc1a&m=",
    quota_screenout=True,
)

SESSION_CONFIGS = [
    dict(
        name='seminar_survey',
        display_name='Seminar Survey',
        num_demo_participants=10,
        app_sequence=['StartApp', 'SocialmediaApp', 'MobilizationApp', 'CandidateApp', 'EndApp'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

PARTICIPANT_FIELDS = [
    "b_group",
    "federal_state",
    "eligible",
    "gender",
    "age_group",
    "quota",
    "screen_out",
]

SESSION_FIELDS = (
    list(
        map(
            lambda i: f"completed_gender_{i}", range(len(cf.prep_gender_ch) - 1)
        )
    )
    + list(map(lambda i: f"completed_age_group_{i}", range(len(cf.age_groups))))
    + list(
        map(
            lambda i: f"completed_federal_state_{i}",
            range(len(cf.prep_federal_state_ch) - 1),
        )
    )
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '9956250561456'
