#!/usr/bin/python
# -*- coding: utf-8 -*-

class EventManager:
    """Sujeito (Subject) do padrão Observer."""
    def __init__(self):
        self._observadores = []

    def inscrever(self, observador):
        """Adiciona um novo observador à lista."""
        self._observadores.append(observador)

    def desinscrever(self, observador):
        """Remove um observador da lista."""
        self._observadores.remove(observador)

    def notificar(self, evento: str, dados=None):
        """Notifica todos os observadores sobre um evento acontecido."""
        for obs in self._observadores:
            obs.receber_notificacao(evento, dados)


class ScoreHUD:
    """Observador para o Placar / Interface de Usuário."""
    def receber_notificacao(self, evento: str, dados=None):
        if evento == "inimigo_derrotado":
            print(f"[HUD] Inimigo derrotado! Pontos somados: {dados}")
        elif evento == "jogador_dano":
            print(f"[HUD] Jogador recebeu dano! Vida restante: {dados}")