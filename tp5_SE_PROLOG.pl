
% TP5 - Système Expert Médical (Prolog)
% Fichier : tp5.pl

% PARTIE 1 — BASE STATIQUE
symptome(p1, fievre).
symptome(p1, toux).
symptome(p1, fatigue).

symptome(p2, mal_gorge).
symptome(p2, fievre).

symptome(p3, eternuements).
symptome(p3, nez_qui_coule).

% Grippe
maladie(grippe, P) :-
    symptome(P, fievre),
    symptome(P, courbatures),
    symptome(P, fatigue).

% Angine
maladie(angine, P) :-
    symptome(P, mal_gorge),
    symptome(P, fievre).

% Covid
maladie(covid, P) :-
    symptome(P, fievre),
    symptome(P, toux),
    symptome(P, fatigue).

% Allergie
maladie(allergie, P) :-
    symptome(P, eternuements),
    symptome(P, nez_qui_coule),
    \+ symptome(P, fievre).

diagnostic(P, M) :- maladie(M, P).

% PARTIE 2 — INTERACTION AVEC L’UTILISATEUR
:- dynamic reponse/2.

a_symptome(S) :-
    reponse(S, oui), !.

a_symptome(S) :-
    reponse(S, non), !, fail.

a_symptome(S) :-
    format("Avez-vous ~w ? (o/n) : ", [S]),
    read(Rep),
    traiter_reponse(S, Rep).

traiter_reponse(S, o) :- assert(reponse(S, oui)), !.
traiter_reponse(S, n) :- assert(reponse(S, non)), !, fail.
traiter_reponse(S, _) :-
    writeln("Tapez seulement o ou n."),
    a_symptome(S).

% Règles dynamiques (diagnostic interactif)
maladie_dyn(grippe) :-
    a_symptome(fievre),
    a_symptome(courbatures),
    a_symptome(fatigue).

maladie_dyn(angine) :-
    a_symptome(mal_gorge),
    a_symptome(fievre).

maladie_dyn(covid) :-
    a_symptome(fievre),
    a_symptome(toux),
    a_symptome(fatigue).

maladie_dyn(allergie) :-
    a_symptome(eternuements),
    a_symptome(nez_qui_coule),
    \+ a_symptome(fievre).

trouver_maladies(L) :-
    findall(M, maladie_dyn(M), L).

% PARTIE 3 — EXPLICATION
symptomes_maladie(grippe, [fievre, courbatures, fatigue]).
symptomes_maladie(angine, [mal_gorge, fievre]).
symptomes_maladie(covid, [fievre, toux, fatigue]).
symptomes_maladie(allergie, [eternuements, nez_qui_coule]).

symptomes_confirmes([], []).
symptomes_confirmes([S|R], [S|RC]) :-
    reponse(S, oui), !,
    symptomes_confirmes(R, RC).
symptomes_confirmes([_|R], RC) :-
    symptomes_confirmes(R, RC).

afficher_resultats([]) :-
    writeln("Aucune maladie trouvée.").

afficher_resultats([M|_]) :-
    format("\nPossible diagnostic : ~w\n", [M]),
    symptomes_maladie(M, Liste),
    symptomes_confirmes(Liste, Conf),
    format("Car vous présentez : ~w\n", [Conf]).

expert :-
    retractall(reponse(_, _)),
    writeln("\n=== SYSTEME EXPERT MEDICAL ==="),
    trouver_maladies(L),
    afficher_resultats(L).
