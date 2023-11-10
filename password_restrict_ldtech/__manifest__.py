
{
    'name': 'Restrict Password - [Sign Up / Reset Password]',
    "version": "17.0.1",
    'summary': """Put Restrictions during Signup / Reset from webpage - [Sign Up / Reset Password]""",
    'category': 'Tools',
    "license": "LGPL-3",
    'sequence': -100,
    'description': """This Module have the functionality by which user can control their password during
        Signup / Reset password.
        Password must following Pattern : 
            * Passsword must be 8 characters or more.
            * atleast 1 Numeric number
            * atleast 1 Alphabatic letter""",
    'author': "Livedigital Technologies Private Limited",
    'website': "ldtech.in",
    'depends': ['website','auth_signup'],
    'data': [
        'views/assets.xml',
    ],
    'bootstrap': True,
    'assets': {
        'web.assets_frontend': [
            'password_restrict_ldtech/static/**/*',
        ],
    },
    'demo': [],
    'images': ['static/description/icon.png'],
    'application': True,
    'auto_install': False,
    'licence': 'LGPL-3',
    'live_test_url' : 'https://www.yYra14IxmFY4outube.com/watch?v=',
}