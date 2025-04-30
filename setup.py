from setuptools import setup, find_packages

setup(
    name="quickpkg",                                                # Nombre del paquete
    version="0.1.0",                                                # Versión inicial
    packages=find_packages(),                                       # Paquetes a incluir
    description="Un paquete pip simple",                            # Breve descripción
    author="Lionel Martínez",                                       # Tu nombre
    url="https://github.com/LionelMc/projPractice---quickpkg",      # URL del proyecto
)