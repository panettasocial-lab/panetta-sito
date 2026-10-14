# MENU PANETTA BAKERY — modifica qui prezzi e prodotti, poi: python3 _build.py
# (nome, prezzo, unità, nota)
MENU = [
  {"id": "pasta", "titolo": "Pasta fresca", "gruppi": [
    (None, [(n, "6,00", "al Kg", nota) for n, nota in [
      ("Chitarra", ""), ("Chitarrina", ""), ("Fettuccina", ""), ("Tagliatella", ""), ("Pappardella", ""),
      ("Fili d'angelo", ""), ("Maltagliati", ""), ("Quadrucci", ""), ("Tagliolini", "schiacciati o tondi")]])]},
  {"id": "pane", "titolo": "Il nostro pane", "gruppi": [
    (None, [
      ("Pane casereccio", "2,70", "al Kg", ""), ("Pane casereccio affettato", "3,20", "al Kg", ""),
      ("Pane pugliese", "3,20", "al Kg", ""), ("Pane semintegrale", "3,20", "al Kg", ""),
      ("Pane integrale", "3,60", "al Kg", ""), ("Pane al granturco", "3,60", "al Kg", ""),
      ("Pane ai cereali", "3,80", "al Kg", ""), ("Pane con le noci", "3,80", "al Kg", ""),
      ("Panini", "3,60", "al Kg", ""), ("Panini integrali", "3,60", "al Kg", ""),
      ("Scrocchiarelle", "3,60", "al Kg", ""), ("Scarapiccia", "3,60", "al Kg", ""),
      ("Ciabatta pugliese", "3,60", "al Kg", ""), ("Pizza olio & sale", "4,00", "al Kg", ""),
      ("Pane grattugiato", "3,00", "al Kg", "")])]},
  {"id": "pizza", "titolo": "Pizza & fritti", "gruppi": [
    ("Pizza al taglio", [("Margherita", "1,00", "", ""), ("+1 gusto", "1,10", "", ""), ("+2 gusti", "1,20", "", ""),
                         ("+3 gusti", "1,30", "", ""), ("Aggiunta di tartufo", "0,50", "", "")]),
    ("Pizza in pala", [("Margherita", "1,20", "", ""), ("Farcita", "1,50", "", ""), ("Ricoperta", "1,80", "", "")]),
    ("I fritti", [("Frittelle piccole", "0,80", "", ""), ("Frittelle grandi", "1,20", "", ""),
                  ("Calzoni piccoli", "0,80", "", ""), ("Calzoni grandi", "1,20", "", ""),
                  ("Panzerotti con sugo", "1,00", "", ""), ("Calzoni cotto, funghi e tartufo", "1,10", "", ""),
                  ("Calzoni al forno", "1,00", "", "")])]},
  {"id": "primi", "titolo": "Primi piatti", "gruppi": [
    (None, [("Chitarra con ragù", "6,00", "", ""), ("Fettuccina alla boscaiola", "6,00", "", ""),
            ("Spaghetti alla carbonara", "6,00", "", ""), ("Tagliatelle porcini e tartufo", "8,00", "", ""),
            ("Boscaiola", "6,00", "", ""), ("Maltagliati zucchine e pachino", "6,00", "", ""),
            ("Tajarill e lenticchie", "6,00", "", ""), ("Tajarill e fagioli", "6,00", "", ""),
            ("Tajarill e ceci", "6,00", "", ""), ("Pasta al forno", "6,00", "", ""),
            ("Lasagna", "6,00", "", "su ordinazione"), ("Timballo", "6,00", "", "su ordinazione")])]},
  {"id": "torte", "titolo": "Torte & goloserie", "gruppi": [
    ("Monoporzione", [("Kinder Paradiso", "1,50", "al pezzo", ""), ("Nesquik", "1,50", "al pezzo", ""),
                      ("Cheesecake", "20,00", "al Kg", "")]),
    ("Su prenotazione", [("Torta casereccia", "14,00", "al Kg", ""), ("Torta moka", "14,00", "", ""),
                         ("Torta mimosa", "16,00", "", ""), ("Torta millefoglie", "16,00", "", "ostia a parte"),
                         ("Torte speciali", "20,00", "", "")])]},
  {"id": "biscotti", "titolo": "Biscotteria", "gruppi": [
    (None, [("Biscotti", "15,00", "al Kg", ""),
            ("Bocconotti", "15,00", "al Kg", "tradizionali, cioccolato, crema al limone, pistacchio, yogurt ai frutti di bosco"),
            ("Biscotti ripieni", "14,00", "al Kg", ""), ("Biscotti di pasta frolla", "11,00", "al Kg", ""),
            ("Crostatine", "15,00", "al Kg", ""), ("Mustaccioli", "15,00", "al Kg", ""),
            ("Taralli al vino e noci", "14,00", "al Kg", ""), ("Taralli ai semi di anice", "14,00", "al Kg", ""),
            ("Taralli integrali", "14,00", "al Kg", ""), ("Taralli di Sant'Antonio", "11,00", "al Kg", ""),
            ("Taralli semidolci di San Biagio", "11,00", "al Kg", ""), ("Mandorlati", "15,00", "al Kg", ""),
            ("Cantucci", "14,00", "al Kg", ""), ("Pepatelli", "14,00", "al Kg", ""),
            ("Maritozzi", "7,00", "al Kg", ""), ("Uccelletti", "14,00", "al Kg", ""),
            ("Biscotti casarecci", "7,00", "al Kg", ""), ("Zeppole", "1,50", "al pezzo", ""),
            ("Ciambelloni", "14,00", "al Kg", ""), ("Crostate", "11,00", "al Kg", ""),
            ("Sbriciolate", "11,00", "al Kg", ""), ("Torta all'amaretto con crema", "12,00", "al Kg", ""),
            ("Torta di mele", "12,00", "al Kg", "")])]},
  {"id": "cornetti", "titolo": "Cornetti & dolci", "gruppi": [
    (None, [(n, "1,20", "", "") for n in [
      "Treccia alle noci", "Girella con gocce di cioccolato", "Saccottino Nutella", "Saccottino gocce di cioccolato",
      "Conchiglia alla crema di latte", "Strudel di mele", "Cornetto vegano", "Cornetto alla crema",
      "Cornetto marmellata", "Cornetto ai frutti di bosco", "Cornetto crema di pistacchio",
      "Cornetto alla Nutella", "Cornetto integrale"]] + [("Cornetto vuoto", "1,00", "", "")])]},
  {"id": "caffetteria", "titolo": "Caffetteria", "gruppi": [
    (None, [("Caffè", "1,00", "", ""), ("Caffè decaffeinato", "1,00", "", ""), ("Cappuccino", "1,30", "", ""),
            ("Latte", "1,00", "", ""), ("Latte macchiato", "1,10", "", ""), ("Orzo", "1,20", "", ""),
            ("Ginseng", "1,20", "", ""), ("Cappuccino orzo / ginseng", "1,40", "", ""),
            ("Caffè americano", "2,00", "", ""), ("Caffè americano macchiato", "2,30", "", ""),
            ("Tisana & biscotti", "2,00", "", ""), ("Cioccolate", "3,00", "", "")])]},
]
