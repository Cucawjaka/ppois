class Cryptography:
    @staticmethod
    def encode_str(secret: str) -> str:
        return "secret" + secret

    @staticmethod
    def decode_str(secreted: str) -> str:
        return secreted[6:]

    @staticmethod
    def encode_int(secret: int) -> int:
        return secret * 2

    @staticmethod
    def decode_int(secreted: int) -> int:
        return int(secreted / 2)

    @staticmethod
    def verify_int(checking_secret: int, right_secret: int) -> bool:
        return Cryptography.encode_int(checking_secret) == right_secret

    @staticmethod
    def verufy_str(checking_secret: str, right_secret: str) -> bool:
        return Cryptography.encode_str(checking_secret) == right_secret
