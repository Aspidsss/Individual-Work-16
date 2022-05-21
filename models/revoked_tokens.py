from app import db, jwt


class RevokedToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(self, decrypted_token):
        return bool(
            RevokedToken.query.filter_by(jti=decrypted_token['jti']).first()
        )