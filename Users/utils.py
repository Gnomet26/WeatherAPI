from rest_framework import serializers

#=========== const variables =========
MIN_LEN_PASSWORD = 4
#=====================================


def validate_serilizers_data(attrs):

    username = attrs.get('username')
    first_name = attrs.get('first_name')
    last_name = attrs.get('last_name')
    password = attrs.get('password')

    if not username:
        return 'Username maydonini kiritish majburiy'
    if not first_name:
        return 'Ismingiz maydonini kiritish majburiy'
    if not last_name:
        return 'Familyangiz maydonini kiritish majburiy'
    if not password:
        return 'Parol maydonini kiritish majburiy'
    if len(str(password).replace(" ","")) < MIN_LEN_PASSWORD:
        return 'Parol kamida 8 ta belgidan iborat bo`lishi kerak '
    return 'Test Ok'
