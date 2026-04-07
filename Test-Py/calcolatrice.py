import tkinter as tk
from tkinter import messagebox

class Calcolatrice:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcolatrice Python")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        self.equazione = ""
        
        # Schermo di visualizzazione
        self.display_var = tk.StringVar(value="0")
        self.crea_interfaccia()

    def crea_interfaccia(self):
        # Display
        display_frame = tk.Frame(self.root, bg="#1e1e1e", padx=10, pady=20)
        display_frame.pack(expand=True, fill="both")

        self.label = tk.Label(
            display_frame, textvariable=self.display_var, 
            anchor="e", bg="#1e1e1e", fg="white", 
            font=("Arial", 32, "bold"), padx=10
        )
        self.label.pack(expand=True, fill="both")

        # Griglia tasti
        buttons_frame = tk.Frame(self.root, bg="#1e1e1e", padx=10, pady=10)
        buttons_frame.pack(expand=True, fill="both")

        tasti = [
            'C', 'DEL', '/', '*',
            '7', '8', '9', '-',
            '4', '5', '6', '+',
            '1', '2', '3', '=',
            '0', '.', 
        ]

        # Configurazione righe e colonne
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)

        row = 0
        col = 0
        for tasto in tasti:
            azione = lambda x=tasto: self.clic_tasto(x)
            
            # Colori tasti
            bg_color = "#333333"
            fg_color = "white"
            if tasto in ['/', '*', '-', '+', '=']:
                bg_color = "#ff9500"
            elif tasto in ['C', 'DEL']:
                bg_color = "#a5a5a5"
                fg_color = "black"

            # Gestione larghezza tasto 0 e =
            if tasto == '0':
                btn = tk.Button(buttons_frame, text=tasto, command=azione, bg=bg_color, fg=fg_color, font=("Arial", 14, "bold"), border=0)
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
                col += 1
            elif tasto == '=':
                btn = tk.Button(buttons_frame, text=tasto, command=azione, bg=bg_color, fg=fg_color, font=("Arial", 14, "bold"), border=0)
                btn.grid(row=row, column=col, rowspan=2, sticky="nsew", padx=2, pady=2)
            else:
                btn = tk.Button(buttons_frame, text=tasto, command=azione, bg=bg_color, fg=fg_color, font=("Arial", 14, "bold"), border=0)
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def clic_tasto(self, tasto):
        if tasto == 'C':
            self.equazione = ""
        elif tasto == 'DEL':
            self.equazione = self.equazione[:-1]
        elif tasto == '=':
            try:
                # eval() calcola la stringa matematicamente
                risultato = str(eval(self.equazione))
                self.equazione = risultato
            except:
                messagebox.showerror("Errore", "Operazione non valida")
                self.equazione = ""
        else:
            self.equazione += str(tasto)
        
        # Aggiorna il display (gestisce il vuoto come 0)
        self.display_var.set(self.equazione if self.equazione != "" else "0")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calcolatrice(root)
    root.mainloop()