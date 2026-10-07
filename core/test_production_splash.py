from unittest.mock import patch
from django.test import SimpleTestCase, override_settings


class ProductionSplashTests(SimpleTestCase):
    @override_settings(PRODUCTION_SPLASH_ENABLED=True)
    def test_production_home_does_not_need_app_database(self):
        with patch('core.views.get_installed_user_apps') as apps:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'core/production_splash.html')
            self.assertContains(response, 'aria-label="Duck Project"')
            self.assertContains(response, '>DUCK</span>')
            self.assertContains(response, '>PROJECT</span>')
            self.assertContains(response, '/static/core/production-splash.js')
            self.assertNotContains(response, 'portal-nav')
            apps.assert_not_called()

    @override_settings(PRODUCTION_SPLASH_ENABLED=False)
    def test_worktree_keeps_portal(self):
        with patch('core.views.get_installed_user_apps', return_value=[]):
            response = self.client.get('/')
            self.assertTemplateUsed(response, 'core/landing.html')
            self.assertContains(response, 'portal-nav')

    def test_self_hosted_assets(self):
        for filename, content_type in [('production-splash.js', 'application/javascript'),
                ('fonts/outfit-800.ttf', 'font/ttf'),
                ('brand/duckproject-square-color.svg', 'image/svg+xml')]:
            response = self.client.get('/static/core/' + filename)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response['Content-Type'], content_type)
            self.assertTrue(b''.join(response.streaming_content))
