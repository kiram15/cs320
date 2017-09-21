import re
def fun(s):
    return bool(re.match(r"[A-Za-z0-9-_]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$", s))
    
def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails
