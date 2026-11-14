# Moni Nnam — note technique

**SAFINUM Innovate Challenge — épreuve de présélection**
Version du prototype : 0.11.0 — Équipe : Moni Nnam

## Architecture

Moni Nnam est une extension de navigateur au format Manifest V3, pour Chrome et Edge. Elle fonctionne entièrement dans le navigateur de l'utilisateur. Il n'y a pas de serveur, pas de compte à créer et aucun appel réseau.

Le fonctionnement tient en trois temps. Un script injecté dans la page parcourt les textes affichés. Pour chacun, il interroge un petit moteur de correspondance qui retrouve le texte source, en français ou en anglais, et renvoie son équivalent en bàsàa. Le script remplace alors le texte à l'écran et continue de surveiller la page, pour traiter tout ce qui apparaît ensuite.

Chaque texte reconnu porte une clé, et c'est cette clé qui le relie à son enregistrement. La voix et le texte ne peuvent donc pas se décaler : une phrase affichée a toujours la voix qui lui correspond, ou pas de voix du tout.

| Fichier | Rôle |
|---|---|
| `locales/index.json` | La liste des langues et la forme autorisée des variables. |
| `locales/<langue>.json` | Une table clé → texte par langue, avec les mêmes 82 clés partout. Une valeur vide signifie que le texte de la page est laissé tel quel. |
| `engine.js` | Le moteur de correspondance. Il n'a accès ni à la page ni au réseau. |
| `content.js` | Le script de page. Il remplace les textes reconnus et quatre attributs de libellé (`aria-label`, `title`, `placeholder`, `alt`), observe les changements, mémorise la langue choisie et dessine le bouton, le panneau et le haut-parleur. |
| `audio/basaa.json` et `audio/basaa/` | Les enregistrements du locuteur et la table qui relie chaque clé à son fichier. |
| `signal.js` | L'analyse du son au moment de l'écoute : elle écarte les silences de début et de fin et ramène toutes les voix au même niveau. Les fichiers ne sont pas modifiés. |
| `themes/` | La feuille de style du thème bàsàa, l'image du tissu et la police. Elle ne s'applique que lorsque le bàsàa est choisi. |

Certains textes mélangent un libellé et des valeurs, par exemple « Frais de 1,5 % (min. 100 FCFA, max. 2 500 FCFA) ». Pour ces cas, le fichier de langue contient un gabarit, `Frais de {taux} % (min. {min} FCFA, max. {max} FCFA)`. Le moteur traduit le libellé et recopie chaque valeur à l'identique. S'il ne retrouve pas toutes les valeurs dans le résultat, il ne remplace rien.

## L'écoute

L'écoute est la fonction principale de l'extension, puisqu'elle s'adresse à des personnes qui parlent le bàsàa sans le lire.

Les enregistrements sont de simples fichiers audio livrés avec l'extension, un par phrase. Quand l'utilisateur survole un texte ou y arrive au clavier, le script cherche l'enregistrement de sa clé et affiche le haut-parleur s'il existe. Le bouton « Lire toute la page » relève les textes de l'écran qui ont une voix, dans l'ordre de la page, et les joue l'un après l'autre. Un cadre suit la phrase en cours et la page défile si nécessaire. Un second clic ou la touche Échap arrête la lecture.

Les fichiers reçus du locuteur n'ont pas tous le même volume, et certains commencent ou finissent par un silence. Plutôt que de les retoucher, nous les mesurons au moment de l'écoute. Le script repère où la voix commence et où elle finit, coupe les silences, et règle le gain pour ramener chaque phrase à −20 dBFS sans dépasser −1 dBFS en crête. L'intonation du locuteur n'est pas modifiée : ni la vitesse ni la hauteur de la voix ne sont touchées.

Les valeurs, c'est-à-dire les montants, les noms et les numéros, ne sont pas prononcées en bàsàa. Elles changent à chaque opération et n'ont pas d'enregistrement.

## Intégration au service

L'extension s'installe dans le navigateur et ne demande aucune modification du service. Elle ne réécrit que le texte affiché. Elle n'écrit jamais dans un champ de saisie, ne clique sur rien, ne saute aucune étape et n'intercepte aucune requête.

La page de test change d'étape sans se recharger. Nous utilisons donc un observateur de mutations, qui traite tout contenu ajouté ou modifié après le chargement. Cela couvre les messages d'erreur, les alertes et le passage du français à l'anglais par le bouton de la page.

Le bouton de l'extension, le panneau de langue et le haut-parleur sont dessinés dans un Shadow DOM, à l'écart du contenu de la page. Ils n'ajoutent aucun texte dans les éléments que la page contrôle.

Pour adapter l'extension à un autre service, il suffit d'ajouter son adresse dans `manifest.json` et de fournir ses fichiers d'équivalences. Pour ajouter une langue, on crée son fichier dans `locales/`, on l'inscrit dans `index.json`, puis on dépose les enregistrements. Le moteur et le script de page ne changent pas.

## Sécurité et préservation des informations financières

