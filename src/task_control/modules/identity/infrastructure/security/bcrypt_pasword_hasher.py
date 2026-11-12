
import bcrypt

class BcryptPasswordHasher:
    """ Adapteur de hashage de mot de passe """
    
    FACTEUR_TRAVAIL=12

    def __init__(self,rounds:int=FACTEUR_TRAVAIL) -> None :
        self._rounds=rounds

    def _encode_password(self,password) -> bytes:

        if not isinstance(password,str):
            raise TypeError ("Le mot de pass doit etre une chaine de caractere !")

        password_bytes=password.encode("utf-8") # parceque unicode est limité à 72 octet et non 72 caracteres

        if len(password_bytes) > 72 : 
            raise ValueError ("La taille du mot de pass ne doit pas depasser plus de 72 caractere !")

        return password_bytes


    def hash(self,password :str) -> str:

        password_bytes= self._encode_password(password)

        salt = bcrypt.gensalt(rounds=self._rounds) # sel aleatoir pour l'unicité au cas ou deux personne aurai le meme mdp

        hashed_password=bcrypt.hashpw(password_bytes,salt)

        return hashed_password.decode("utf-8")


    def verify(self,password,hashed_password) -> bool : 

        try:
            password_bytes = self._encode_password(password)

            return bcrypt.checkpw(
                    password_bytes,
                    hashed_password.encode("utf-8")
                )
        
        except (ValueError,TypeError,UnicodeError):
            return False

    

