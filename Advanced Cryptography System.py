from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
import base64
import os
from typing import Tuple

class AdvancedCryptoSystem:
    def __init__(self):
        self.symmetric_key = None
        self.private_key = None
        self.public_key = None
    
    def generate_symmetric_key(self, password: str, salt: bytes = None) -> bytes:
        if salt is None:
            salt = os.urandom(16)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        self.symmetric_key = key
        return key, salt
    
    def generate_asymmetric_keys(self) -> Tuple[bytes, bytes]:
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
        
        private_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        return private_pem, public_pem
    
    def symmetric_encrypt(self, data: bytes) -> bytes:
        if not self.symmetric_key:
            raise ValueError("Symmetric key not generated")
        
        fernet = Fernet(self.symmetric_key)
        return fernet.encrypt(data)
    
    def symmetric_decrypt(self, encrypted_data: bytes) -> bytes:
        if not self.symmetric_key:
            raise ValueError("Symmetric key not generated")
        
        fernet = Fernet(self.symmetric_key)
        return fernet.decrypt(encrypted_data)
    
    def asymmetric_encrypt(self, data: bytes, public_key_pem: bytes = None) -> bytes:
        public_key = public_key_pem or self.public_key
        if isinstance(public_key, bytes):
            public_key = serialization.load_pem_public_key(public_key)
        
        encrypted = public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted
    
    def asymmetric_decrypt(self, encrypted_data: bytes) -> bytes:
        if not self.private_key:
            raise ValueError("Private key not available")
        
        decrypted = self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted
    
    def create_digital_signature(self, data: bytes) -> bytes:
        if not self.private_key:
            raise ValueError("Private key not available")
        
        signature = self.private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
    
    def verify_signature(self, data: bytes, signature: bytes, public_key_pem: bytes) -> bool:
        public_key = serialization.load_pem_public_key(public_key_pem)
        try:
            public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False
    
    def hybrid_encrypt(self, data: bytes, recipient_public_key: bytes) -> Tuple[bytes, bytes, bytes]:
        # Generate ephemeral symmetric key
        sym_key, salt = self.generate_symmetric_key(os.urandom(32).hex())
        
        # Encrypt data with symmetric key
        encrypted_data = self.symmetric_encrypt(data)
        
        # Encrypt symmetric key with recipient's public key
        encrypted_key = self.asymmetric_encrypt(sym_key, recipient_public_key)
        
        return encrypted_data, encrypted_key, salt
    
    def hybrid_decrypt(self, encrypted_data: bytes, encrypted_key: bytes, salt: bytes) -> bytes:
        # Decrypt symmetric key with private key
        sym_key = self.asymmetric_decrypt(encrypted_key)
        self.symmetric_key = sym_key
        
        # Decrypt data with symmetric key
        return self.symmetric_decrypt(encrypted_data)

# Example usage
crypto = AdvancedCryptoSystem()
private_key, public_key = crypto.generate_asymmetric_keys()

# Hybrid encryption
data = b"Secret message"
encrypted_data, encrypted_key, salt = crypto.hybrid_encrypt(data, public_key)

# Hybrid decryption
decrypted = crypto.hybrid_decrypt(encrypted_data, encrypted_key, salt)
print("Decrypted:", decrypted.decode())
