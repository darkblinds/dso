from dao import DAO
from model.usuario import User


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuario.pkl')

    def add(self,usuario: User):
        if (isinstance(usuario.id, int)) and (usuario is not None) and isinstance(usuario, User):
            super().add(usuario.id, usuario)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, int):
            return super().remove(key)