#!/usr/bin/python
# -*- coding: utf-8 -*-
import time


def medir_tempo(func):
    """Decorator para medir o tempo de execução de funções/métodos."""
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"O método '{func.__name__}' demorou {fim - inicio:.6f} segundos para ser executado.")
        return resultado
    return wrapper