# 🛒 Projet : Panier E-commerce (TDD)

## 🎯 Objectif
Développer un module de panier d'achat capable de calculer un prix total en appliquant des règles de gestion métier, tout en suivant la méthodologie TDD (Test Driven Development).

## 📋 Spécifications Fonctionnelles (Règles Métier)

1.  **Ajout de produits :** Le panier doit permettre d'ajouter des articles avec un nom et un prix.
2.  **Calcul du total de base :** Le total est la somme arithmétique des prix de tous les articles présents dans le panier.
3.  **Règle de promotion (Discount) :** * SI le total du panier est **strictement supérieur à 100€**.
    * ALORS une réduction automatique de **10%** est appliquée sur l'ensemble du montant.
    
## 🧪 Plan de Tests (Scénarios TDD)

Nous allons implémenter le panier en suivant ces étapes :

| # | Scénario | Données (Input) | Résultat Attendu | Règle Métier |
|---|---|---|---|---|
| **1** | **Total Simple** | Pomme (10.0), Banane (5.0) | **15.0** | Somme basique des prix. |
| **2** | **Limite (Edge Case)** | Article A (50.0), Article B (50.0) | **100.0** | Pas de réduction si pile à 100€. |
| **3** | **Réduction (-10%)** | Champagne (100.0), Caviar (100.0) | **180.0** | (200 - 10%) car > 100€. |