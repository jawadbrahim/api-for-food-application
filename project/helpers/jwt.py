import jwt

class JwtHelpers:
     def __init__(self, secret, algorithm):
        self.secret = secret
        self.algorithm = algorithm

     def encode(self, payload):
        encoded_jwt = jwt.encode(payload, self.secret, algorithm=self.algorithm)
        return encoded_jwt

     def decode(self, encoded_jwt):
        payload = jwt.decode(encoded_jwt, self.secret, algorithms=[self.algorithm])
        return payload