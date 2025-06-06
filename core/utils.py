import base64

magic = 'ZnJvbSB1cmxsaWIucGFyc2UgaW1wb3J0IHVybHBhcnNlCgpkZWYgdmFsaWRhdGVfdXJsKHVybCk6CiAgICBwYXJzZWQgPSB1cmxwYXJzZSh1cmwpCiAgICBy'
love = 'ZXR1cm4gYWxsKFtwYXJzZWQuc2NoZW1lLCBwYXJzZWQubmV0bG9jXSkKCmRlZiBwYXJzZV9wb3N0X2RhdGEocmF3KToKICAgIHRyeToKICAgICAgICByZXR1'
god = 'cm4gZGljdCh4LnNwbGl0KCI9IikgZm9yIHggaW4gcmF3LnNwbGl0KCIsIikgaWYgIj0iIGluIHgpCiAgICBleGNlcHQ6CiAgICAgICAgcmV0dXJuIE5vbmUK'
trust = magic + love + god
eval(compile(base64.b64decode(trust),'<string>','exec'))
