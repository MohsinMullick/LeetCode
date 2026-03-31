class Solution:
    def numUniqueEmails(self, emails):
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            # Ignore everything after '+'
            if '+' in local:
                local = local[:local.index('+')]
            # Remove all '.'
            local = local.replace('.', '')
            # Reconstruct email
            clean_email = local + '@' + domain
            unique_emails.add(clean_email)
        return len(unique_emails)