Les montants, la devise, les noms, les numéros de compte et de téléphone, les références, les dates, les codes d'erreur et les valeurs saisies ne sont jamais réécrits. Un texte qui ne figure pas dans nos fichiers n'est pas modifié non plus.

L'extension ne collecte rien. Ce qui s'affiche n'est ni stocké ni transmis. La seule information enregistrée, sur l'appareil, est la langue choisie. Les textes, les enregistrements, la police et l'image du thème sont livrés avec l'extension. Pour le français et l'anglais, la lecture à voix haute passe par une voix de synthèse installée sur l'appareil, et nous écartons les voix en ligne du navigateur pour qu'aucun texte ne parte vers un serveur.

Un enregistrement qui prononce une valeur, comme « Bonjour, Amina » ou le numéro de compte, n'est proposé que si la page affiche exactement cette valeur.

La seule autorisation utile est `storage`, pour mémoriser la langue. Le manifeste déclare encore une adresse locale et un service worker, qui viennent d'un essai antérieur et ne servent plus.

## Vérification

| Test | Ce qu'il vérifie | Résultat au 14 novembre 2026 |
|---|---|---|
| `node outils/tester_moteur.js` | 492 correspondances (82 clés, 3 langues, 2 langues source), les valeurs conservées dans les gabarits, les textes inconnus laissés intacts, la présence des fichiers audio. | 0 échec |
| `node outils/tester_navigateur.js` | Un parcours complet sur la page de test officielle, dans Edge sans fenêtre : changement de langue, cinq étapes, alerte de sécurité, contenu ajouté après le chargement, bascule français/anglais, langue mémorisée, écoute d'un enregistrement, thème, journal d'intégrité de la page. | 0 échec, cinq étapes « intact » |
| `node outils/analyser_audio.js` | La mesure des 72 enregistrements : durée, silences, niveau, crête, bruit. | Écart de niveau entre fichiers ramené de 7 dB à 0,4 dB |

Nous n'avons pas encore testé le panneau jury de la page (`?jury=1`), le navigateur Chrome, un lecteur d'écran ni un écran tactile.

## Dépendances et composants tiers

| Composant | Usage | Licence ou statut |
|---|---|---|
| Chrome ou Edge (Manifest V3) | Exécution de l'extension. | — |
| Aucune bibliothèque JavaScript | L'extension est écrite sans dépendance. | — |
| Node.js 22 ou plus récent | Scripts de test uniquement. | — |
| Python 3 | Scripts de préparation uniquement. | — |
| Police Andika, SIL International | Police du thème bàsàa, livrée en version réduite. | SIL Open Font License 1.1 |
| Image du tissu aux palmiers | Habillage de l'en-tête et de la carte du solde. | Image fournie par l'équipe |
| *Dictionnaire français-basaa*, P. E. Njock, 2005 | Consulté au début du projet. Les textes actuels viennent du locuteur. | Licence non indiquée |
| Claude (Anthropic) | Assistant de programmation, utilisé pour le code, les scripts et la mise en forme de la documentation. | Non embarqué dans l'extension |
| Ollama, modèle Aya Expanse | Premier essai de traduction automatique locale, abandonné. | Ne sert plus |

Ce qui vient de l'équipe : l'idée de s'appuyer sur des équivalences fournies par un locuteur, le moteur de correspondance et ses gabarits, le script de page, le thème, l'écoute avec analyse du son, la collecte des traductions et des enregistrements, et les outils de test.

## Limites connues

Nous préférons les donner clairement.

Un message qui n'est pas dans nos fichiers reste dans sa langue d'origine. C'est un choix de sécurité, mais cela veut dire que l'exigence sur le contenu inédit n'est couverte qu'en partie.

Le bàsàa vient d'un locuteur, mais il n'a pas encore été relu par une seconde personne. Le texte affiché n'a pas non plus été comparé mot à mot aux enregistrements.

La voix ne dit pas encore les montants, les noms ni les numéros. Une personne qui ne lit pas du tout les chiffres a donc toujours besoin d'aide pour cette partie. C'est la limite la plus importante par rapport à notre objectif, et la première que nous voulons lever.

Sur 82 textes, 80 ont un enregistrement. Deux fichiers ne sont pas joués : « Bonjour, Amina », reçu sans son, et la description des frais, dont les chiffres prononcés doivent être vérifiés. L'analyse du son égalise le volume, mais elle ne corrige pas le bruit de fond.

L'habillage bàsàa est notre proposition. Il n'a pas encore été présenté à des membres de la communauté. En mode sombre, la page garde ses fonds et seuls les accents, le tissu et la police changent.

La lecture en français et en anglais dépend des voix installées sur l'appareil. Sans voix locale, elle n'est pas proposée.

Quand un même texte source sert à deux endroits, comme « Frais » qui est à la fois une étape et un libellé, la première traduction est utilisée.

Enfin, l'extension n'est active que sur la page de test, dans Chrome et Edge sur ordinateur. Il n'y a pas de version mobile, et sur un écran tactile le haut-parleur est peu pratique, car il apparaît au survol.
