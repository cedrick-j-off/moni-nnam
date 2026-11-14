# Moni Nnam — identification linguistique

**SAFINUM Innovate Challenge — épreuve de présélection**
Équipe : Moni Nnam — État au 14 novembre 2026

## Langues nationales prises en charge

Le prototype prend en charge deux langues bantoues du Cameroun. Le bàsàa, que l'on écrit aussi basaa ou bassa, est parlé surtout dans les régions du Centre et du Littoral. L'éton est parlé dans la région du Centre, principalement dans le département de la Lékié.

| Langue | Texte | Voix | État |
|---|---|---|---|
| Bàsàa | 82 textes sur 82 | 80 textes sur 82 | Traduit et enregistré par un locuteur |
| Éton | 82 textes sur 82 | 57 textes sur 82 | En cours : lignes à vérifier, voix incomplète |

L'extension reconnaît la page dans ses deux langues d'origine, le français et l'anglais.

Ces deux langues se transmettent surtout à l'oral. Beaucoup de leurs locuteurs les parlent couramment sans les avoir jamais lues, car elles ne sont presque pas enseignées à l'école. Ce sont aussi des langues à tons, où la hauteur de la voix distingue des mots. Ces deux raisons expliquent notre choix : chaque phrase est donnée par écrit, mais surtout dite par un locuteur, avec son intonation.

## Notre méthode

Aucune phrase n'est fabriquée au moment où l'utilisateur se sert de l'extension. Tout ce qui s'affiche ou s'entend vient d'un fichier préparé à l'avance, qu'un locuteur peut relire ligne par ligne.

Nous décrivons ici la méthode suivie pour le bàsàa, qui a servi de modèle. Nous avons commencé par relever les 72 phrases de l'environnement de test, en notant pour chacune où elle apparaît : un bouton, un titre, un message d'erreur, une alerte. Nous les avons numérotées et remises au locuteur avec quelques consignes simples. Il fallait traduire le sens plutôt que le mot à mot, garder toujours le même mot pour le même terme (transfert, solde, frais, bénéficiaire, montant, compte), ne toucher ni aux noms, ni aux chiffres, ni à « FCFA », et surtout ne pas deviner : en cas de doute, écrire un point d'interrogation.

Les 28 phrases qui parlent d'argent ou de sécurité portaient la mention [IMPORTANT], pour signaler que le sens devait y être exact.

Le locuteur a ensuite enregistré chaque phrase. Les fichiers portent le numéro de la phrase dans la liste, ce qui nous a permis de les rattacher à l'interface.

Chaque phrase a un statut de suivi (à traduire, traduite, approuvée) et une place pour le nom de la personne qui valide. Dans le panneau de l'extension, une langue qui ne serait pas entièrement validée porte une étiquette visible. Enfin, nos tests automatiques vérifient que les montants, les noms, les numéros et les codes ressortent à l'identique, et qu'un texte inconnu n'est jamais modifié.

## Le bàsàa en détail

Les 72 phrases ont été traduites par [nom du locuteur bàsàa], locuteur bàsàa. Nous avons reçu ses traductions le 14 novembre 2026 et nous les avons reprises telles quelles.

Nous n'avons fait que deux retouches, toutes deux pour protéger un nom ou une valeur. Le nom « Safinum Pay », écrit « Safinum pay », a été rétabli. Dans la description des frais, les chiffres sont recopiés depuis la page, car la traduction indiquait « 15% » là où la page affiche « 1,5 % ». De la même façon, dans « Bonjour, Amina » et dans le numéro de compte, la valeur vient toujours de la page.

Pour l'orthographe, la traduction utilise ô, é et ñ, sans les lettres ɓ, ŋ, ɛ, ɔ ni les marques de ton. Nous l'avons gardée ainsi. Comme le texte ne note pas les tons, c'est l'enregistrement qui les porte : une raison de plus pour que la voix accompagne chaque phrase.

Quelques points restent à confirmer avec le locuteur avant la démonstration :

1. « Alerte de sécurité » est rendu par « Biyihne inyu matat » dans le titre, mais par « Bibéhne inyu matat » au début des deux messages d'alerte.
2. Le mot « compte » s'écrit de trois façons : « Kônto », « Konto » et « kôntô ».
3. Les boutons « Fermer » (« Homa liyibne li biyihne ») et « Modifier » (« Lihéñha biyihne ») sont longs pour des boutons. Il faut s'assurer qu'il s'agit bien du libellé et non d'une explication.
4. Une seconde relecture des 28 phrases marquées [IMPORTANT] par une autre personne qui parle bàsàa.

Côté voix, nous avons reçu 72 fichiers, un par phrase, le 14 novembre 2026. Deux ne sont pas joués par l'extension pour l'instant. « Bonjour, Amina » nous est parvenu sans son et doit être refait. La description des frais prononce des chiffres et nous voulons l'écouter avec le locuteur avant de l'activer. Il restera ensuite à écouter chaque enregistrement en face de sa phrase.

## L'éton en détail

La version éton n'est pas terminée. Nous avons partagé notre temps entre cette deuxième langue et le design de l'extension, et nous donnons ici son état exact.

Les traductions ont été établies avec l'aide de [personne ayant aidé à la traduction éton]. Elles ont été écrites à la main dans un cahier, avec les tons, puis nous les avons recopiées à partir de photos. Les 72 phrases portent les mêmes numéros que la liste bàsàa.

Comme pour le bàsàa, nos seules retouches protègent un nom ou une valeur. Le nom « Safinum Pay » a été remis en tête de la mention de bas de page. Le prénom, le numéro de compte et les chiffres des frais sont recopiés depuis la page. Pour « Téléphone », le cahier propose deux mots, « telefon » et « ŋ̀kual lɔŋní » : nous avons gardé le premier en attendant un choix.

Il reste du travail sur le texte. En recopiant le cahier, nous avons hésité sur une trentaine de lignes : des accents de ton très petits sur les photos, des mots raturés, et quelques mots écrits de plusieurs façons d'une ligne à l'autre, comme « mɔ̀ní » et « mɔní » pour l'argent, ou « dzəblə » et « dzəlbə » pour confirmer. Ces lignes sont repérées dans notre fichier de travail et doivent être relues avec la personne qui a traduit.

Côté voix, nous avons 49 notes vocales, pour les phrases 1 à 49. Elles couvrent les éléments communs, le solde, les frais, le bénéficiaire et le début du récapitulatif. Les phrases 50 à 72 n'ont pas encore de voix : la fin du récapitulatif, le reçu, et surtout les messages d'erreur et les alertes de sécurité. Les notes ont été rattachées aux phrases par leur numéro, et une écoute de contrôle reste à faire.

Tant que ce travail n'est pas achevé, l'éton porte la mention « à confirmer » dans le panneau de l'extension.

## Notre engagement

Nous ne présenterons au jury aucun texte comme validé s'il ne vient pas d'un locuteur. Tant qu'une phrase sensible n'est pas confirmée, nous pouvons la laisser en français : il suffit de vider sa ligne dans le fichier de langue, et l'extension ne touche plus au texte de la page.
