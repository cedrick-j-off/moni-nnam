# Moni Nnam — description de la solution

**SAFINUM Innovate Challenge — épreuve de présélection**
Équipe : Moni Nnam

## Le constat de départ

Au Cameroun, on apprend sa langue maternelle à la maison, en l'écoutant et en la parlant. On ne l'apprend presque jamais à l'école. Le résultat est connu de tous : beaucoup de personnes comprennent et parlent très bien leur langue, le bàsàa ou l'éton par exemple, mais ne savent ni la lire ni l'écrire. Elles n'ont jamais eu de livre, de cahier ou d'écran dans cette langue.

Les applications de banque, de paiement mobile et de microfinance, elles, sont en français ou en anglais. Pour quelqu'un qui lit mal ces deux langues, vérifier un solde, comprendre des frais ou contrôler le nom d'un bénéficiaire avant d'envoyer de l'argent devient difficile. Cette personne demande alors à un proche de le faire à sa place, avec les risques que cela comporte, ou bien elle renonce au service.

Traduire l'écran ne suffit donc pas. Si l'on se contente d'afficher du texte en langue nationale, on aide ceux qui lisent déjà cette langue, et ils sont peu nombreux. Ceux qui en ont le plus besoin restent devant un écran qu'ils ne peuvent pas lire, dans une langue qu'ils parlent pourtant tous les jours.

## Notre idée : faire parler l'écran

Moni Nnam part de ce que les gens savent faire : écouter. C'est une extension pour les navigateurs Chrome et Edge qui fait entendre un service financier en bàsàa et en éton, en plus de l'afficher. Elle ne change rien au service lui-même. Son code, ses serveurs et ses données restent ce qu'ils sont.

Chaque traduction a sa voix. Quand l'utilisateur passe sur un texte, un petit haut-parleur apparaît à côté. Un clic, et la phrase est dite à voix haute. Un bouton « Lire toute la page » enchaîne toutes les phrases de l'écran, pendant qu'un cadre montre celle qui est en train d'être lue. L'utilisateur peut ainsi se faire expliquer chaque étape d'un transfert : le solde, les frais, le bénéficiaire, le récapitulatif, la confirmation, et même les alertes de sécurité.

Il reste une limite, que nous préférons dire tout de suite. Les montants, les noms et les numéros changent à chaque opération, et on ne peut pas les enregistrer à l'avance. Dans ce prototype, la voix dit donc « solde disponible » ou « frais de transfert », et le chiffre reste affiché à l'écran. Faire dire les nombres par les locuteurs est la suite logique du travail.

## La bonne intonation

Nous n'avons pas utilisé de voix de synthèse. Il n'en existe ni pour le bàsàa ni pour l'éton, et ce ne serait pas une bonne idée. Ce sont deux langues à tons : la hauteur de la voix fait partie du mot, et la même suite de lettres peut changer de sens selon la façon dont on la prononce. Une machine qui lirait le texte à plat serait difficile à comprendre, parfois trompeuse.

Les phrases ont donc été enregistrées une par une, par des personnes qui parlent la langue, avec leur intonation naturelle. C'est aussi ce qui donne confiance. Entendre une voix de chez soi expliquer des frais ou demander de vérifier un numéro, ce n'est pas la même chose qu'entendre un robot.

Pour que l'écoute soit agréable, l'extension règle elle-même chaque enregistrement au moment de le jouer. Elle enlève les silences du début et de la fin et met toutes les phrases au même volume, pour que l'on n'ait pas à monter ou baisser le son d'une phrase à l'autre.

## Le texte, en appui de la voix

Le texte de la page est lui aussi remplacé par sa traduction : les titres, les boutons, les consignes, les messages d'erreur. Il sert à ceux qui lisent la langue, et il aide les autres à faire le lien entre ce qu'ils entendent et ce qu'ils voient. À force d'écouter une phrase en regardant les mots, on finit par les reconnaître.

## Un design qui parle de la langue

Quand on choisit une langue, la page change aussi d'aspect. En bàsàa, un tissu aux palmiers habille l'en-tête et la carte du solde, et les boutons passent au bleu de ce tissu. En éton, c'est un tissu léopard, et les boutons passent au marron. Dans les deux cas, les textes sont composés dans une police dessinée pour les langues africaines, qui affiche correctement leurs lettres et leurs tons.

Ce n'est pas de la décoration. Pour une personne qui ne lit pas, les images et les couleurs sont les premiers repères. En voyant un décor qui lui est familier, elle comprend tout de suite que la page s'adresse à elle, dans sa langue, avant même d'avoir écouté une phrase. Les couleurs qui portent un sens, comme le rouge d'une erreur ou le vert d'un succès, ne sont pas touchées.

Nous avons donné à ce travail de design une vraie part de notre temps. Nous pensons qu'il compte autant que la traduction pour que l'utilisateur ait envie de se servir de l'outil.

## Où en est chaque langue

Le bàsàa est la langue la plus avancée. Toutes les phrases sont traduites et enregistrées.

L'éton n'est pas terminé, et nous préférons le dire. Tous les textes de l'interface sont traduits, mais plusieurs lignes doivent encore être vérifiées avec la personne qui nous a aidés. Côté voix, 49 phrases sur 72 sont enregistrées. Il manque la fin du parcours : le reçu et les messages d'erreur s'affichent en éton, mais ne se font pas encore entendre. Dans le panneau de l'extension, l'éton porte pour cette raison la mention « à confirmer ». Nous avons fait le choix d'avancer en même temps sur le design des deux langues plutôt que de finir l'éton à la hâte. Le détail est donné dans la partie 3.

## Deux règles de prudence

L'extension n'invente jamais rien. Chaque phrase affichée ou entendue vient d'un fichier préparé à l'avance avec un locuteur, et non d'une traduction automatique. Si un texte n'est pas dans nos fichiers, il reste tel quel.

Les valeurs ne sont jamais réécrites. Les montants, les frais, les noms, les numéros, les références et les codes d'erreur s'affichent exactement comme le service les a produits.

## Ce que le prototype montre sur l'environnement de test

| Ce qui est attendu | Où nous en sommes |
|---|---|
| Adapter la langue de l'interface | Fait en bàsàa. Fait en éton, avec des lignes encore à vérifier. |
| Rendre l'interface accessible à l'oral | En bàsàa, 80 textes sur 82 ont une voix. En éton, 57 sur 82 : la fin du parcours reste à enregistrer. |
| Suivre le parcours financier | Fait. Solde, frais, bénéficiaire, récapitulatif et reçu, sans recharger la page. |
| Préserver les informations financières | Fait. Le contrôle d'intégrité de la page de test marque les cinq étapes « intact ». |
| Fonctionner sans toucher au service | Fait. L'extension lit l'affichage et le réécrit, rien d'autre. |
| Gérer un contenu inédit | En partie. Un message connu est traduit dès qu'il apparaît. Un message jamais vu reste dans sa langue d'origine. |

## Ce que cela change

Avec Moni Nnam, une personne qui parle bàsàa ou éton sans le lire comprend ce que chaque écran lui demande. Elle entend ce qu'est le chiffre affiché, ce que signifie un bouton, ce que dit une alerte, et elle peut avancer dans son transfert sans dépendre de quelqu'un d'autre pour lui traduire la page.

La méthode ne dépend ni du service ni de la langue. Il faut une liste de phrases, un locuteur pour les traduire et les dire, et quelques éléments visuels choisis avec lui. Le même travail peut être refait pour une autre application et pour une autre langue nationale.
