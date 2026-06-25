report = """
=================================
PASSWORD SECURITY AUDIT REPORT
=================================

Weak Passwords Found : 5

Risk Level : MEDIUM

Recommendations:
- Use 12+ characters
- Enable MFA
- Avoid common passwords
"""

file = open("audit_report.txt", "w")
file.write(report)
file.close()

print("Report Generated Successfully") Password Cracking & Credential Attack Suite