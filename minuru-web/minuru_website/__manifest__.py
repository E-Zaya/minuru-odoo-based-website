{
    'name': 'Minuru Website',
    'version': '17.0.1.0.0',
    'summary': 'Minuru Motors — Mongolian expedition website',
    'category': 'Website',
    'author': 'Minuru Motors',
    'website': 'https://www.minururental.com',
    'depends': ['website'],
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'minuru_website/static/src/scss/variables.scss',
            'minuru_website/static/src/scss/theme.scss',
            'minuru_website/static/src/js/theme.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
