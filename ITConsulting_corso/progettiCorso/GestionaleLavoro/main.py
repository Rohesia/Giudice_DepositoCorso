from dipendente import Dipendente
from ruoli import Manager, Operaio, Security
from badge import Badge
from turno import Turno
from log import LogIngresso
from menu import Menu, MenuItem

# --- Log centrale ---
log_centrale = LogIngresso()

# --- Badge ---
badge_manager = Badge(101, ["uffici", "archivi"])
badge_operaio = Badge(102, ["produzione"])
badge_security = Badge(103, ["uffici", "archivi", "produzione", "laboratori"])

# --- Turni ---
turno_mattina = Turno("08:00", "16:00")
turno_pomeriggio = Turno("16:00", "23:00")
turno_notturno = Turno("23:00", "06:00", tipo="notturno")

# --- Ruoli ---
manager = Manager("Manager")
operaio = Operaio("Operaio")
security = Security("Security")

# --- Dipendenti ---
dip1 = Dipendente("Ludovica", "M.", "LM123", manager, badge_manager, [turno_mattina])
dip2 = Dipendente("Marco", "Rossi", "MR456", operaio, badge_operaio, [turno_pomeriggio])
dip3 = Dipendente("Anna", "Bianchi", "AB789", security, badge_security, [turno_notturno])
dipendenti = [dip1, dip2, dip3]

# --- Funzioni da input
def mostra_info_dipendenti():
    for idx, d in enumerate(dipendenti, 1):
        print(f"{idx}. {d.info()}")

def ingresso_dipendente():
    mostra_info_dipendenti()
    scelta = input("Seleziona dipendente per ingresso: ").strip()
    if not scelta.isdigit() or not 1 <= int(scelta) <= len(dipendenti):
        print("Scelta non valida")
        return
    ora = input("Inserisci ora (HH:MM): ").strip()
    dipendenti[int(scelta)-1].entra_in_azienda(ora, log_centrale)

def uscita_dipendente():
    mostra_info_dipendenti()
    scelta = input("Seleziona dipendente per uscita: ").strip()
    if not scelta.isdigit() or not 1 <= int(scelta) <= len(dipendenti):
        print("Scelta non valida")
        return
    ora = input("Inserisci ora (HH:MM): ").strip()
    dipendenti[int(scelta)-1].esce_dall_azienda(ora, log_centrale)

def attiva_disattiva_badge():
    mostra_info_dipendenti()
    scelta = input("Seleziona dipendente per gestire badge: ").strip()
    if not scelta.isdigit() or not 1 <= int(scelta) <= len(dipendenti):
        print("Scelta non valida")
        return
    d = dipendenti[int(scelta)-1]
    azione = input("Scrivi 'attiva' o 'disattiva': ").strip().lower()
    if azione == "attiva":
        d.get_badge().attiva()
    elif azione == "disattiva":
        d.get_badge().disattiva()
    else:
        print("Azione non valida")

def modifica_turno():
    mostra_info_dipendenti()
    scelta = input("Seleziona dipendente per modificare turno: ").strip()
    if not scelta.isdigit() or not 1 <= int(scelta) <= len(dipendenti):
        print("Scelta non valida")
        return
    d = dipendenti[int(scelta)-1]
    ora_in = input("Inserisci nuova ora entrata (HH:MM): ").strip()
    ora_out = input("Inserisci nuova ora uscita (HH:MM): ").strip()
    tipo = input("Tipo turno (normale/straordinario/notturno): ").strip().lower()
    nuovo_turno = Turno(ora_in, ora_out, tipo)
    d.get_ruolo().modifica_turno(d, nuovo_turno)

def segnalazione_guasto():
    mostra_info_dipendenti()
    scelta = input("Seleziona dipendente per segnalare guasto: ").strip()
    if not scelta.isdigit() or not 1 <= int(scelta) <= len(dipendenti):
        print("Scelta non valida")
        return
    area = input("Inserisci area del guasto: ").strip()
    dipendenti[int(scelta)-1].get_ruolo().segnala_guasto(area)

def mostra_log():
    log_centrale.mostra_report()

# --- Menu interattivo ---
menu = Menu("Gestionale Ingresso Azienda Interattivo")
menu.aggiungi_voce(MenuItem("Mostra info dipendenti", "Visualizza info di tutti i dipendenti", mostra_info_dipendenti))
menu.aggiungi_voce(MenuItem("Ingresso dipendente", "Registra ingresso manuale", ingresso_dipendente))
menu.aggiungi_voce(MenuItem("Uscita dipendente", "Registra uscita manuale", uscita_dipendente))
menu.aggiungi_voce(MenuItem("Attiva/Disattiva badge", "Gestisci stato badge dipendente", attiva_disattiva_badge))
menu.aggiungi_voce(MenuItem("Modifica turno", "Modifica turno dipendente", modifica_turno))
menu.aggiungi_voce(MenuItem("Segnalazione guasto", "Segnalazione guasto da dipendente", segnalazione_guasto))
menu.aggiungi_voce(MenuItem("Mostra log completo", "Visualizza entrate, uscite e errori", mostra_log))

if __name__ == "__main__":
    menu.seleziona()
