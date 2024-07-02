from django.core.mail import send_mail

send_mail(
    "probar",
    "Hola",
    "aleceduardoortizcordova@gmail.com",
    ["ortizalec350@gmail.com"],
    fail_silently=False
)


