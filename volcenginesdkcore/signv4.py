# coding: utf-8

# Copy from https://github.com/volcengine/volc-sdk-python

import datetime
import hmac
import hashlib

try:
    from urllib import quote
except:
    from urllib.parse import quote


class SignerV4(object):

    @staticmethod
    def sign(path, method, headers, body, query, ak, sk, region, service):
        if path == '':
            path = '/'
        if method != 'GET' and not ('Content-Type' in headers):
            headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=utf-8'
        format_date = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        headers['X-Date'] = format_date

        body_hash = hashlib.sha256(body.encode('utf-8')).hexdigest()
        headers['X-Content-Sha256'] = body_hash

        signed_headers = dict()
        for key in headers:
            if key in ['Content-Type', 'Content-Md5', 'Host'] or key.startswith('X-'):
                signed_headers[key.lower()] = headers[key]

        if 'host' in signed_headers:
            v = signed_headers['host']
            if v.find(':') != -1:
                split = v.split(':')
                port = split[1]
                if str(port) == '80' or str(port) == '443':
                    signed_headers['host'] = split[0]

        signed_str = ''
        for key in sorted(signed_headers.keys()):
            signed_str += key + ':' + signed_headers[key] + '\n'

        signed_headers_string = ';'.join(sorted(signed_headers.keys()))

        canonical_request = '\n'.join(
            [method, path, SignerV4.norm_query(query), signed_str,
             signed_headers_string, body_hash])
        credential_scope = '/'.join([format_date[:8], region, service, 'request'])
        signing_str = '\n'.join(['HMAC-SHA256', format_date, credential_scope,
                                 hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()])
        signing_key = SignerV4.get_signing_secret_key_v4(sk, format_date[:8], region, service)

        signature = hmac.new(signing_key, signing_str.encode('utf-8'), hashlib.sha256).hexdigest()

        credential = ak + '/' + credential_scope
        headers[
            'Authorization'] = 'HMAC-SHA256' + ' Credential=' + credential + ', SignedHeaders=' + \
                               signed_headers_string + ', Signature=' + signature
        return

    @staticmethod
    def get_signing_secret_key_v4(sk, date, region, service):
        kdate = SignerV4.hmac_sha256(sk.encode('utf-8'), date)
        kregion = SignerV4.hmac_sha256(kdate, region)
        kservice = SignerV4.hmac_sha256(kregion, service)
        return SignerV4.hmac_sha256(kservice, 'request')

    @staticmethod
    def hmac_sha256(key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

    @staticmethod
    def norm_query(params):
        query = ''
        for key in sorted(params.keys()):
            if type(params[key]) == list:
                for k in params[key]:
                    query = query + quote(key, safe='-_.~') + '=' + quote(k, safe='-_.~') + '&'
            elif type(params[key]) in [int, float, bool]:
                # The argument to urllib.parse.quote must be a string
                ele = str(params[key])
                query = query + quote(key, safe='-_.~') + '=' + quote(ele, safe='-_.~') + '&'
            else:
                query = query + quote(key, safe='-_.~') + '=' + quote(params[key], safe='-_.~') + '&'
        query = query[:-1]
        return query.replace('+', '%20')
