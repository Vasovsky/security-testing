import unittest
from zapv2 import ZAPv2

class TestSecurity(unittest.TestCase):

    def setUp(self):
        # Make sure ZAP is running and listening on the correct port
     self.zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}, apikey='YOUR_API_KEY_HERE')



    def test_no_high_risk_vulnerabilities(self):
        target = 'http://example.com'
        alerts = self.zap.core.alerts(baseurl=target)
        high_risk_alerts = [alert for alert in alerts if alert['risk'] == 'High']
        self.assertEqual(len(high_risk_alerts), 0, "Found high-risk vulnerabilities")

if __name__ == "__main__":
    unittest.main()
